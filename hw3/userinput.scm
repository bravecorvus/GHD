(define getuserinput
  (lambda userinput)
  (printf "Input the number you want to factorialized ")
  (define userinput (read-line))
  (printf "You entered: ~a\n" userinput))