(define guardbehavior
  (lambda (num) ; a non-negative integer
    (if (number? num) (+ num 1)
	;; assert:  num > 0
	(display num))))
