(define (parimpar x)
  (cond
    ((= (mod x 2) 0) "par")
    ((= (mod x 2) 1) "impar")
    (#t "desconocido")))

(display (parimpar 7))
(newline)
