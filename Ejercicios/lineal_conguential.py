# Generador congruencial lineal
import math

def is_pattern_repeated(l):
    if len(l) > 2 and len(l) % 2 == 0:
        for i in range(math.floor(len(l)/2)):
            if l[i] != l[i+math.floor(len(l)/2)]:
                return False

        return True
    else:
        return False

m, a, c, z = [int(x) for x in input().split()]
values = []
while not is_pattern_repeated(values):
    z = (a*z+c)%m
    values.append(z)
print('Z: {}'.format(values[0:math.floor(len(values)/2)]))
print('R: {}'.format([x/m for x in values[0:math.floor(len(values)/2)]]))