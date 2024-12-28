from SchemeParser import SchemeParser
from SchemeVisitor import SchemeVisitor
from antlr4.tree.Tree import TerminalNodeImpl

import sys

# Tablas globales
FunctionTable = {}   # Almacena las funciones (nombre y parametros)
SymbolTable = [{}]   # Pila de scopes de variables

# Diccionarios de operaciones
ArithmeticDicc = {
    '+': lambda x, y: x + y, 
    '-': lambda x, y: x - y, 
    '*': lambda x, y: x * y, 
    '/': lambda x, y: x // y if y != 0 else Exception("Error: Division by zero"),
    'mod': lambda x, y: x % y if y != 0 else Exception("Error: Division by zero"),
    '^': lambda x, y: x ** y
}

LogicDicc = {
    '<':  lambda a, b: a < b, 
    '<=': lambda a, b: a <= b, 
    '>':  lambda a, b: a > b, 
    '>=': lambda a, b: a >= b, 
    '<>': lambda a, b: a != b, 
    '=':  lambda x, y: x == y, 
    'and': lambda a, b: a and b, 
    'or':  lambda a, b: a or b,
    'not': lambda a: not a  
}


class EvalVisitor(SchemeVisitor):
    """
    Visitador principal. Recorre el arbol AST y
    evalua cada nodo segun su tipo.
    """

    def visit(self, ctx):
        return super().visit(ctx)

    def visitRoot(self, ctx):
        result = 0
        for child in ctx.getChildren():
            temp = self.visit(child)
            # Guardamos el ultimo resultado no-nulo
            if temp is not None:
                result = temp
        return result

    # ---------------------------
    #  Expresiones Aritmeticas
    # ---------------------------
    def visitArithmeticExpr(self, ctx):
        operator = ctx.getChild(1).getText()
        left = self.visit(ctx.getChild(2))
        right = self.visit(ctx.getChild(3))
        return ArithmeticDicc[operator](left, right)

    # ---------------------------
    #   Expresiones Logicas
    # ---------------------------
    def visitLogicalExpr(self, ctx):
        operator = ctx.getChild(1).getText()
        try:
            args = [self.visit(expr) for expr in ctx.expr()]
        except Exception as e:
            raise Exception(f"Error en la evaluacion de argumentos para '{operator}': {e}")

        if not args:
            raise Exception(f"Error: Ninguna condicion valida para el operador logico '{operator}'.")

        if operator not in LogicDicc:
            raise Exception(f"Error: Operador logico '{operator}' no definido.")

        if operator == 'not':
            if len(args) != 1:
                raise Exception(f"Error: El operador 'not' espera un unico argumento, pero recibio {len(args)}.")
            return '#t' if LogicDicc[operator](args[0]) else '#f'

        if operator in ['and', 'or']:
            if len(args) != 2:
                raise Exception(f"Error: El operador '{operator}' espera exactamente dos argumentos, pero recibio {len(args)}.")
            return '#t' if LogicDicc[operator](args[0], args[1]) else '#f'

        raise Exception(f"Error: Operador logico '{operator}' no soportado.")

    # ---------------------------
    #       If y Cond
    # ---------------------------
    def visitIfExpr(self, ctx):
        condition = self.visit(ctx.expr(0))
        if condition:
            return self.visit(ctx.expr(1))
        else:
            return self.visit(ctx.expr(2))

    def visitCondExpr(self, ctx):
        for clause in ctx.condClause():
            # Clausula normal
            if isinstance(clause, SchemeParser.CondClauseExprContext):
                condition = self.visit(clause.expr(0))
                if condition:
                    return self.visit(clause.expr(1))
            # Clausula else
            if isinstance(clause, SchemeParser.CondElseClauseContext):
                return self.visit(clause.expr())
        return None

    # ---------------------------
    #        Declaraciones
    # ---------------------------
    def visitDeclaration(self, ctx):
        # Constante
        if ctx.constantDeclaration():
            constant_name = ctx.constantDeclaration().ID().getText()
            if not self.validate_identifier(constant_name):
                print(f"ERROR: No se pudo procesar la constante '{constant_name}' debido a un identificador invalido.")
                return None
            return self.visit(ctx.constantDeclaration())

        # Funcion
        elif ctx.functionDeclaration():
            function_name = ctx.functionDeclaration().ID(0).getText()
            if not self.validate_identifier(function_name):
                print(f"ERROR: No se pudo procesar la funcion '{function_name}' debido a un identificador invalido.")
                return None
            return self.visit(ctx.functionDeclaration())

        else:
            raise Exception("Error: Declaracion desconocida.")

    def visitConstantDeclaration(self, ctx):
        constant_name = ctx.ID().getText()
        # Verificamos si la constante ya existe
        if any(constant_name in scope for scope in SymbolTable):
            raise Exception(f"Error: La constante '{constant_name}' ya esta definida.")
        value = self.visit(ctx.expr())
        SymbolTable[0][constant_name] = value
        return constant_name
    

    def visitFunctionDeclaration(self, ctx):
        function_name = ctx.ID(0).getText()
        params = [param.getText() for param in ctx.ID()[1:]]
        block = ctx.block()
        FunctionTable[function_name] = (params, block)
        return function_name

    # ---------------------------
    #       Bloques y Stmts
    # ---------------------------
    def visitBlock(self, ctx):
        result = 0
        for stmt in ctx.stmt():
            temp = self.visit(stmt)
            if temp is not None:
                result = temp
        return result

    # ---------------------------
    #   Expresiones de Variables
    # ---------------------------
    def validate_identifier(self, identifier):
        import re
        pattern = r"^[a-zA-Z][a-zA-Z0-9?-]*;*$"
        if not re.match(pattern, identifier):
            print(f"ERROR: Identificador invalido '{identifier}'. "
                  f"Un identificador debe comenzar con letra y solo puede contener letras, numeros y guiones ('-').")
            return False
        return True

    def visitVariableExpr(self, ctx):
        var_name = ctx.getText()
        self.validate_identifier(var_name)

        # Buscar en SymbolTable (ultimo scope primero)
        for scope in reversed(SymbolTable):
            if var_name in scope:
                return scope[var_name]

        # Si no esta en SymbolTable, buscar en FunctionTable
        if var_name in FunctionTable:
            # Retorna el nombre como referencia de la funcion
            return var_name

        raise Exception(f"Error: Variable o funcion '{var_name}' no definida.")

    # ---------------------------
    #       Let
    # ---------------------------
    def visitLetExpr(self, ctx):
        local_scope = {}
        for binding in ctx.letBinding():
            var_name = binding.ID().getText()
            value = self.visit(binding.expr())
            local_scope[var_name] = value

        SymbolTable.append(local_scope)
        result = 0
        for expr in ctx.expr():
            temp = self.visit(expr)
            if temp is not None:
                result = temp
        SymbolTable.pop()
        return result

    # ---------------------------
    #   Expresiones de E/S
    # ---------------------------
    def visitDisplayExpr(self, ctx):
        value = self.visit(ctx.expr())
        if value is None:
            value = "None"
        if isinstance(value, list):
            value = '(' + ' '.join(map(str, value)) + ')'
        print(value, end="", flush=True)
        return value

    def visitWriteExpr(self, ctx):
        value = self.visit(ctx.expr())
        if value is None:
            value = "None"
        if isinstance(value, list):
            value = '(' + ' '.join(map(str, value)) + ')'
        elif isinstance(value, str):
            # Imprimir con comillas
            value = f'"{value}"'
        print(value, end="", flush=True)
        return value

    def visitReadExpr(self, ctx):
        try:
            value = sys.stdin.readline().strip()
            # Verificar si el valor es un booleano válido
            if value.lower() in ['#t', 'true']:
                return True
            elif value.lower() in ['#f', 'false']:
                return False
            # Verificar si el valor es un entero válido
            elif value.lstrip('-').isdigit():
                return int(value)
            else:
                raise ValueError("Entrada invalida: solo se aceptan enteros y booleanos.")
        except Exception as e:
            raise Exception(f"Error en 'read': {e}")



    def visitNewlineExpr(self, ctx):
        print()
        return None

    # ---------------------------
    #  Expresiones Basicas
    # ---------------------------
    def visitNumberExpr(self, ctx):
        return int(ctx.getText())

    def visitStringExpr(self, ctx):
        # Eliminar las comillas
        raw_string = ctx.getText()
        return raw_string[1:-1]

    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        operator = ctx.getChild(1).getText()
        return LogicDicc[operator](left, right)

    def visitGroupExpr(self, ctx):
        return self.visit(ctx.expr())

    # ---------------------------
    #      Listas
    # ---------------------------
    def visitListLiteralExpr(self, ctx):
        # Extraer elementos entre la comilla y los parentesis
        elements = ctx.getText()[2:-1].split()
        processed_elements = []
        for element in elements:
            try:
                processed_elements.append(int(element))
            except ValueError:
                processed_elements.append(element)
        return processed_elements

    def visitEmptyListExpr(self, ctx):
        return []

    def visitCarExpr(self, ctx):
        lst = self.visit(ctx.expr())
        if not isinstance(lst, list):
            raise Exception(f"Error: 'car' solo se puede usar con listas, recibido: {lst}")
        if len(lst) == 0:
            raise Exception("Error: 'car' no puede operar sobre una lista vacia.")
        return lst[0]

    def visitCdrExpr(self, ctx):
        lst = self.visit(ctx.expr())
        if not isinstance(lst, list):
            raise Exception(f"Error: 'cdr' solo se puede usar con listas, recibido: {lst}")
        if len(lst) == 0:
            raise Exception("Error: 'cdr' no puede operar sobre una lista vacia.")
        return lst[1:]

    def visitNullExpr(self, ctx):
        lst = self.visit(ctx.expr())
        if not isinstance(lst, list):
            raise Exception(f"Error: 'null?' solo se puede usar con listas, recibido: {lst}")
        return len(lst) == 0

    def visitConsExpr(self, ctx):
        element = self.visit(ctx.expr(0))
        lst = self.visit(ctx.expr(1))
        if not isinstance(lst, list):
            raise Exception(f"Error: 'cons' requiere una lista como segundo argumento, recibido: {lst}")
        return [element] + lst
    def visitLengthExpr(self, ctx):
        lst = self.visit(ctx.expr())
        if not isinstance(lst, list):
            raise Exception(f"Error: 'length' solo se puede usar con listas, recibido: {lst}")
        return len(lst)
    
    def visitAppendExpr(self, ctx):
        lst1 = self.visit(ctx.expr(0))
        lst2 = self.visit(ctx.expr(1))
        if not isinstance(lst1, list) or not isinstance(lst2, list):
            raise Exception(f"Error: 'append' requiere listas como argumentos, recibido: {lst1}, {lst2}")
        return lst1 + lst2

    
    
    # ---------------------------
    #  Operaciones  avanzadas con cadenas 
    # ---------------------------
    def visitStringAppendExpr(self, ctx):
        strings = [self.visit(expr) for expr in ctx.expr()]
        if not all(isinstance(s, str) for s in strings):
            raise Exception(f"Error: 'string-append' requiere solo cadenas, recibido: {strings}")
        return ''.join(strings)
    def visitStringLengthExpr(self, ctx):
        string = self.visit(ctx.expr())
        if not isinstance(string, str):
            raise Exception(f"Error: 'string-length' requiere una cadena, recibido: {string}")
        return len(string)
    def visitStringEqualsExpr(self, ctx):
        str1 = self.visit(ctx.expr(0))
        str2 = self.visit(ctx.expr(1))
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise Exception(f"Error: 'string=?' requiere cadenas como argumentos, recibido: {str1}, {str2}")
        return '#t' if str1 == str2 else '#f'


    # ---------------------------
    #  Llamada a funciones
    # ---------------------------
    
    def visitFunctionCallExpr(self, ctx):
        func_name = ctx.ID().getText()
        self.validate_identifier(func_name)

        # Revisar si la funcion esta como simbolo en algun scope
        for scope in reversed(SymbolTable):
            if func_name in scope:
                func_name = scope[func_name]
                break

        if func_name not in FunctionTable:
            raise Exception(f"Error: Funcion '{func_name}' no definida.")

        params, block = FunctionTable[func_name]
        args = [self.visit(arg) for arg in ctx.expr()]

        if len(args) != len(params):
            raise Exception(f"Error: La funcion '{func_name}' esperaba {len(params)} argumentos, pero recibio {len(args)}.")

        local_scope = dict(zip(params, args))
        SymbolTable.append(local_scope)
        result = self.visit(block)
        SymbolTable.pop()
        return result
