# Intérprete Scheme

**Scheme** es un lenguaje de programación funcional basado en expresiones y funciones. Este proyecto implementa un **intérprete de Scheme** que permite al usuario evaluar programas de manera sencilla, con soporte para un conjunto amplio de características y funcionalidades. Está diseñado para manejar programas de cálculo funcional y estructurado, brindando herramientas para definir funciones, manejar estructuras condicionales, operar con listas y cadenas, y trabajar con expresiones lógicas y aritméticas.

El intérprete también soporta **funciones de orden superior** y permite realizar cálculos avanzados sin preocuparse de detalles como la gestión de memoria. Además, incluye un sistema básico de manejo de errores para prevenir problemas comunes, como divisiones por cero o llamadas a funciones no definidas.

---

## Especificación del Lenguaje

### Tipos de datos y estructuras

En este intérprete de Scheme, se manejan los siguientes tipos de datos:

- **Números enteros**: Representan la base de las operaciones matemáticas.
- **Booleanos**: Los valores `#t` (true) y `#f` (false) representan el resultado de evaluaciones lógicas.
- **Cadenas de texto**: Utilizadas para mostrar mensajes o realizar concatenaciones.
- **Listas**: Representadas con el formato `'(<elementos>)` o listas vacías `'()`.

El intérprete **gestiona variables y funciones locales**, limitando su alcance al ámbito en el que son definidas. También incluye un sistema básico de excepciones para manejar errores de ejecución y programación.

---

### Instrucciones y Operaciones

El lenguaje implementa las siguientes construcciones y operadores:

#### Condicionales
Scheme permite trabajar con estructuras condicionales simples y avanzadas:

- **Condicional `if`**:
  ```scheme
  (if <condicion> <expr_si_verdadero> <expr_si_falso>)
  ```

- **Condicional `cond`**:
  ```scheme
  (cond
    (<condicion1> <resultado1>)
    (<condicion2> <resultado2>)
    (else <resultado_por_defecto>))
  ```

#### Bucles
Scheme en su diseño original no incluye bucles iterativos explícitos, pero estos se pueden simular mediante recursión y funciones.

#### Operadores
El intérprete soporta:
- **Operadores aritméticos**: `+`, `-`, `*`, `/`, `mod`, `^` (exponenciación).
- **Operadores de comparación**: `<`, `<=`, `>`, `>=`, `=`, `<>`.
- **Operadores lógicos**: `and`, `or`, `not`.

Ejemplo:
```scheme
(display (+ 3 5)) ; 8
(display (and #t (< 2 5))) ; #t
```

#### Manejo de listas
El intérprete incluye operaciones básicas y avanzadas sobre listas:
- `car`: Devuelve el primer elemento.
- `cdr`: Devuelve la lista sin el primer elemento.
- `cons`: Construye una nueva lista añadiendo un elemento al inicio.
- `null?`: Verifica si una lista está vacía.
- **Nuevas operaciones**: 
  - `length`: Retorna la longitud de la lista.
  - `append`: Concatena dos listas.

Ejemplo:
```scheme
(display (length '(1 2 3))) ; 3
(display (append '(1 2) '(3 4))) ; (1 2 3 4)
```

#### Manejo de cadenas
Se añaden funciones para manipular cadenas de texto:
- `string-append`: Concatena múltiples cadenas.
- `string-length`: Retorna la longitud de una cadena.
- `string=?`: Verifica si dos cadenas son iguales.

Ejemplo:
```scheme
(display (string-append "Hola, " "Mundo!")) ; Hola, Mundo!
(display (string-length "Test")) ; 4
(display (string=? "abc" "abc")) ; #t
```

#### Funciones
El núcleo del lenguaje son las funciones, que permiten definir cálculos reutilizables. Las funciones son **implicítamente tipadas**, y soportan recursión, ámbito local y funciones como parámetros.

Ejemplo:
```scheme
(define (factorial n)
  (if (= n 0) 1 (* n (factorial (- n 1)))))

(display (factorial 5)) ; 120
```

---

## Implementación

### Componentes Principales

1. **`Scheme.g4`**
   - Define la gramática del lenguaje en ANTLR4.
   - Incluye soporte para expresiones aritméticas, listas, cadenas, funciones y estructuras condicionales.

2. **`EvalVisitor.py`**
   - Implementa la evaluación del árbol sintáctico abstracto (AST) generado por ANTLR4.
   - Maneja tablas de funciones y variables para gestionar los ámbitos.
   - Soporta el manejo de errores, evaluaciones condicionales, recursión y operaciones avanzadas.

3. **`Scheme.py`**
   - Punto de entrada principal para ejecutar programas en Scheme.
   - Llama al `EvalVisitor` para evaluar el AST generado.

4. **`Makefile`**
   - Automatiza tareas como generación de código, pruebas y ejecución.

---

## Instrucciones de Uso

### Configuración
1. Generar los archivos de ANTLR4:
   ```bash
   make aux
   ```
2. Construir el proyecto:
   ```bash
   make build
   ```

### Ejecución
Ejecutar un programa en Scheme:
```bash
python3 Scheme.py programa.scm
```

### Pruebas
Correr todas las pruebas predefinidas:
```bash
make test
```

---

## Ejemplos de Uso

**Ejemplo 1**: Operaciones aritméticas
```scheme
(display (+ 3 7)) ; 10
(display (* 4 5)) ; 20
```

**Ejemplo 2**: Manejo de listas
```scheme
(display (length '(1 2 3))) ; 3
(display (append '(1) '(2 3))) ; (1 2 3)
```

**Ejemplo 3**: Definición y uso de funciones
```scheme
(define (suma x y) (+ x y))
(display (suma 4 5)) ; 9
```

---

## Mejoras Realizadas y Futuras

1. **Ampliación del soporte a listas y cadenas**:
   - Se añadieron las funciones `length`, `append`, `string-append`, entre otras.

2. **Errores mejorados**:
   - El intérprete detecta casos como división por cero o funciones mal definidas.

3. **Futuras extensiones**:
   - Soporte para expresiones lambda (`(lambda (x) <expr>)`).
   - Sistema de tipos avanzado para detectar errores antes de la evaluación.
   - Soporte para macros y construcciones como `case`.

---

## Agradecimientos

Este proyecto fue desarrollado como una práctica educativa. Agradecemos a las herramientas como **ANTLR4** y **Python** por permitirnos implementar un lenguaje funcional con relativa facilidad. También queremos reconocer a los desarrolladores que contribuyeron con ideas para extender el diseño del intérprete.

**¡Esperamos que este intérprete sea útil y sirva como base para futuros proyectos en Scheme!**