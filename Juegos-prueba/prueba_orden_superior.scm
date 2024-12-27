;Función map: aplicar una función a cada elemento de una lista
(define (map func llista)
  (cond
    ((null? llista) '())  ; Caso base: lista vacía
    (else (cons (func (car llista)) (map func (cdr llista))))))  ;Aplicar func al car y recursión al cdr

;Función filter: filtrar elementos de una lista según un predicado
(define (filter predicat llista)
  (cond
    ((null? llista) '())  ; Caso base: lista vacía
    ((predicat (car llista))
     (cons (car llista) (filter predicat (cdr llista)))) ; Incluir si cumple el predicado
    (else (filter predicat (cdr llista))))) ;  Ignorar si no cumple el predicado

;Lista de prueba
(define lista '(1 2 3 4 5 6 7 8 9 10))

;Funciones nombradas
(define (duplicar x) (* x 2))
(define (incrementar x) (+ x 1))
(define (modulo2 x) (mod x 2))
(define (mayor-que-5 x) (> x 5))
(define (menor-que-5 x) (< x 5))
(define (es-par x) (= (mod x 2) 0))
(define (es-multiplo-de-3 x) (= (mod x 3) 0))
(define (impar x) (= (mod x 2) 1))
(define (aplica-dos-cops f x) (f (f x)))

;Pruebas
(display (map duplicar lista))   
(newline)

(display (map incrementar lista))   
(newline)

(display (map modulo2 lista))   
(newline)

(display (filter mayor-que-5 lista))   
(newline)

(display (filter menor-que-5 lista))   
(newline)

(display (filter es-par lista))   
(newline)

(display (map duplicar (filter es-par lista)))   
(newline)

(display (map duplicar (filter menor-que-5 lista)))   
(newline)

(display (filter es-multiplo-de-3 (map duplicar lista)))   
(newline)

(display (map duplicar '()))   
(newline)

(display (filter mayor-que-5 '()))   
(newline)

(display (map incrementar (filter menor-que-5 lista)))   
(newline)

(display (filter impar lista))   
(newline)

(display (map duplicar (filter impar lista))) 
(newline)

(display (aplica-dos-cops duplicar 5))  
(newline)
