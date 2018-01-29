import math


def get_combinations_count(n=None, r=None):
    if not n or not r:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

def get_permutations_count(n=None, r=None):
    if not n or not r:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/math.factorial(n-r))


def get_mean(prob_list=None):
    if not prob_list:
        n = int(input('n of values:'))
        prob_list = [(int(input('x{}: '.format(i+1))), float(input('p(x{}): '.format(i+1)))) for i in range(n)]
    return sum(x*y for x,y in prob_list)


#print(get_combinations_count())
#print(get_permutations_count())
print(get_mean())