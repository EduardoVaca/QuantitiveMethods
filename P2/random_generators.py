"""
Func for random generators
"""
import math

def mid_square(z, n):
    """Get n random numbers with seed z
    PARAMS:
    - z : seed (first number)
    - n : number of iterations
    RETURNS:
    - list of random numbers
    """
    results = []
    if len(str(z)) == 4:
        for _ in range(n):
            current_z = str(z**2)
            if len(current_z) < 8:
                current_z = ''.join(['0' for _ in range(8-len(current_z))]) + current_z
            z = int(current_z[2:6])
            results.append(float('0.'+str(z)))                
    else:
        print('N needs to have 4 digits')
    return results

def lineal_congruential(m, a, c, z):
    """Generate random numbers with lineal congrential
    PARAMS:
    - m : module magnitute
    - a : multiplicador 0 -> n-1
    - c : increment
    - z : seed
    RETURNS:
    - list of random numbers
    """
    def is_pattern_repeated(l):
        if len(l) > 2 and len(l) % 2 == 0:
            for i in range(math.floor(len(l)/2)):
                if l[i] != l[i+math.floor(len(l)/2)]:
                    return False

            return True
        else:
            return False    
    values = []
    while not is_pattern_repeated(values):
        z = (a*z+c)%m
        values.append(z)
    results = values[0:math.floor(len(values)/2)]
    print('Z: {}'.format(results))
    print('R: {}'.format([x/m for x in results]))
    print('Period length: {}'.format(len(results)))
    print('Period COMPLETE' if len(results) == m else 'Cicle INCOMPLETE')