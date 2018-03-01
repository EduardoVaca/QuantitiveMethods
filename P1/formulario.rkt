#lang racket
;; factorial
;; calculates the factorial of a given number
;; n: number
(define (factorial n)
  (factorial_p n 1))
(define (factorial_p n total)
 (if (<= n 1)
    total
    (factorial_p (- n 1) (* n total))))
;; nCr
;; calculates the number of combinations
;; n: number of choices
;; r: number of choices to pick
(define (combination n r)
  (/ (factorial n) (* (factorial r) (factorial (- n r)))))
;; nPr
;; n: number of choices
;; r: number of choices to pick
(define (permutation n r)
  (/ (factorial n) (factorial (- n r))))
;; Mean ∑ x*p(x)
;; x: list of discrete variables x
;; px: list of probability mass functions p(x)
(define (mean x px)
  (if (and (empty? x) (empty? px))
      0
      (+ (* (car x) (car px)) (mean (cdr x) (cdr px)))))    
;(mean '(1 2 3 4 5 6 7) '(0.01 0.03 0.13 0.25 0.39 0.17 0.02))
;; variance

;; Pow
;; calculates the value of x to the power of n
;; x: base value
;; n: exponent value
(define (pow x n)
  (if (<= n 0)
      1
      (* x (pow x (- n 1)))))
;; Variance
;; calculates the variance
;; x: values of x
;; px: values of p(x)
(define (variance x px)
  (variance_p x px (mean x px)))
(define (variance_p x px mean)
  (if (and (empty? x) (empty? px))
      0
      (+ (* (pow (- (car x) mean) 2) (car px)) (variance_p (cdr x) (cdr px) mean))))
;(variance '(1 2 3 4 5 6 7) '(0.01 0.03 0.13 0.25 0.39 0.17 0.02))
;; standard deviation
;; calculates the standard deviation
;; x: values of x
;; px: values of p(x)
(define (std x px)
  (sqrt (variance x px)))
;(std '(1 2 3 4 5 6 7) '(0.01 0.03 0.13 0.25 0.39 0.17 0.02))
;; DISTRIBUTIONS ;;

;; binomial distribution
;; calculates the binomail distribution
;; n: number of trials
;; k: list with the number of successes
;; p: success probability
(define (binomial_distribution n k p)
  (if (empty? k)
      0
      (+
       (* (combination n (car k))
          (pow p (car k))
          (pow (- 1 p) (- n (car k))))
       (binomial_distribution n (cdr k) p))))
; (binomial_distribution 4 '(0 1 2) 0.8 )

;; poisson_distribution
;; calculates the poisson distribution, lam = np where n is number of tests and p the probability
;; x: list of values
;; lam: mean/lamba of poisson_distribution
(define (poisson_distribution x lam)
  (if (empty? x)
      0
      (+
       (/
        (* (expt (exp 1) (* -1 lam))
           (expt lam (car x)))
        (factorial (car x)))
       (poisson_distribution (cdr x) lam))))
;(poisson_distribution '(1 2 3 4 5) 4.5 )

;; exponential distribution
;; calculculates the exponential distribution
;; x: value for x
;; lam: lambda value, 1 / lambda
;; limit1: limit for x
;; limit2: limit for x
;; NOTE: limit1 < limit 2
(define (proc_ed lam x)
   (- 1 (expt (exp 1) (* x lam -1))))
(define (exponential_distribution lam lim1 lim2)
  (if (= lim1 lim2)
      (proc_ed lam lim1)
      (- (proc_ed lam lim2) (proc_ed lam lim1))))
;(exponential_distribution 0.1667 10 10)
;(exponential_distribution 0.1667 5 10)
 