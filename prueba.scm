(define (es-par n)
  (= (mod n 2) 0)) ; Devuelve #t si n es divisible por 2

(define (es-impar n)
  (not (es-par n))) ; Devuelve lo opuesto de es-par

; Pruebas
(display (es-par 2)) ; Esperado: #t
(newline)

(display (es-par 3)) ; Esperado: #f
(newline)

(display (es-impar 2)) ; Esperado: #f
(newline)

(display (es-impar 3)) ; Esperado: #t
(newline)
