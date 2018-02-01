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
    prob_list = get_prob_list() if not prob_list else prob_list
    mean = get_mean(prob_list) if not mean else mean
    return sum(math.pow(x-mean, 2)*y for x,y in prob_list)

def get_standard_dev(variance=None, prob_list=None):
    """Compute the standard devaition of a prob list
    PARAMS:
    - variance : variance of list
    - prob_list : list of tuples with (x, prob(x))
    RETURNS:
    - standard dev of list
    """  
    return math.sqrt(get_variance(prob_list, mean=None) if not variance else variance)

def binomial_distribution(n, k, p, q):
    """Computes the Binomial Distribution
    PARAMS:
    - n : number of tests
    - k : list of success
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
    return sum(math.exp(-lam)*math.pow(lam, i)/math.factorial(i) for i in x)

