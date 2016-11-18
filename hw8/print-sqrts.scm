(define print-sqrts
    (lambda (n) ; print square roots from n to 5
        (if (> n 5) ’done
            (begin
                (display (sqrt n))
            (newline)
        (print-sqrts (+ n 1))))))