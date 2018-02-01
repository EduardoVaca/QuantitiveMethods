import math


def get_combinations_count(n=None, r=None):
    if  n is None or r is None:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

def get_permutations_count(n=None, r=None):
    if n is None or r is None:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/math.factorial(n-r))

def get_prob_list():
    return [(int(input('x{}: '.format(i+1))), float(input('p(x{}): '.format(i+1)))) for i in range(int(input('n of values:')))]

def get_mean(prob_list=None):
    prob_list = get_prob_list() if not prob_list else prob_list   
    return sum(x*y for x,y in prob_list)

def get_variance(prob_list=None, mean=None):
    prob_list = get_prob_list() if not prob_list else prob_list
    mean = get_mean(prob_list) if not mean else mean
    return sum(math.pow(x-mean, 2)*y for x,y in prob_list)

def get_standard_dev(variance=None, prob_list=None):    
    return math.sqrt(get_variance(prob_list, mean=None) if not variance else variance)

def binomial_distribution(n, k, p, q):
    """Computes the Binomial Distribution
    PARAMS:
    - n : number of tests
    - k : list of success
    - p : success prob
    - q : failure prob
    """
    return sum(get_combinations_count(n, x)*math.pow(p, x)*math.pow(q, n-x) for x in k)

# INCOMPLETE
def get_poisson(x, p):
    return sum(math.exp(-p)*(p**i)/math.factorial(i) for i in x)
