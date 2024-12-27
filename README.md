# Intérprete Scheme

**Scheme** es un lenguaje de programación FUNCIONAL. Este proyecto implementa un **intérprete de Scheme** que permite al usuario evaluar programas sencillos.

El intérprete contiene un soporte para un conjunto amplio de características y funcionalidades. Está diseñado para manejar programas de cálculo funcional y estructurado, también aporta herramientas para definir funciones, manejar estructuras condicionales, operar con listas y cadenas, y trabajar con expresiones lógicas y aritméticas.

También soporta **funciones de orden superior** ,además de permitir cálculos avanzados sin preocuparse de detalles como la gestión de memoria, ya que al apoyarse en Python, este intérprete hereda su gestión automática de memoria. Y como cualquier intérprete incluye un sistema básico de manejo de errores de código para prevenir problemas comunes.

---

## Especificación del Lenguaje

### Tipos de datos y estructuras

En este intérprete de Scheme, se manejan los siguientes tipos de datos:

- **Números enteros**: Básicamente representan la base de las operaciones matemáticas.
- **Booleanos**: En este caso los valores `#t` (true) y `#f` (false) representan el resultado de evaluaciones lógicas.
- **Cadenas de texto**: Son utilizadas para mostrar mensajes o realizar concatenaciones.
- **Listas**: Las cuales se representan con el formato `'(<elementos>)` o listas vacías `'()`.

Además el intérprete **gestiona variables y funciones locales**, el cual limita a su alcance al ámbito en el que son definidas. Esta parte también incluye un sistema básico de excepciones para manejar errores de ejecución y programación.

---

### Instrucciones y Operaciones

El interprete permite que el usuario implemente las siguientes construcciones y operadores:

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

#### Operadores
El intérprete soporta los operadores:
- **Operadores aritméticos**: `+`, `-`, `*`, `/`, `mod`, `^` (exponenciación).
- **Operadores de comparación**: `<`, `<=`, `>`, `>=`, `=`, `<>`.
- **Operadores lógicos**: `and`, `or`, `not`.

Ejemplo:
```scheme
(display (+ 3 5)) ; 8
(display (and #t (< 2 5))) ; #t
```

#### Manejo de listas
El intérprete incluye estas operaciones básicas y avanzadas sobre listas:

- `car`: Devuelve el primer elemento de la lista.
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
(display (null? '())) ; #t
(display (cons 1 '(2 3))) ; (1 2 3)
```

#### **Let: Declaración de variables locales**

El **`let`** permite definir variables locales dentro de un bloque específico, es útil para cálculos temporales sin afectar otras partes del programa.

**Sintaxis:**
```scheme
(let ((var1 val1) (var2 val2) ...)
  <expr1>
  <expr2>
  ...)
```

**Ejemplo**:
```scheme
(let ((a 10) (b 20))
  (display "La suma de a y b es: ")
  (display (+ a b)); La suma de a y b es: 30
  (newline))
```


#### Manejo de cadenas
He añadido funciones para manipular cadenas de texto:
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
El núcleo de Scheme son las funciones, que permiten definir cálculos reutilizables. Estas funciones son **implícitamente tipadas**, esto significa que no necesitas declarar el tipo de una función o una variable explícitamente, ya que el lenguaje es dinámicamente tipado. 

Además, el intérprete admite **funciones de orden superior**, lo que significa que las funciones pueden ser pasadas como argumentos a otras funciones, retornadas como valores, o almacenadas en variables.

Ejemplo de función recursiva:
```scheme
(define (factorial n)
  (if (= n 0) 1 (* n (factorial (- n 1)))))

(display (factorial 5)) ; 120
```

Ejemplo de función de orden superior:
```scheme
(define (map func lst)
  (if (null? lst)
      '()
      (cons (func (car lst)) (map func (cdr lst)))))

(define (doblar x) (* x 2))

(display (map doblar '(1 2 3 4))) ; (2 4 6 8)
```
---

## Implementación

### Componentes Principales

1. **`Scheme.g4`**
   - Se define la gramática del lenguaje en ANTLR4.
   - Se incluye soporte para expresiones aritméticas, listas, cadenas, funciones y estructuras condicionales.

2. **`EvalVisitor.py`**
   - Una clase que implementa la evaluación del árbol sintáctico abstracto (AST) generado por ANTLR4.
   - Maneja tablas de funciones y variables para gestionar los ámbitos.
   - Se soporta el manejo de errores, evaluaciones condicionales, recursión y operaciones avanzadas.

3. **`Scheme.py`**
   - Es el punto de entrada principal para ejecutar programas en Scheme.
   - Llama al `EvalVisitor` para evaluar el AST generado.

4. **`Makefile`**
   - Automatiza tareas como generación de código, pruebas y ejecución.

---

## Instrucciones de Uso

### Configuración
1. Generar los archivos de ANTLR4:
   ```bash
   make 
   ```
2. Construir el proyecto (En caso de necesitarlo):
   ```bash
   make build
   ```
3. Generar los archivos de ANTLR4 con archivo (He añadido esta función ya que ANTLR4 dejó de funcionar, en caso auxiliar):
   ```bash
   make aux
   ```

### Ejecución
Ejecutar un programa en Scheme:
```bash
python3 Scheme.py programa.scm
```

### Pruebas

El comando `make test` ejecuta un conjunto de juego de pruebas que verifican el funcionamiento del intérprete. Estas pruebas están organizadas en tres partes principales:

---

#### **1. Pruebas Sencillas**

Estas pruebas evalúan las características más básicas del lenguaje como entrada/salida, cálculos aritméticos simples, condicionales y definiciones sencillas de funciones.

**Ejemplo 1**: Entrada de datos y suma
```scheme
(display "Ingrese dos números: ")
(newline)
(let ((x (read)) (y (read)))
  (display "La suma es: ")
  (display (+ x y))
  (newline))
```
**Salida esperada**:
```plaintext
Ingrese dos números: 
La suma es: <resultado_de_la_suma>
```

**Ejemplo 2**: Función condicional básica
```scheme
(define (parimpar x)
  (cond
    ((= (mod x 2) 0) "par")
    ((= (mod x 2) 1) "impar")
    (#t "desconocido")))

(display (parimpar 7)) ; Esperado: impar
(newline)
```

---

#### **2. Pruebas Complejas**

Estas pruebas abarcan características avanzadas como ejemlos de recursión, funciones de orden superior (`map`, `filter`), manejo de listas y condicionales complejos.

**Ejemplo 1**: Factorial recursivo
```scheme
(define (factorial n)
  (if (= n 0) 1
      (* n (factorial (- n 1)))))

(define (fibonacci n)
  (if (<= n 1) n
      (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))

(define (suma lista)
  (if (null? lista) 0
      (+ (car lista) (suma (cdr lista)))))

(display (factorial 5)) ; Esperado: 120
(newline)

(display (fibonacci 10)) ; Esperado: 55
(newline)

(display (suma '(1 2 3 4 5))) ; Esperado: 15
(newline)

```
---

#### **3. Pruebas de Errores**

Estas pruebas están diseñadas para verificar que el intérprete muestre correctamente los errores y muestre mensajes adecuados cuando se encuentran las situaciones no válidas que hemos implementado.

**Ejemplo 1**: Uso incorrecto de `null?`
```scheme
(display (null? 42)) ; Error esperado: 'null?' solo se puede usar con listas, recibido: 42
(newline)
```

**Ejemplo 2**: Llamada a una función con argumentos incorrectos
```scheme
(display (factorial)) ; Error esperado: Número incorrecto de argumentos para 'factorial'.
(newline)
```

**Ejemplo 3**: Uso de una variable no definida
```scheme
(display x) ; Error esperado: Variable o función 'x' no definida.
(newline)
```
---

### Cómo funciona el comando `make test`

1. **Ejecución de pruebas**:
   - Cada programa de prueba se ejecuta utilizando el intérprete (`Scheme.py`) y si es necesario con su archivo de entrada.
   - Las salidas generadas se comparan con los archivos de salida esperada utilizando el comando `diff`.

2. **Verificación de resultados**:
   - Si las salidas coinciden con las esperadas, la prueba se marca como correcta.
   - Si hay discrepancias, se informa del error y el archivo el cual es diferente.

---

### Ejecución del comando

Para correr las pruebas:
```bash
make test
```

**Salida esperada en consola**:
```plaintext
Ejecutando test...
Test simples...
Prueba suma.scm completada correctamente
Prueba cond.scm completada correctamente
....

Test complejos...
Prueba factorial.scm completada correctamente
...

Test errores...
Prueba errores1.scm completada correctamente
Prueba errores2.scm completada correctamente
Prueba errores3.scm completada correctament
...
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
   - Soporte para macros.

---

### Conclusión

Este proyecto ha resultado ser una práctica muy interesante para entender más en profundidad cómo funcionan los compiladores y los intérpretes. En esste proyecto al trabajar con herramientas como **ANTLR4** y **Python** me ha facilitado implementar un lenguaje funcional sea más sencillo de lo que esperaba. Ha resultado ser una buena oportunidad para aplicar lo que he aprendido en clase y conectar la teoría con algo más práctico.

Además, los materiales de clase me han sido de gran ayuda para desarrollar el intérprete. En general, ha sido una experiencia bastante educativa y me ha permitido ver de cerca lo complejo y a la vez fascinante que puede ser crear un lenguaje de programación desde cero.
