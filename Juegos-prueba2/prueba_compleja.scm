(define (es-divisible x y)
  (= (mod x y) 0))

(define (primo-rec n x)
  (if (> (* x x) n)
      #t
      (if (es-divisible n x)
          #f
          (primo-rec n (+ x 1)))))

(define (es-primo n)
  (if (< n 2)
      #f
      (primo-rec n 2)))

(display (es-primo 2)) ; Esperado: #t
(newline)

(display (es-primo 4)) ; Esperado: #f
(newline)

(display (es-primo 17)) ; Esperado: #t
(newline)
