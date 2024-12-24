# README del Proyecto Scheme

Este documento describe el funcionamiento, las características y las decisiones de diseño principales del **intérprete de Scheme** desarrollado en Python usando ANTLR4. Su objetivo es proporcionar una visión clara y completa para cualquier usuario o desarrollador que desee comprender cómo funciona, cómo utilizarlo y qué funcionalidades ofrece.

---

## 1. Introducción General

El proyecto implementa un **intérprete de Scheme** capaz de leer, analizar y ejecutar archivos `.scm`. La sintaxis y funcionalidad siguen los principios básicos del lenguaje Scheme, pero incluyen un conjunto de características adicionales, entre las que se destacan:

- **Operaciones aritméticas**: `+`, `-`, `*`, `/`, `mod`, `^`
- **Operadores lógicos**: `and`, `or`, `not` y comparaciones `<`, `<=`, `>`, `>=`, `=`, `<>`
- **Expresiones condicionales**: `if`, `cond`
- **Definición de variables y funciones** mediante `define`
- **Estructura de `let`** para crear ámbitos locales
- **Funciones de lista**: `car`, `cdr`, `cons`, `null?`, `length`, `append`
- **Funciones de cadena**: `string-append`, `string-length`, `string=?`
- **Entrada/Salida** con `read`, `display`, `write`, `newline`

De esta forma, el usuario puede escribir pequeños programas en Scheme y ejecutarlos en este intérprete con relativa facilidad.

---

## 2. Estructura y Archivos Principales

### 2.1 `Scheme.g4`
- **Gramática ANTLR4** que describe la sintaxis del lenguaje Scheme simplificado que maneja este proyecto.  
- Incluye reglas para expresiones, definición de funciones, sentencias condicionales, listas y manejo de cadenas.  
- Se añaden producciones para `length`, `append`, `string-append`, `string-length` y `string=?`.

### 2.2 `EvalVisitor.py`
- **Visitador** que recorre el Árbol de Sintaxis Abstracta (AST) generado por ANTLR4.  
- Ejecuta la lógica de cada nodo: expresiones aritméticas, llamadas a funciones, definiciones de variables, etc.  
- Maneja una **tabla de símbolos** (`SymbolTable`) y una **tabla de funciones** (`FunctionTable`) para la gestión de ámbitos y definiciones de funciones.  
- Contiene la implementación de funciones avanzadas de listas, cadenas, así como la semántica de `if`, `cond` y posibles errores de tipos o referencias inválidas.

### 2.3 `Scheme.py`
- **Punto de entrada principal** para ejecutar el intérprete.  
- Expone la función `processInput(input_text)`, que:
  1. Genera el lexer y el parser con ANTLR4.
  2. Construye el árbol sintáctico (AST) a partir del texto Scheme.
  3. Invoca al `EvalVisitor` para evaluar el AST.
  4. Si existe la función `main`, la ejecuta como punto inicial del programa Scheme.  
- Retorna resultados y/o errores en una lista global.

### 2.4 `Makefile`
- Automatiza tareas de **generación**, **construcción** y **pruebas**:
  - **`antlr`**: Genera `SchemeLexer.py`, `SchemeParser.py` y `SchemeVisitor.py` a partir de `Scheme.g4`.  
  - **`build`**: Instala la biblioteca `antlr4-python3-runtime`.  
  - **`run`**: Ejecuta `programa.scm` con este intérprete.  
  - **`test`**: Procesa diferentes casos de prueba en `Juegos-prueba`, comparando la salida generada con la salida esperada `.out`.  

---

## 3. Decisiones de Diseño

1. **Visitador (EvalVisitor)**  
   - Se emplea una clase `EvalVisitor` que sigue la estructura de visitador de ANTLR4. Cada tipo de nodo (expresión aritmética, condicional, let, etc.) se maneja en un método `visitXxx`.  
   - Esta modularización facilita la comprensión de la semántica de cada constructo.

2. **Gestión de ámbitos**  
   - Se utiliza una **pila de diccionarios** (`SymbolTable`) para las variables, y un **diccionario global** (`FunctionTable`) para funciones.  
   - Cada vez que se entra en una función o en un bloque `let`, se crea un nuevo diccionario en la pila para manejar el alcance local. Al finalizar, se elimina.

3. **Tratamiento de errores**  
   - Si se produce una operación inválida (por ejemplo, sumar una lista a un número) o se llama a una función no definida, se lanza una excepción.  
   - El sistema de pruebas incluye archivos `.scm` que ponen a prueba las situaciones de error, validando que se notifiquen adecuadamente.

4. **Extensiones de Scheme**  
   - Se agregan funciones típicas como `car`, `cdr`, `cons`, `null?` y se amplían con `append`, `string-append`, etc.  
   - La lectura (`read`) está actualmente limitada a enteros, con la posibilidad de extenderla a otros tipos en el futuro.

---

## 4. Instrucciones de Uso

### 4.1 Generar y Construir
```bash
make aux      # Genera SchemeLexer.py, SchemeParser.py y SchemeVisitor.py
make build    # Instala antlr4-python3-runtime
```

### 4.2 Ejecutar un Programa
```bash
make run
```
- Ejecuta `Scheme.py` con el archivo `programa.scm`.  
- Opcionalmente, se puede ejecutar directamente:
  ```bash
  python3 Scheme.py archivo.scm
  ```

### 4.3 Lanzar las Pruebas
```bash
make test
```
- Se compila la gramática y se ejecutan los archivos de prueba en `Juegos-prueba`.  
- Para cada archivo `<nombre>.scm`, se genera `<nombre>_test.out` y se compara con `<nombre>.out`.  
- Si hay diferencias, se informa el error; si coinciden, se indica que la prueba se completó correctamente.

---

## 5. Ejemplos de Uso

**Ejemplo 1: Operaciones básicas y condicionales**:
```scheme
(display (+ 3 5))        ; 8
(newline)
(display (if (> 10 2) 1 0)) ; 1
(newline)
```
Salida esperada:
```
8
1
```

**Ejemplo 2: Manejo de listas**:
```scheme
(display (length '(1 2 3 4))) ; 4
(newline)
(display (append '(1 2) '(3 4))) ; (1 2 3 4)
(newline)
```

**Ejemplo 3: Cadenas**:
```scheme
(display (string-append "Hola " "Mundo"))
(newline)
(display (string-length "Test")) ; 4
(newline)
(display (string=? "abc" "abc")) ; #t
(newline)
```

**Ejemplo 4: Definición de funciones**:
```scheme
(define (doble x) (* x 2))
(display (doble 4)) ; 8
(newline)

(define (saludar nombre) (string-append "Hola " nombre))
(display (saludar "Ana")) ; "Hola Ana"
(newline)
```

---

## 6. Limitaciones y Futuras Extensiones

1. **Expresiones Lambda**  
   - Falta soporte para crear funciones anónimas con `(lambda (x) <cuerpo>)`.  

2. **Sistema de Tipos Mejorado**  
   - Sería deseable una verificación más estricta de tipos para evitar operaciones con tipos incompatibles.  

3. **Macros**  
   - Scheme suele permitir macros que expanden el lenguaje. No están implementadas actualmente.  

4. **Más Funciones de Lista**  
   - Se pueden incorporar funciones como `map`, `filter`, `fold`, y otras presentes en Scheme clásico.  

5. **Manejo de E/S Más Completo**  
   - Soporte para lectura de cadenas, booleanos y otros tipos complejos con la forma `(read)`.  

---

## 7. Conclusión

Este intérprete de Scheme proporciona funcionalidades básicas y algunas extensiones útiles para listas y cadenas. Su diseño se fundamenta en una arquitectura clara de **visitador** y **tablas** de símbolos/funciones, lo que facilita su mantenimiento y extensión.  

¡Gracias por utilizar este intérprete de Scheme! Si deseas contribuir con nuevas características, correcciones o mejoras de rendimiento, no dudes en proponer tus ideas mediante una **issue** o un **pull request** en el repositorio correspondiente.