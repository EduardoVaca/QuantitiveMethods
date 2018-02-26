import random

def get_max_m(my_func, limit1, limit2):
    return max(my_func(limit1), my_func(limit2))

def get_two_rand(limit1, limit2):
    return (random.uniform(limit1, limit2), random.uniform(limit1, limit2))

def get_x_star(limit1, limit2, r1):
    return limit1+(limit2-limit1)*r1

def accept_decline_method(limit1, limit2, my_func, n):
    values = []
    M = get_max_m(my_func, limit1, limit2)
    while len(values) < n:
        rands = get_two_rand(limit1, limit2)
        x = get_x_star(limit1, limit2, rands[0])
        if rands[1] <= my_func(x):
            values.append(x)
    return values

def main():

    def my_func(x):
        return 2*x
    
    limit1, limit2, n = [int(x) for x in input().split(' ')]
    print(accept_decline_method(limit1, limit2, my_func, n))

if __name__ == "__main__":
    main()