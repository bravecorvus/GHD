(define print-sqrts
    (lambda (n) ; print square roots from n to 5
        (if (> n 5) 'done
            (begin
                (display (sqrt n))
                (newline)
                (print-sqrts (+ n 1))))))




;(define accumulator 0)

;(define sum-squares
    ;(lambda (n) ; print square roots from n to 5
        ;(if (< n 0) 'done
            ;(begin
                ;(+accumulator (* n n))
                ;sum-squares(n-1)
        ;    (begin
        ;        ;(sum-squares (+ (* n n ) (* (- n 1 ) (- n 1 ))))
;            )
;        )
;    )
;)


;I'm gonna be honest, I really don't understand Scheme
(define (sum-squares n)
  (* 1/6 n (+ n 1) (+ n n 1)))


(define print-sums
    (lambda (n) ; print square roots from n to 5
        (display (sum-squares n))
        (newline)))




;my attempts to get a read-evel loop
;Getting user input for what number they want
;(display "what do you want n to be")
;(newline)
;(define num (read))
;Getting user input for what operation they want to do
;(display "'1' for print-sqrts")
;(newline)
;(if (compare? func 1)(begin(begin(print-sqrts num)))(else (begin( (begin (display "Invalid number"))))))
;(display "'2' for sum-squares")
;(newline)
;(define func (read))
;(if (compare? func 2)(begin(begin(print-sqrts num)))(else (begin( (begin (display "Invalid number"))))))