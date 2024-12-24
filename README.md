# Scheme Compiler

Este documento describe el funcionamiento y las caracteristicas del **intérprete de Scheme** desarrollado en Python usando ANTLR4. A continuacion se detallan las funcionalidades soportadas, la estructura del proyecto, la forma de uso y la manera de ejecutar las pruebas incluidas.

---

## **Caracteristicas Generales**

Este interprete procesa y evalua programas escritos en Scheme. Algunas de las caracteristicas mas relevantes son:

1. **Soporte para Expresiones Basicas**  
   - Operaciones aritmeticas: `+`, `-`, `*`, `/`, `mod`, `^`  
   - Comparaciones: `<`, `<=`, `>`, `>=`, `=`, `<>`  
   - Operadores logicos: `and`, `or`, `not`  

2. **Control de Flujo**  
   - Expresiones condicionales con `if`  
   - Bloques `cond` con clausulas normales y `else`  

3. **Manejo de Listas**  
   - Operaciones `car`, `cdr`, `cons`, `null?`  
   - Literal de listas: `'(1 2 3)`  
   - Lista vacia: `'( )`  
   - **Nuevas funciones**: `length`, `append`  

4. **Manejo de Cadenas**  
   - `string-append` para concatenar multiples cadenas  
   - `string-length` para obtener la longitud de una cadena  
   - `string=?` para comparar la igualdad entre dos cadenas  

5. **Definiciones de Variables y Funciones**  
   - Definicion de constantes con `(define <id> <expr>)`  
   - Definicion de funciones con `(define (nombre param1 param2 ...) (cuerpo))`  
   - Soporte para ambitos anidados mediante una pila de `SymbolTable`  

6. **Entrada/Salida**  
   - `read` para leer un entero desde la entrada estandar  
   - `display` para imprimir un valor sin salto de linea  
   - `write` para imprimir un valor, manteniendo comillas de cadenas y formato en listas  
   - `newline` para imprimir un salto de linea  

7. **Estructura de `let`**  
   - Bloques locales de vinculos `(let ((var1 expr1) (var2 expr2) ...) <expr1> <expr2> ...)`  

---

## **Estructura del Proyecto**

### **Archivos Principales**

1. **`Scheme.g4`**  
   - Contiene la gramatica en ANTLR4 que describe la estructura sintactica del lenguaje Scheme manejado por este proyecto.  
   - Se incluyen nuevas reglas para funciones como `length`, `append`, `string-append`, `string-length` y `string=?`.  

2. **`SchemeLexer.py` y `SchemeParser.py`**  
   - Generados automaticamente por ANTLR4 a partir de la gramatica `Scheme.g4`.  

3. **`EvalVisitor.py`**  
   - Implementa la logica de evaluacion de las expresiones y nodos del AST (Abstract Syntax Tree).  
   - Contiene los metodos de visita para cada tipo de nodo (expresiones aritmeticas, condicionales, manejo de listas, cadenas, etc.).  

4. **`Scheme.py`**  
   - Punto de entrada principal para procesar programas Scheme.  
   - Define la funcion `processInput()` para leer el archivo fuente Scheme, construir el arbol sintactico y delegar su evaluacion a `EvalVisitor`.  

5. **`Makefile`**  
   - Facilita la generacion del lexer y parser con `antlr4`, la instalacion de la runtime para Python y la ejecucion de las pruebas.  
   - Incluye la regla `test` que procesa varios archivos de la carpeta `Juegos-prueba` y compara la salida obtenida con la salida esperada (.out).  

6. **Carpeta `Juegos-prueba`**  
   - Contiene programas de prueba (`.scm`) y archivos de salida esperada (`.out`). Tambien puede contener entradas (`.inp`) para pruebas que requieren entrada del usuario.  
   - Ejemplos: `suma.scm`, `cond.scm`, `errores1.scm`, etc.  

---

## **Gramatica Resumida (Scheme.g4)**

Dentro de `Scheme.g4`, se definen las reglas principales para reconocer el lenguaje Scheme simplificado. Algunas producciones relevantes:

- **Expresiones**:
  ```antlr
  expr
    : '(' expr ')'                             #groupExpr
    | ID                                       #variableExpr
    | NUM                                      #numberExpr
    | STRING                                   #stringExpr
    | '#t'                                     #trueExpr
    | '#f'                                     #falseExpr
    | '(' (SUM | SUB | PROD | DIV | MOD | EXP) expr expr ')' #arithmeticExpr
    | '(' 'if' expr expr expr ')'              #ifExpr
    | '(' 'cond' condClause+ ')'               #condExpr
    | '(' 'let' '(' letBinding (letBinding)* ')' expr+ ')'   #letExpr
    | '(' 'read' ')'                           #readExpr
    | '(' 'display' expr ')'                   #displayExpr
    | '(' 'write' expr ')'                     #writeExpr
    | '(' 'newline' ')'                        #newlineExpr
    | '(' (LESS | LESSEQ | GREATER | GREATEREQ | EQ | NOTEQ) expr expr ')' #comparisonExpr
    | '(' (AND | OR | NOT) expr+ ')'           #logicalExpr
    | '(' 'car' expr ')'                       #carExpr
    | '(' 'cdr' expr ')'                       #cdrExpr
    | '(' 'cons' expr expr ')'                 #consExpr
    | '(' 'null?' expr ')'                     #nullExpr
    | '(' 'length' expr ')'                    #lengthExpr
    | '(' 'append' expr expr ')'               #appendExpr
    | '(' 'string-append' expr+ ')'            #stringAppendExpr
    | '(' 'string-length' expr ')'             #stringLengthExpr
    | '(' 'string=?' expr expr ')'             #stringEqualsExpr
    | ID expr*                                 #functionCallExpr
    | LIST                                     #listLiteralExpr
    | EMPTY_LIST                               #emptyListExpr
    ;
  ```

- **Declaraciones**:
  ```antlr
  declaration
    : '(' 'define' ID expr ')'                 #constantDeclaration
    | '(' 'define' '(' ID ID* ')' block ')'    #functionDeclaration
    ;
  ```

- **Bloques y Sentencias**:
  ```antlr
  block
    : stmt*
    ;

  stmt
    : expr                                      #expressionStmt
    | '(' 'define' ID expr ')'                  #assignmentStmt
    | '(' 'if' expr block ')'                   #ifStmt
    | '(' 'if' expr block 'else' block ')'      #ifElseStmt
    ;
  ```

- **Operadores**:
  ```antlr
  SUM       : '+';
  SUB       : '-';
  PROD      : '*';
  DIV       : '/';
  MOD       : 'mod';
  EXP       : '^';
  NOTEQ     : '<>';
  LESSEQ    : '<=';
  GREATEREQ : '>=';
  LESS      : '<';
  GREATER   : '>';
  EQ        : '=';
  AND       : 'and';
  OR        : 'or';
  NOT       : 'not';
  ```

---

## **Funciones Principales (EvalVisitor.py)**

El archivo `EvalVisitor.py` contiene la logica de evaluacion de cada nodo del arbol sintactico. Destacamos algunos metodos:

- **Listas**  
  - `visitCarExpr`, `visitCdrExpr`, `visitNullExpr`: Acceso y verificacion de listas.  
  - `visitLengthExpr`: Nuevo metodo que calcula el tamano de una lista.  
  - `visitAppendExpr`: Concatena dos listas.  

- **Cadenas**  
  - `visitStringAppendExpr`: Concatena multiples cadenas (equivalente a `string-append`).  
  - `visitStringLengthExpr`: Devuelve la longitud de una cadena.  
  - `visitStringEqualsExpr`: Compara dos cadenas, devolviendo `#t` o `#f`.  

- **Declaraciones y Ambitos**  
  - `visitConstantDeclaration`: Define variables en el scope global.  
  - `visitFunctionDeclaration`: Almacena la definicion de funciones (nombre, parametros y bloque).  
  - `visitFunctionCallExpr`: Evalua la llamada a una funcion, creando un nuevo scope local para los parametros.  

- **Expresiones de Control**  
  - `visitIfExpr`: Maneja expresiones `(if <cond> <exprSi> <exprNo>)`.  
  - `visitCondExpr`: Itera por las clausulas condicionales `(cond ...)`.  

- **Operaciones Aritmeticas y Logicas**  
  - `ArithmeticDicc`: Diccionario para `+`, `-`, `*`, `/`, `mod`, `^`.  
  - `LogicDicc`: Diccionario para `<`, `<=`, `>`, `>=`, `<>`, `=`, `and`, `or`, `not`.  

---

## **Uso del Intérprete**

### **Requisitos**

- Python 3.x  
- ANTLR4 (se instala automaticamente con la regla `make build` o manualmente `pip install antlr4-python3-runtime`).  

### **Compilar y Ejecutar**  

1. **Generar el lexer y parser**  
   ```bash
   make aux
   ```
   Esto ejecuta `java -jar antlr-4.13.2-complete.jar` para generar los archivos `SchemeLexer.py`, `SchemeParser.py` y `SchemeVisitor.py` basados en `Scheme.g4`.

2. **Construir el proyecto**  
   ```bash
   make build
   ```
   Esto instala la dependencia `antlr4-python3-runtime`.

3. **Ejecutar un programa Scheme**  
   ```bash
   make run
   ```
   Por defecto, intenta ejecutar `programa.scm`. Si quieres ejecutar otro archivo, puedes modificar la regla o directamente invocar:
   ```bash
   python3 Scheme.py ruta/a/tu_programa.scm
   ```

4. **Ejecutar las pruebas**  
   ```bash
   make test
   ```
   - Esta regla compila la gramatica, luego ejecuta cada uno de los archivos de prueba en la carpeta `Juegos-prueba`, comparando las salidas generadas con las salidas esperadas `.out`.  
   - En caso de existir diferencias, se mostrara un mensaje de error indicando la prueba que ha fallado.  

---

## **Ejemplos de Prueba**

A continuacion algunos ejemplos cortos de uso:

1. **Operaciones Basicas**  
   ```scheme
   (display (+ 3 5))         ; Esperado: 8
   (newline)
   (display (mod 10 3))      ; Esperado: 1
   (newline)
   (display (if (> 5 2) 10 20)) ; Esperado: 10
   (newline)
   ```

2. **Listas y sus Nuevas Funciones**  
   ```scheme
   (display (length '(1 2 3 4))) ; Esperado: 4
   (newline)

   (display (append '(1 2) '(3 4))) ; Esperado: (1 2 3 4)
   (newline)
   ```

3. **Cadenas**  
   ```scheme
   (display (string-append "Hola, " "Mundo" "!"))  ; Esperado: Hola, Mundo!
   (newline)

   (display (string-length "Hola"))     ; Esperado: 4
   (newline)

   (display (string=? "abc" "abc"))     ; Esperado: #t
   (newline)
   (display (string=? "abc" "def"))     ; Esperado: #f
   (newline)
   ```

4. **Funciones Definidas por el Usuario**  
   ```scheme
   (define (suma a b)
     (+ a b))

   (display (suma 5 7)) ; Esperado: 12
   (newline)
   ```

5. **Uso de Let**  
   ```scheme
   (let ((x 3)
         (y 4))
     (display (* x y))) ; Esperado: 12
   (newline)
   ```

---

## **Ejecucion de Pruebas (Makefile)**

El archivo `Makefile` incluye la regla `test`, que ejecuta una bateria de pruebas:

- **Pruebas simples**:  
  - `suma.scm`, `recursiva.scm`, `cond.scm`, `let.scm`, `map.scm`, `entrada.scm`
- **Pruebas complejas**:  
  - `prueba_orden_superior.scm`, `prueba_recursiva.scm`, `main.scm`, `extra.scm`
- **Pruebas de errores**:  
  - `errores1.scm`, `errores2.scm`, ..., `errores8.scm`

Cada prueba `<archivo>.scm` genera una salida `<archivo>_test.out`. Luego se compara con `<archivo>.out`. Si coinciden, se indica que la prueba fue completada correctamente; de lo contrario, se muestra un error.

Para correr estas pruebas en bloque:
```bash
make test
```
Si todas las pruebas coinciden, se mostrara un mensaje de confirmacion para cada una.

---

## **Limitaciones y Mejoras Futuras**

1. **Soporte adicional de macros**  
   - Expandiendo la gramatica para permitir definiciones de macros y su expansion en tiempo de compilacion.  

2. **Funciones Lambda**  
   - Permitir la definicion de funciones anonimas (`(lambda (x) <cuerpo>)`).  

3. **Mejoras en el Sistema de Tipos**  
   - Validaciones mas robustas para detectar mezclas indebidas de tipos (p.ej., intentar hacer `+` con cadenas).  

4. **Soporte para mas Operaciones de Lista**  
   - `map`, `filter`, `fold`, entre otras.  

---

## **Contribuciones**

Las contribuciones son bienvenidas. Por favor, crea un **issue** o haz un **pull request** en el repositorio si deseas mejorar o corregir algo en este interprete.

**Contacto**:  
- Autor original: _Nombre del autor_  
- Mantenedor actual: _Nombre del mantenedor_  

¡Gracias por utilizar este interprete de Scheme!