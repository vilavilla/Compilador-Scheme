(define (par-impar? x)
  (cond
    ((= (mod x 2) 0) "par")
    ((= (mod x 2) 1) "impar")
    (#t "desconocido")))

(display (par-impar? 7)); Esperado: impar
(newline)
