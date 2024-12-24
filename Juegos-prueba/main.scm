; Declaración de funciones y constantes para pruebas
(define x 42)  ; Declaración de una constante

(define (add a b)  ; Declaración de una función simple
  (+ a b))

(define (factorial n)  ; Función recursiva para calcular factorial
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

; Punto de entrada principal
(define (main)
  (write "Iniciando pruebas...") (newline)

  ; Prueba 1: Suma
  (display "Prueba 1: Suma") (newline)
  (display "(add 3 4) => ")
  (display (add 3 4))
  (newline)

  ; Prueba 2: Condicional simple
  (display "Prueba 2: Condicional simple") (newline)
  (display "(if (< 3 5) \"verdadero\" \"falso\") => ")
  (display (if (< 3 5) "verdadero" "falso")) ; Evaluación de una expresión lógica
  (newline)

  ; Prueba 3: Condicional múltiple (cond)
  (display "Prueba 3: Condicional múltiple") (newline)
  (display "(cond ((< 5 3) \"menor\") ((= 5 5) \"igual\") (else \"ninguno\")) => ")
  (display (cond
             ((< 5 3) "menor")
             ((= 5 5) "igual")
             (else "ninguno")))
  (newline)

  ; Prueba 4: Let
  (display "Prueba 4: Let") (newline)
  (display "(let ((a 10) (b 20)) (+ a b)) => ")
  (display (let ((a 10)
                 (b 20))
             (+ a b)))
  (newline)

  ; Prueba 5: Operadores aritméticos
  (display "Prueba 5: Operadores aritméticos") (newline)
  (display "(/ 8 4) => ")
  (display (/ 8 4))
  (newline)

  ; Prueba 6: Operadores lógicos
  (display "Prueba 6: Operadores lógicos") (newline)
  (display "(and (< 3 5) (= 4 4) ) => ")
  (display (and (< 3 5) (= 4 4) )) ; Debería imprimir #t
  (newline)

  ; Prueba 7: Trabajo con listas
  (display "Prueba 7: Trabajo con listas") (newline)
  (display "(car '(1 2 3)) => ")
  (display (car '(1 2 3)))
  (newline)

  ; Prueba 8: Factorial recursivo
  (display "Prueba 8: Factorial recursivo") (newline)
  (display "(factorial 5) => ")
  (display (factorial 5))
  (newline)

  (display "Pruebas finalizadas.") (newline))

; Llamada al punto de entrada
(main)
