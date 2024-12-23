from antlr4 import *
from SchemeLexer import SchemeLexer
from SchemeParser import SchemeParser
from EvalVisitor import EvalVisitor, FunctionTable, SymbolTable
import sys

# Listas globales para almacenar resultados y funciones
functions = []
results = []

# Función auxiliar para formatear funciones
def getFunx(tokens):
    return " ".join(map(str, tokens))

# Procesar la entrada Scheme
def process_input(input_text):
    try:
        print("DEBUG: Iniciando procesamiento de entrada...")
        print("DEBUG: Texto de entrada recibido:")

        # Lexer, Parser y árbol de sintaxis
        input_stream = InputStream(input_text)
        lexer = SchemeLexer(input_stream)
        print("DEBUG: Lexer inicializado.")

        token_stream = CommonTokenStream(lexer)
        print("DEBUG: TokenStream generado.")

        parser = SchemeParser(token_stream)
        print("DEBUG: Parser inicializado.")

        tree = parser.root()  # Construye el árbol AST
        print("DEBUG: Árbol AST generado:")
        print(tree.toStringTree(recog=parser))  # Imprime el árbol de análisis sintáctico

        # Visitador para evaluar el árbol
        visitor = EvalVisitor()
        print("DEBUG: Visitador inicializado.")
        result = visitor.visit(tree)
        print(f"DEBUG: Resultado de la evaluación inicial: {result}")

        # Ejecutar 'main' si está definida
        if 'main' in FunctionTable:
            print("DEBUG: Ejecutando función 'main'...")
            main_params, main_block = FunctionTable['main']
            print(f"DEBUG: Parámetros de 'main': {main_params}")
            print(f"DEBUG: Bloque de 'main': {main_block.getText()}")

            SymbolTable.append({})  # Añadimos un nuevo scope vacío
            result = visitor.visit(main_block)  # Ejecutar el bloque principal
            SymbolTable.pop()       # Limpiamos el scope local

            print(f"DEBUG: Resultado de 'main': {result}")
        else:
            print("DEBUG: No se encontró la función 'main'.")

        # Gestión de resultados
        if isinstance(result, int):
            output = f"IN: {input_text.strip()} /// OUT: {result}"
            results.append(output)
            print(f"DEBUG: Resultado añadido a 'results': {output}")
            if len(results) > 8:
                results.pop(0)

        elif isinstance(result, list):  # Si es una lista, probablemente funciones
            functions.append(getFunx(result))
            print(f"DEBUG: Función añadida a 'functions': {functions[-1]}")
            if len(functions) > 8:
                functions.pop(0)

    except Exception as e:
        output = f"IN: {input_text.strip()} /// OUT: Error: {str(e)}"
        results.append(output)
        print(f"DEBUG: Error capturado: {str(e)}")
        if len(results) > 8:
            results.pop(0)

    return results, functions

# Punto de entrada principal
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 Scheme.py <archivo_entrada.scm>")
        sys.exit(1)

    # Leer archivo de entrada
    input_file = sys.argv[1]
    try:
        print(f"DEBUG: Leyendo archivo '{input_file}'...")
        with open(input_file, "r") as file:
            input_text = file.read()

        # Procesar la entrada y mostrar resultados
        results, funcs = process_input(input_text)
        
        print("DEBUG: Procesamiento completado.")

        print("\nResultados:")
        print("\n".join(results))

        # Imprimir funciones definidas
        print("Funciones definidas:")
        for func, (params, _) in FunctionTable.items():
            print(f"{func} ({', '.join(params)})")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        sys.exit(1)
