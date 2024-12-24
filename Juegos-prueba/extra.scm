; Pruebas de operaciones avanzadas con listas
(display "Pruebas de operaciones avanzadas con listas") (newline)

(display "length '(1 2 3 4): ")
(display (length '(1 2 3 4))) ; Debería devolver 4
(newline)

(display "append '(1 2) '(3 4): ")
(display (append '(1 2) '(3 4))) ; Debería devolver '(1 2 3 4)
(newline)

; Pruebas de operaciones avanzadas con cadenas
(newline)
(display "Pruebas de operaciones avanzadas con cadenas") (newline)

(display "string-append Hola,  mundo!: ")
(display (string-append "Hola, " "mundo!")) ; Debería devolver "Hola, mundo!"
(newline)

(display "string-length Hola: ")
(display (string-length "Hola")) ; Debería devolver 4
(newline)

(display "string=? abc abc: ")
(display (string=? "abc" "abc")) ; Debería devolver #t
(newline)

(display "string=? abc def: ")
(display (string=? "abc" "def")) ; Debería devolver #f
(newline)

; Fin de las pruebas
(newline)
(display "Pruebas finalizadas.") (newline)
