; Función map: aplicar una función a cada elemento de una lista
(define (map func llista)
  (cond
    ((null? llista) '())  ; Caso base: lista vacía
    (else (cons (func (car llista)) (map func (cdr llista)))))) ; Aplicar func al car y recursión al cdr

; Función filter: filtrar elementos de una lista según un predicado
(define (filter predicat llista)
  (cond
    ((null? llista) '())  ; Caso base: lista vacía
    ((predicat (car llista))
     (cons (car llista) (filter predicat (cdr llista)))) ; Incluir si cumple el predicado
    (else (filter predicat (cdr llista)))))  ; Ignorar si no cumple el predicado

; Lista de prueba
(define lista '(1 2 3 4 5 6 7 8 9 10))

; Funciones nombradas
(define (duplicar x) (* x 2))
(define (incrementar x) (+ x 1))
(define (modulo2 x) (mod x 2))
(define (mayor-que-5 x) (> x 5))
(define (menor-que-5 x) (< x 5))
(define (es-par x) (= (mod x 2) 0))
(define (es-multiplo-de-3 x) (= (mod x 3) 0))
(define (impar x) (= (mod x 2) 1))

; Pruebas
(display (map duplicar lista)) ; Test 1
(newline)

(display (map incrementar lista)) ; Test 2
(newline)

(display (map modulo2 lista)) ; Test 3
(newline)

(display (filter mayor-que-5 lista)) ; Test 4
(newline)

(display (filter menor-que-5 lista)) ; Test 5
(newline)

(display (filter es-par lista)) ; Test 6
(newline)

(display (map duplicar (filter es-par lista))) ; Test 7
(newline)

(display (map duplicar (filter menor-que-5 lista))) ; Test 8
(newline)

(display (filter es-multiplo-de-3 (map duplicar lista))) ; Test 9
(newline)

(display (map duplicar '())) ; Test 10
(newline)

(display (filter mayor-que-5 '())) ; Test 11
(newline)

(display (map incrementar (filter menor-que-5 lista))) ; Test 12
(newline)

(display (filter impar lista)) ; Test 13
(newline)

(display (map duplicar (filter impar lista))) ; Test 14
(newline)
