; Definición de la función map
(define (map func llista)
  (cond
    ((null? llista) '())  ; Caso base: lista vacía
    (else (cons (func (car llista)) (map func (cdr llista)))))) ; Aplicar func al car y recursión al cdr

; Definición de la función filter
(define (filter predicat llista)
  (cond
    ((null? llista) '())  ; Caso base: lista vacía
    ((predicat (car llista))
     (cons (car llista) (filter predicat (cdr llista)))) ; Incluir si cumple el predicado
    (else (filter predicat (cdr llista)))))  ; Ignorar si no cumple el predicado

; Lista de prueba
(define lista '(1 2 3 4 5 6 7 8 9 10))

; Prueba de map: duplicar cada elemento
(display (map (lambda (x) (* x 2)) lista)) ; Esperado: (2 4 6 8 10 12 14 16 18 20)
(newline)

; Prueba de filter: números pares
(display (filter (lambda (x) (= (mod x 2) 0)) lista)) ; Esperado: (2 4 6 8 10)
(newline)

; Combinación: duplicar solo los números pares
(display (map (lambda (x) (* x 2)) (filter (lambda (x) (= (mod x 2) 0)) lista))) ; Esperado: (4 8 12 16 20)
(newline)

; Función definida para verificar si un número es mayor que 5
(define (mayor-que-5? x) (> x 5))

; Filtrar números mayores que 5
(display (filter mayor-que-5? lista)) ; Esperado: (6 7 8 9 10)
(newline)

; Map sobre una función definida: sumar 1 a cada número mayor que 5
(display (map (lambda (x) (+ x 1)) (filter mayor-que-5? lista))) ; Esperado: (7 8 9 10 11)
(newline)

; Usar map y filter para generar cuadrados de números menores que 6
(display (map (lambda (x) (* x x)) (filter (lambda (x) (< x 6)) lista))) ; Esperado: (1 4 9 16 25)
(newline)
