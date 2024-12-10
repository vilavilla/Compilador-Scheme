(define (valor-absolut x)
  (cond
    ((> x 0) x)
    ((< x 0) (- x))
    (#t 0)))

(valor-absolut -5)
(valor-absolut 5)
(valor-absolut 0)
