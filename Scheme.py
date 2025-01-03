import sys

from antlr4 import *
from SchemeLexer import SchemeLexer
from SchemeParser import SchemeParser
from EvalVisitor import EvalVisitor, Function_Table, Symbol_Table


# Lista global para almacenar resultados
Results = []

# Procesar la entrada Scheme
def processInput(input_text):
    try:
        # Paso 1: Crear flujo de entrada y lexer
        input_stream = InputStream(input_text)
        lexer = SchemeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)

        # Paso 2: Crear parser y arbol AST
        parser = SchemeParser(token_stream)
        tree = parser.root()

        # Paso 3: Crear visitador para evaluar el arbol
        visitor = EvalVisitor()
        result = visitor.visit(tree)

        # Si existe la funcion 'main', ejecutarla
        if 'main' in Function_Table:
            main_params, main_block = Function_Table['main']
            Symbol_Table.append({})  # Introducimos un nuevo scope vacio
            result = visitor.visit(main_block)  # Ejecutar el bloque principal
            Symbol_Table.pop()       # Limpiamos el scope local

        # Manejo de resultados
        if isinstance(result, int):
            if len(Results) > 8:
                Results.pop(0)
        elif isinstance(result, list):
            # Si es una lista, se almacena directamente en Results
            Results.append(str(result))
            if len(Results) > 8:
                Results.pop(0)

    except Exception as e:
        # Manejo de errores
        Results.append(f"{str(e)}")
        if len(Results) > 8:
            Results.pop(0)

    return Results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 Scheme.py <archivo_entrada.scm>")
        sys.exit(1)

    inputFile = sys.argv[1]
    try:
        with open(inputFile, "r") as file:
            input_text = file.read()

        # Procesar la entrada y mostrar resultados
        output = processInput(input_text)
        if output:  
            print(*output, sep="")

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{inputFile}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        sys.exit(1)
