(define (factorial n)
  (if (= n 0) 1
      (* n (factorial (- n 1)))))

(define (fibonacci n)
  (if (<= n 1) n
      (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))

(define (suma lista)
  (if (null? lista) 0
      (+ (car lista) (suma (cdr lista)))))

(display (factorial 5)) ; Esperado: 120
(newline)

(display (fibonacci 10)) ; Esperado: 55
(newline)

(display (suma '(1 2 3 4 5))) ; Esperado: 15
(newline)
