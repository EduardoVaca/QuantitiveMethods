import math


def get_combinations_count(n=None, r=None):
    if not n or not r:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

def get_permutations_count(n=None, r=None):
    if not n or not r:
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

#print(get_combinations_count())
#print(get_permutations_count())
print(get_standard_dev())