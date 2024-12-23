# Scheme Compiler

Este documento describe el funcionamiento y las características del compilador de Scheme desarrollado en Python usando ANTLR4.

---

## **Características Generales**

Este compilador procesa y evalúa programas escritos en Scheme. Entre sus características principales se encuentran:

1. **Soporte para Expresiones Básicas**:
   - Operaciones aritméticas: `+`, `-`, `*`, `/`, `mod`, `^`
   - Comparaciones: `<`, `<=`, `>`, `>=`, `=`, `!=`
   - Operadores lógicos: `&&`, `||`, `!`

2. **Control de Flujo**:
   - Expresiones condicionales: `if`, `cond`

3. **Manejo de Listas**:
   - Operaciones como `car`, `cdr`, `cons`, `null?`
   - Literales de listas en formato `(1 2 3)`

4. **Funciones de Orden Superior**:
   - `map`, `filter`

5. **Definiciones de Variables y Funciones**:
   - Variables globales con `define`
   - Funciones anidadas

6. **Entrada/Salida**:
   - Lectura con `read`
   - Impresión con `display`
   - Nueva línea con `newline`

---

## **Estructura del Proyecto**

### **Archivos Principales**

1. **`Scheme.g4`**
   - Contiene la gramática ANTLR4 para analizar el código Scheme.

2. **`SchemeLexer.py` y `SchemeParser.py`**
   - Generados automáticamente por ANTLR4.

3. **`EvalVisitor.py`**
   - Implementa la lógica de evaluación de las expresiones y nodos del AST.

4. **`Scheme.py`**
   - Punto de entrada principal para procesar programas Scheme.

5. **Carpeta `Juegos-prueba`**
   - Contiene programas de prueba y sus salidas esperadas.

### **Gramaticales Principales**

- **Expresiones**:
  ```
  expr
    : '(' expr ')'                           #groupExpr
    | ID                                     #variableExpr
    | NUM                                    #numberExpr
    | STRING                                 #stringExpr
    | '#t'                                   #trueExpr
    | '#f'                                   #falseExpr
    | '(' (SUM | SUB | PROD | DIV | MOD | EXP) expr expr ')' #arithmeticExpr
    | '(' 'if' expr expr expr ')'            #ifExpr
    | '(' 'cond' condClause+ ')'             #condExpr
    | '(' 'map' ID expr ')'                  #mapExpr
    | '(' 'filter' ID expr ')'               #filterExpr
    | ID expr*                               #functionCallExpr
    ```

- **Definiciones**:
  ```
  declaration
    : '(' 'define' '(' ID ID* ')' block ')'  #functionDeclaration
    | '(' 'define' ID expr ')'               #constantDeclaration
  ```

---

## **Funciones Principales**

### **`EvalVisitor.py`**

#### Métodos Clave

1. **`visitFunctionDeclaration`**
   - Define funciones globales y anidadas.

2. **`visitFunctionCallExpr`**
   - Evalúa llamadas a funciones, incluyendo el manejo de argumentos y ámbitos.

3. **`visitIfExpr`**
   - Evalúa estructuras condicionales `if`.

4. **`visitCondExpr`**
   - Evalúa bloques `cond`, comprobando cada condición en orden.

5. **`visitListLiteralExpr`**
   - Convierte literales de listas Scheme a listas de Python.

6. **`visitDisplayExpr`**
   - Imprime el resultado de una expresión en pantalla.

---

## **Instrucciones de Uso**

### **Compilar y Ejecutar**

1. Generar el Lexer y Parser:
   ```bash
   make aux
   ```

2. Construir el proyecto:
   ```bash
   make build
   ```

3. Ejecutar un programa Scheme:
   ```bash
   make run
   ```

4. Probar con casos predefinidos:
   ```bash
   make test
   make test2
   ```

---

## **Ejemplos de Prueba**

1. **Operaciones Básicas**:
   ```scheme
   (display (+ 3 5)) ; Esperado: 8
   (newline)
   (display (< 3 5)) ; Esperado: #t
   (newline)
   ```

2. **Definiciones y Condicionales**:
   ```scheme
   (define x 5)
   (display (if (> x 3) "Mayor" "Menor")) ; Esperado: Mayor
   (newline)
   ```

3. **Funciones y Recursión**:
   ```scheme
   (define (factorial n)
     (if (= n 0)
         1
         (* n (factorial (- n 1)))))

   (display (factorial 5)) ; Esperado: 120
   (newline)
   ```

4. **Map y Filter**:
   ```scheme
   (define (doblar x) (* x 2))
   (display (map doblar '(1 2 3 4))) ; Esperado: (2 4 6 8)
   (newline)

   (define (es-par x) (= (mod x 2) 0))
   (display (filter es-par '(1 2 3 4 5 6))) ; Esperado: (2 4 6)
   (newline)
   ```

---

## **Ejecución de Pruebas**

- Las pruebas se encuentran en las carpetas `Juegos-prueba` y `Juegos-prueba2`.
- Cada prueba tiene un archivo `.scm` con el programa Scheme y un archivo `.out` con la salida esperada.

Para ejecutar las pruebas:
```bash
make test
make test2
```

---

## **Limitaciones y Mejoras Futuras**

1. **Soporte para macros**:
   - Implementar macros para expandir la funcionalidad de Scheme.

2. **Funciones Lambda**:
   - Añadir soporte para funciones anónimas.

3. **Errores de Tipo**:
   - Mejorar la gestión de errores cuando se usan tipos incorrectos.

---

## **Contribuciones**

Cualquier contribución para mejorar el compilador es bienvenida. Por favor, crea un issue o realiza un pull request en el repositorio.

