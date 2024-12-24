from SchemeParser import SchemeParser
from SchemeVisitor import SchemeVisitor
from antlr4.tree.Tree import TerminalNodeImpl

import sys

# Tabla de funciones y símbolos globales
FunctionTable = {}  # Almacena funciones (nombre y parámetros)
SymbolTable = [{}]  # Pila de scopes de variables

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
    '<': lambda a, b: a < b, 
    '<=': lambda a, b: a <= b, 
    '>': lambda a, b: a > b, 
    '>=': lambda a, b: a >= b, 
    '<>': lambda a, b: a != b, 
    '=': lambda x, y: x == y, 
    'and': lambda a, b: a and b, 
    'or': lambda a, b: a or b,
    'not': lambda a: not a  
}


class EvalVisitor(SchemeVisitor):
    
    def visit(self, ctx):
        """
        Visitador genérico con depuración.
        """
        # print(f"DEBUG: Visitando nodo: {type(ctx).__name__}, texto: {ctx.getText()}")
        result = super().visit(ctx)  # Llama al visitador correspondiente
        # print(f"DEBUG: Nodo {type(ctx).__name__} evaluado con resultado: {result}")
        return result


    def visitRoot(self, ctx):
        # print("DEBUG: visitRoot - Start")
        result = 0
        for child in ctx.getChildren():
            # print(f"DEBUG: visitRoot - Visiting child: {child.getText()}")
            result = self.visit(child) or result
        # print(f"DEBUG: visitRoot - End with result: {result}")
        return result

    def visitArithmeticExpr(self, ctx):
        operator = ctx.getChild(1).getText()
        left = self.visit(ctx.getChild(2))
        right = self.visit(ctx.getChild(3))
        # print(f"DEBUG: visitArithmeticExpr - Operator: {operator}, Left: {left}, Right: {right}")
        result = ArithmeticDicc[operator](left, right)
        # print(f"DEBUG: visitArithmeticExpr - Result: {result}")
        return result
    def visitLogicalExpr(self, ctx):
        """
        Evalúa expresiones lógicas como (and ...), (or ...), (not ...).
        """
        operator = ctx.getChild(1).getText()

        # Intentar evaluar los argumentos booleanos
        try:
            args = [self.visit(expr) for expr in ctx.expr()]
        except Exception as e:
            raise Exception(f"Error en la evaluación de argumentos para '{operator}': {e}")

        # Verificar si no hay argumentos
        if not args:
            raise Exception(f"Error: Ninguna condición válida para el operador lógico '{operator}'.")

        # Validar el operador
        if operator not in LogicDicc:
            raise Exception(f"Error: Operador lógico '{operator}' no definido.")

        # Manejar caso especial para 'not'
        if operator == 'not':
            if len(args) != 1:
                raise Exception(f"Error: El operador 'not' espera un único argumento, pero recibió {len(args)}.")
            return '#t' if LogicDicc[operator](args[0]) else '#f'

        # Manejar 'and' y 'or' con exactamente dos argumentos
        if operator in ['and', 'or']:
            if len(args) != 2:
                raise Exception(f"Error: El operador '{operator}' espera exactamente dos argumentos, pero recibió {len(args)}.")
            return '#t' if LogicDicc[operator](args[0], args[1]) else '#f'

        # Para otros operadores lógicos
        raise Exception(f"Error: Operador lógico '{operator}' no soportado.")
    
    
    def visitIfExpr(self, ctx):
        """
        Maneja expresiones 'if'.
        """
        # print("DEBUG: visitIfExpr - Start")
        
        # Evaluar la condición
        condition = self.visit(ctx.expr(0))
        # print(f"DEBUG: visitIfExpr - Condition evaluated: {condition}")

        if condition:  # Si la condición es verdadera
            result = self.visit(ctx.expr(1))
            # print(f"DEBUG: visitIfExpr - True branch result: {result}")
        else:  # Si la condición es falsa
            result = self.visit(ctx.expr(2))
            # print(f"DEBUG: visitIfExpr - False branch result: {result}")

        # print("DEBUG: visitIfExpr - End")
        return result
    
    def visitCondExpr(self, ctx):
        """
        Evalúa una expresión 'cond', manejando cláusulas normales y la cláusula 'else'.
        """
        # print(f"DEBUG: visitCondExpr - Start, texto: {ctx.getText()}")

        # Iterar sobre todas las cláusulas
        for clause in ctx.condClause():
            if isinstance(clause, SchemeParser.CondClauseExprContext):  # Cláusula normal
                condition = self.visit(clause.expr(0))  # Primera expresión como condición
                # print(f"DEBUG: visitCondExpr - Evaluando condición: {condition}")

                if condition:  # Si la condición es verdadera
                    result = self.visit(clause.expr(1))  # Evaluar y devolver el resultado
                    # print(f"DEBUG: visitCondExpr - Resultado: {result}")
                    return result

            if isinstance(clause, SchemeParser.CondElseClauseContext):  # Cláusula 'else'
                result = self.visit(clause.expr())  # Evaluar y devolver el resultado
                # print(f"DEBUG: visitCondExpr - Else resultado: {result}")
                return result

        # Si ninguna cláusula es válida (teóricamente imposible con un cond correcto)
        # print("DEBUG: visitCondExpr - Ninguna cláusula válida encontrada.")
        return None



    def validate_identifier(self, identifier):
        import re
        # Regex que permite solo letras, números y guiones, comenzando con una letra
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9-]*$", identifier):
            print(f"ERROR: Identificador inválido '{identifier}'. "
                "Un identificador debe comenzar con una letra y solo puede contener letras, números y guiones ('-').")
            return False  # Identificador inválido
        return True  # Identificador válido


    def visitFunctionCallExpr(self, ctx):
        func_name = ctx.ID().getText()
        self.validate_identifier(func_name)
        # print(f"DEBUG: visitFunctionCallExpr - Llamando función: {func_name}")

        # Buscar en SymbolTable para funciones pasadas como argumentos
        for scope in reversed(SymbolTable):
            if func_name in scope:
                func_name = scope[func_name]  # Resolver referencia
                break

        if func_name not in FunctionTable:
            raise Exception(f"Error: Función '{func_name}' no definida.")

        # Obtener parámetros y bloque
        params, block = FunctionTable[func_name]

        # Evaluar argumentos
        args = [self.visit(arg) for arg in ctx.expr()]
        # print(f"DEBUG: visitFunctionCallExpr - Params: {params}, Args: {args}")

        if len(args) != len(params):
            raise Exception(f"Error: La función '{func_name}' esperaba {len(params)} argumentos, pero recibió {len(args)}.")

        # Crear un nuevo scope para los argumentos
        local_scope = dict(zip(params, args))
        SymbolTable.append(local_scope)
        # print(f"DEBUG: visitFunctionCallExpr - SymbolTable después de añadir scope: {SymbolTable}")

        # Evaluar el bloque de la función
        result = self.visit(block)
        SymbolTable.pop()
        # print(f"DEBUG: visitFunctionCallExpr - Resultado: {result}, SymbolTable después de limpiar scope: {SymbolTable}")
        return result


    def visitConstantDeclaration(self, ctx):
        constant_name = ctx.ID().getText()  # Nombre de la constante
        # print(f"DEBUG: visitConstantDeclaration - Definiendo constante: {constant_name}")
        
        # Comprobar si ya existe
        if any(constant_name in scope for scope in SymbolTable):
            raise Exception(f"Error: La constante '{constant_name}' ya está definida.")
        
        # Evaluar el valor de la constante
        value = self.visit(ctx.expr())
        # print(f"DEBUG: visitConstantDeclaration - Valor evaluado: {value}")
        
        # Añadir al scope global
        SymbolTable[0][constant_name] = value
        # print(f"DEBUG: visitConstantDeclaration - SymbolTable actualizada: {SymbolTable}")
        
        return constant_name


    def visitLetExpr(self, ctx):
        # print("DEBUG: visitLetExpr - Start")
        local_scope = {}
        for binding in ctx.letBinding():
            var_name = binding.ID().getText()
            value = self.visit(binding.expr())
            local_scope[var_name] = value
            # print(f"DEBUG: visitLetExpr - Binding: {var_name} = {value}")
        SymbolTable.append(local_scope)
        # print(f"DEBUG: visitLetExpr - SymbolTable after push: {SymbolTable}")
        result = 0
        for expr in ctx.expr():
            result = self.visit(expr) or result
        SymbolTable.pop()
        # print(f"DEBUG: visitLetExpr - Result: {result}, SymbolTable after pop: {SymbolTable}")
        return result


    def visitDisplayExpr(self, ctx):
        """
        Imprime el resultado de la expresión evaluada en el display.
        """
        # print(f"DEBUG: visitDisplayExpr - Start, texto: {ctx.getText()}")
        value = self.visit(ctx.expr())  # Evaluar el hijo
        if value is None:
            value = "None"  # Evitar impresión vacía
        if isinstance(value, list):
         value = '(' + ' '.join(map(str, value)) + ')'
        # print(f"DEBUG: visitDisplayExpr - Valor evaluado: {value}")
        print(value, end="", flush=True)  # Imprimir sin salto de línea y vaciar el búfer
        # print(f"DEBUG: visitDisplayExpr - End")
        return value
    
    def visitWriteExpr(self, ctx):
        """
        Imprime el resultado de la expresión evaluada en el nodo 'writeExpr',
        asegurándose de mantener las comillas visibles si es una cadena.
        """
        # Evaluar el hijo del nodo 'writeExpr'
        value = self.visit(ctx.expr())

        # Si el valor es None, se maneja explícitamente
        if value is None:
            value = "None"

        # Si el valor es una lista, se convierte a la notación de lista de Scheme
        if isinstance(value, list):
            value = '(' + ' '.join(map(str, value)) + ')'

        # Si el valor es una cadena, se imprime tal cual, incluyendo las comillas
        elif isinstance(value, str):
            value = f'"{value}"'  # Asegura que las comillas visibles se impriman

        # Imprimir el valor en la salida estándar
        print(value, end="", flush=True)

        # Retornar el valor evaluado (opcional)
        return value


    def visitReadExpr(self, ctx):
        # print("DEBUG: visitReadExpr - Waiting for input...")
        try:
            value = sys.stdin.readline().strip()
            # print(f"DEBUG: visitReadExpr - Value read: {value}")
            return int(value)
        except ValueError:
            raise Exception("Error: Invalid input for 'read'.")

    def visitNewlineExpr(self, ctx):
        # print("DEBUG: visitNewlineExpr - Printing newline")
        print()
        return None

    def visitNumberExpr(self, ctx):
        # print(f"DEBUG: visitNumberExpr - Number: {ctx.getText()}")
        return int(ctx.getText())
    
    def visitVariableExpr(self, ctx):
        var_name = ctx.getText()
        self.validate_identifier(var_name)
        # print(f"DEBUG: visitVariableExpr - Accediendo a variable: {var_name}")

        # Buscar en SymbolTable
        for scope in reversed(SymbolTable):
            if var_name in scope:
                # print(f"DEBUG: visitVariableExpr - Encontrada en SymbolTable: {var_name} = {scope[var_name]}")
                return scope[var_name]

        # Buscar en FunctionTable
        if var_name in FunctionTable:
            # print(f"DEBUG: visitVariableExpr - Encontrada en FunctionTable: {var_name}")
            return var_name  # Retorna el nombre como referencia de la función

        raise Exception(f"Error: Variable o función '{var_name}' no definida.")

  
  
    def visitDeclaration(self, ctx):
        """
        Procesa las declaraciones: constantes y funciones.
        """
        # print(f"DEBUG: visitDeclaration - Start, texto: {ctx.getText()}")

        if ctx.constantDeclaration():
            # Obtener el identificador de la constante
            constant_name = ctx.constantDeclaration().ID().getText()

            # Validar el identificador
            if not self.validate_identifier(constant_name):
                print(f"ERROR: No se pudo procesar la constante '{constant_name}' debido a un identificador inválido.")
                return None  # Abortamos el procesamiento de esta declaración

            # Procesar la declaración como constante
            result = self.visit(ctx.constantDeclaration())
            return result

        elif ctx.functionDeclaration():
            # Obtener el identificador de la función
            function_name = ctx.functionDeclaration().ID(0).getText()

            # Validar el identificador
            if not self.validate_identifier(function_name):
                print(f"ERROR: No se pudo procesar la función '{function_name}' debido a un identificador inválido.")
                return None  # Abortamos el procesamiento de esta declaración

            # Procesar la declaración como función
            result = self.visit(ctx.functionDeclaration())
            return result

        else:
            raise Exception("Error: Declaración desconocida.")


    def visitFunctionDeclaration(self, ctx):
        """
        Guarda la definición de una función en la tabla FunctionTable.
        """
        function_name = ctx.ID(0).getText()  # Nombre de la función
        params = [param.getText() for param in ctx.ID()[1:]]  # Parámetros de la función
        block = ctx.block()  # Captura el cuerpo de la función como un nodo completo
        
        # Guarda la función en FunctionTable
        FunctionTable[function_name] = (params, block)
        # print(f"DEBUG: visitFunctionDeclaration - Function '{function_name}' defined with params {params} and block {block.getText()}")
        return function_name


    def visitBlock(self, ctx):
        # print("DEBUG: visitBlock - Start")
        result = 0
        for stmt in ctx.stmt():
            temp = self.visit(stmt)
            # print(f"DEBUG: visitBlock - Visiting stmt, result: {temp}")
            if temp is not None:
                result = temp
        # print(f"DEBUG: visitBlock - End with result: {result}")
        return result
    
    def visitStringExpr(self, ctx):
        """
        Maneja nodos StringExprContext.
        Devuelve el contenido de la cadena eliminando las comillas.
        """
        # Obtiene el texto completo del nodo, incluyendo las comillas
        raw_string = ctx.getText()
        # print(f"DEBUG: visitStringExpr - Raw string: {raw_string}")

        # Remueve las comillas del principio y final
        clean_string = raw_string[1:-1]  # Elimina las comillas
        # print(f"DEBUG: visitStringExpr - Cleaned string: {clean_string}")

        return clean_string
    def visitComparisonExpr(self, ctx):
        """
        Evalúa comparaciones (>, <, >=, <=, etc.).
        """
        # print(f"DEBUG: visitComparisonExpr - Start, texto: {ctx.getText()}")

        left = self.visit(ctx.expr(0))  # Lado izquierdo
        right = self.visit(ctx.expr(1))  # Lado derecho
        operator = ctx.getChild(1).getText()  # Operador de comparación

        # print(f"DEBUG: visitComparisonExpr - Left: {left}, Right: {right}, Operator: {operator}")

        # Realizar la comparación
        result = LogicDicc[operator](left, right)
        # print(f"DEBUG: visitComparisonExpr - Result: {result}")
        # print(f"DEBUG: visitComparisonExpr - End")
        return result
    def visitGroupExpr(self, ctx):
        """
        Evalúa un GroupExpr devolviendo el resultado de su contenido.
        """
        # print(f"DEBUG: visitGroupExpr - Start, texto: {ctx.getText()}")
        result = self.visit(ctx.expr())  # Evaluar el hijo
        # print(f"DEBUG: visitGroupExpr - Result: {result}")
        # print(f"DEBUG: visitGroupExpr - End")
        return result


    def visitListLiteralExpr(self, ctx):
        """
        Convierte el literal de lista Scheme en una lista Python.
        """
        # print(f"DEBUG: visitListLiteralExpr - Start, texto: {ctx.getText()}")
        
        # Extraer el texto de los elementos de la lista
        elements = ctx.getText()[2:-1].split()  # Quita la comilla inicial y los paréntesis
        processed_elements = []

        for element in elements:
            try:
                # Intenta convertir a número
                processed_elements.append(int(element))
            except ValueError:
                # Si no es un número, lo trata como una cadena o un identificador
                processed_elements.append(element)

        # print(f"DEBUG: visitListLiteralExpr - Elementos procesados: {processed_elements}")
        return processed_elements
    
    def visitEmptyListExpr(self, ctx):
        """
        Maneja un nodo EMPTY_LIST y lo convierte en una lista vacía de Python.
        """
        # print(f"DEBUG: visitEmptyListExpr - Start, texto: {ctx.getText()}")
        result = []  # Representación de una lista vacía en Python
        # print(f"DEBUG: visitEmptyListExpr - Resultado: {result}")
        return result

    def visitCarExpr(self, ctx):
        # print(f"DEBUG: visitCarExpr - Start, texto: {ctx.getText()}")
        lst = self.visit(ctx.expr())
        # print(f"DEBUG: visitCarExpr - Lista evaluada: {lst}")
        if not isinstance(lst, list):
            raise Exception(f"Error: 'car' solo se puede usar con listas, recibido: {lst}")
        if len(lst) == 0:
            raise Exception("Error: 'car' no puede operar sobre una lista vacía.")
        result = lst[0]
        # print(f"DEBUG: visitCarExpr - Resultado: {result}")
        return result

    def visitCdrExpr(self, ctx):
        # print(f"DEBUG: visitCdrExpr - Start, texto: {ctx.getText()}")
        lst = self.visit(ctx.expr())
        # print(f"DEBUG: visitCdrExpr - Lista evaluada: {lst}")
        if not isinstance(lst, list):
            raise Exception(f"Error: 'cdr' solo se puede usar con listas, recibido: {lst}")
        if len(lst) == 0:
            raise Exception("Error: 'cdr' no puede operar sobre una lista vacía.")
        result = lst[1:] 
        # print(f"DEBUG: visitCdrExpr - Resultado: {result}")
        return result

    def visitNullExpr(self, ctx):
        # print(f"DEBUG: visitNullExpr - Start, texto: {ctx.getText()}")
        lst = self.visit(ctx.expr())
        # print(f"DEBUG: visitNullExpr - Lista evaluada: {lst}")
        if not isinstance(lst, list):
            raise Exception(f"Error: 'null?' solo se puede usar con listas, recibido: {lst}")
        result = len(lst) == 0
        # print(f"DEBUG: visitNullExpr - Resultado: {result}")
        return result

    def visitConsExpr(self, ctx):
        # print(f"DEBUG: visitConsExpr - Start, texto: {ctx.getText()}")
        element = self.visit(ctx.expr(0))  # Primer argumento
        # print(f"DEBUG: visitConsExpr - Elemento: {element}")
        lst = self.visit(ctx.expr(1))      # Segundo argumento
        # print(f"DEBUG: visitConsExpr - Lista evaluada: {lst}")
        if not isinstance(lst, list):
            raise Exception(f"Error: 'cons' requiere una lista como segundo argumento, recibido: {lst}")
        result = [element] + lst
        # print(f"DEBUG: visitConsExpr - Resultado: {result}")
        return result

 