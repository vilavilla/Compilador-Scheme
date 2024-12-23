(define (es-primo? n)
  (define (es-divisible? x y)
    (= (mod x y) 0))
  (define (primo-rec x)
    (if (> (* x x) n)
        #t
        (if (es-divisible? n x)
            #f
            (primo-rec (+ x 1)))))
  (if (< n 2)
      #f
      (primo-rec 2)))

(display (es-primo? 2)) ; Esperado: #t
(newline)

(display (es-primo? 4)) ; Esperado: #f
(newline)

(display (es-primo? 17)) ; Esperado: #t
(newline)
