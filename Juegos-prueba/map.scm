(define (doble x)
  (* x 2))

(define (mapear f lst)
  (if (null? lst)
      '()
      (cons (f (car lst)) (mapear f (cdr lst)))))

(display (mapear doble '(1 2 3 4)))
(newline)
