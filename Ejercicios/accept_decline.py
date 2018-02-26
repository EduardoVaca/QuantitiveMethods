""" 
Generating random numbers with Acceptance-Decline method
Date: 26/Feb/2018
"""

import random

def get_max_m(funcs):
    current_max = 0
    for func in funcs:
        current_max = max(current_max, max(func[0](func[1][0]), func[0](func[1][1])))
    return current_max

def get_two_rand():
    return (random.uniform(0, 1), random.uniform(0, 1))

def get_x_star(limit1, limit2, r1):
    return limit1+(limit2-limit1)*r1

def get_func_by_limit(x, funcs):
    for func in funcs:
        if x >= func[1][0] and x <= func[1][1]:
            return func
    return None

def accept_decline_method(funcs, n):
    values = []
    M = get_max_m(funcs)
    counter = 0
    while len(values) < n:
        rands = get_two_rand()
        x = get_x_star(funcs[0][1][0], funcs[-1][1][1], rands[0])
        current_func = get_func_by_limit(x, funcs)
        if rands[1] <= current_func[0](x)/M:
            values.append(x)
        counter += 1
    print('{} accepted from {} iterations'.format(n, counter))
    return values


def main():

    def my_func(x):
        return -1*1/6+x/12
    
    def myfunc_2(x):
        return 4/3-x/6
    
    n_functions, n_iterations = [int(x) for x in input().split(' ')]
    funcs = []
    for i in range(n_functions):
        limit1, limit2 = [int(x) for x in input().split(' ')]
        if i == 0:
            funcs.append((my_func, (limit1, limit2)))
        else:
            funcs.append((myfunc_2, (limit1, limit2)))
    
    x_stars = accept_decline_method(funcs, n_iterations)
    print('MEAN: {}'.format(sum(x_stars)/len(x_stars)))
    print('MIN: {}'.format(min(x_stars)))
    print('MAX: {}'.format(max(x_stars)))
    print(x_stars)

if __name__ == "__main__":
    main()