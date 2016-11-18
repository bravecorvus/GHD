(define factorial

  (lambda (n)
    (display n) (newline)
    (if (< n 1) 1
      (* n (factorial (- n 1))))))

; main
(printf "Input the number you want to factorialized in the following structure: '(factorial #)' (where # is the number you want a factorial of)")


; (display (factorial userinput))
; (newline)
; (factorial (+ n 1))))))
n