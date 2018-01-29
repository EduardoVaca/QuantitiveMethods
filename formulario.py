import math


def get_combinations_count(n=None, r=None):
    if not n or not r:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

def get_permutations_count(n=None, r=None):
    if not n or not r:
        n, r = int(input('n:')), int(input('r:'))
    return math.floor(math.factorial(n)/math.factorial(n-r))


print(get_combinations_count())
print(get_permutations_count())