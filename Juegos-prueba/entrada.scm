(define (sumar-dos-valors)
  (display "Introduce dos valores: ")
  (let ((val1 (read))
        (val2 (read)))
     (display "La suma es: ")
     (display (+ val1 val2))
     (newline)))

(sumar-dos-valors)
