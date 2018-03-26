#lang racket
(define (factorial n)
  (factorial_p n 1))
(define (factorial_p n total)
 (if (<= n 1)
     total
     (factorial_p (- n 1) (* n total))))

;; nCr
(define (combination n r)
  (/ (factorial n) (* (factorial r) (factorial (- n r)))))
;; nPr
(define (permutation n r)
  (/ (factorial n) (factorial (- n r))))
