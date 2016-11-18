(define factorial
  (lambda (n)
    (if (< n 1) 1
    (* n (factorial (- n 1))))))


; main
(display "Input the number you want to factorialized (type in '(factorial #')\n")
(define m (or (string->number (read-line))
  (error "I said a number!")))

