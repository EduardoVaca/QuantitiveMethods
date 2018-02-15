"""
Author: Eduardo Vaca
"""
import math


def get_combinations_count(n=None, r=None):
    """Computes the total possible combinations
    PARAMS:
    - n : N
    - r : R
    RETURNS:
    Number of combinations
    """
    if  n is None or r is None:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

def get_permutations_count(n=None, r=None):
    """Computes the total possible permutations
    PARAMS:
    - n : N
    - r : R
    RETURNS:
    Number of permutations
    """
    if n is None or r is None:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/math.factorial(n-r))

def get_prob_list():
    """Input the prob list
    RETURNS:
    - list of tuples (x, prob(x))
    """
    return [(int(input('x{}: '.format(i+1))), float(input('p(x{}): '.format(i+1)))) for i in range(int(input('n of values:')))]

def get_mean(prob_list=None):
    """Compute the mean of a prob list
    PARAMS:
    - prob_list : list of tuples with (x, prob(x))
    RETURNS:
    - mean of list
    """
    prob_list = get_prob_list() if not prob_list else prob_list   
    return sum(x*y for x,y in prob_list)

def get_variance(prob_list=None, mean=None):
    """Compute the variance of a prob list
    PARAMS:
    - prob_list : list of tuples with (x, prob(x))
    - mean : mean of list
    RETURNS:
    - variance of list
    """
    prob_list = get_prob_list() if not prob_list and mean is None else prob_list
    mean = get_mean(prob_list) if not mean else mean
    return sum(math.pow(x-mean, 2)*y for x,y in prob_list)

def get_standard_dev(prob_list=None, variance=None):
    """Compute the standard devaition of a prob list
    PARAMS:
    - variance : variance of list
    - prob_list : list of tuples with (x, prob(x))
    RETURNS:
    - standard dev of list
    """  
    return math.sqrt(get_variance(prob_list, mean=None) if not variance else variance)

def get_uniform_values():
    """Get list of values for uniform distribution
    RETURNS:
    - list of values
    """
    return [int(input('value {}: '.format(x+1))) for x in range(int(input('n of values: ')))]

def get_uniform_mean(values=None):
    """Compute uniform mean
    PARAMS:
    - values : list of values
    RETURNS:
    - mean of values
    """
    if not values:
        values = get_uniform_values()
    return sum(x/len(values) for x in values)

def get_uniform_variance(values=None, mean=None):
    """Compute uniform variance
    PARAMS:
    - values : list of values
    - mean : uniform mean
    RETURNS:
    - variance of values
    """
    values = get_uniform_values() if not values and mean is None else values
    mean = get_uniform_mean(values) if mean is None else mean
    return sum(math.pow(x-mean, 2)/len(values) for x in values)

def get_uniform_standard_dev(values=None, variance=None):
    """Compute uniform standard dev
    PARAMS:
    - values : list of values
    - variance : uniform variance
    RETURNS:
    - standard dev of values
    """
    return math.sqrt(get_uniform_variance(values) if not variance else variance)

def binomial_distribution(n, k, p, q):
    """Computes the Binomial Distribution
    PARAMS:
    - n : number of tests
    - k : list of values
    - p : success prob
    - q : failure prob
    RETURNS:
    - Binomial dist
    """
    return sum(get_combinations_count(n, x)*math.pow(p, x)*math.pow(q, n-x) for x in k)

def poisson_distribution(x, lam=None, n=None, p=None):
    """Computes Poisson Distribution
    PARAMS:
    - x : list of x values
    - lam : lambda of possion dist
    - n : number of tests
    - p : prob
    RETURNS:
    - Poisson dist
    """
    if lam is None and (n is None or p is None) :
        return 0
    if lam is None:
        lam = n*p
    return sum(math.exp(-1*lam)*math.pow(lam, i)/math.factorial(i) for i in x)


def exponential_distribution(limit1, lam=None, mean=None, limit2=None):
    """Computes the exponential distribution
    PARAMS:
    - limit1 : limit for x
    - lam : lam value for the exp dist
    - mean : expected value
    - limit2 : limit for x
    RETURN:
    - exponential dist
    """
    if not lam and mean is not None:
        lam = 1/mean
    if limit2 is not None:
        return (1-math.exp(-1*lam*limit1)) - (1-math.exp(-1*lam*limit2)) if limit1 > limit2 else (1-math.exp(-1*lam*limit2)) - (1-math.exp(-1*lam*limit1))
    else:
        return (1-math.exp(-1*lam*limit1))
