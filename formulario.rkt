#lang racket
;; factorial
;; n number
(define (factorial n)
  (factorial_p n 1))
(define (factorial_p n total)
 (if (<= n 1)
    total
    (factorial_p (- n 1) (* n total))))
;; nCr
;; n number of choices
;; r number of choices to pick
(define (combination n r)
  (/ (factorial n) (* (factorial r) (factorial (- n r)))))
;; nPr
;; n number of choices
;; r number of choices to pick
(define (permutation n r)
  (/ (factorial n) (factorial (- n r))))
;; Mean ∑ x*p(x)
;; x list of discrete variables x
;; px list od probability mass functions p(x)
(define (mean x px)
  (if (and (empty? x) (empty? px))
      0
      (+ (* (car x) (car px)) (mean (cdr x) (cdr px)))))    
(mean '(1 2 3 4 5 6 7) '(0.01 0.03 0.13 0.25 0.39 0.17 0.02))
;; variance
(define (pow x n)
  (if (= n 0)
      1
      (* x (pow x (- n 1)))))
(define (variance x px)
  (variance_p x px (mean x px)))
(define (variance_p x px mean)
  (if (and (empty? x) (empty? px))
      0
      (+ (* (pow (- (car x) mean) 2) (car px)) (variance_p (cdr x) (cdr px) mean))))
(variance '(1 2 3 4 5 6 7) '(0.01 0.03 0.13 0.25 0.39 0.17 0.02))
;; standard deviation
(define (std x px)
  (sqrt (variance x px)))
(std '(1 2 3 4 5 6 7) '(0.01 0.03 0.13 0.25 0.39 0.17 0.02))
;; binomial distribution
;; mean = np
;; variance = npq
(define (binomial_distribution n k p)
  (* (combination n k) (pow p k) (pow (- 1 p) (- n k))))
(binomial_distribution 4 2 0.8 )
  