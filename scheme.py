import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from antlr4.error.ErrorListener import ErrorListener

class SchemeErrorListener(ErrorListener):
    def __init__(self):
        super(SchemeErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error sintáctico en la línea {line}, columna {column}: {msg}")
        sys.exit(1)

class SchemeInterpreter(ExprVisitor):
    def __init__(self):
        self.global_env = {}

    def visitRoot(self, ctx):
        return self.visitChildren(ctx)

    def visitFuncion(self, ctx):
        func_name = str(ctx.VAR())
        params = [str(var) for var in ctx.VAR()[1:]]
        body = ctx.expr()
        self.global_env[func_name] = (params, body)
        return func_name

    def visitConstante(self, ctx):
        const_name = str(ctx.VAR())
        value = self.visit(ctx.expr())
        self.global_env[const_name] = value
        return const_name

    def visitExpr(self, ctx):
        if ctx.operacion_aritmetica():
            return self.visitOperacion_aritmetica(ctx)
        elif ctx.operacion_relacional():
            return self.visitOperacion_relacional(ctx)
        elif ctx.entrada():
            return self.visitEntrada(ctx)
        elif ctx.VAR():
            return self.global_env.get(str(ctx.VAR()))
        elif ctx.NUM():
            return int(str(ctx.NUM()))
        elif ctx.BOOLEAN():
            return str(ctx.BOOLEAN()) == '#t'
        else:
            return self.visitChildren(ctx)

    def visitOperacion_aritmetica(self, ctx):
        op = str(ctx.operacion_aritmetica().getText())
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right

    def visitOperacion_relacional(self, ctx):
        op = str(ctx.operacion_relacional().getText())
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '>=':
            return left >= right
        elif op == '<=':
            return left <= right
        elif op == '=':
            return left == right
        elif op == '<>':
            return left != right

    def visitEntrada(self, ctx):
        return int(input())

# Manejo de entrada y salida
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    parser.addErrorListener(SchemeErrorListener())
    tree = parser.root()
    interpreter = SchemeInterpreter()
    interpreter.visit(tree)

if __name__ == "__main__":
    main(sys.argv)
