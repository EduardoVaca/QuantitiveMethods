
import numpy as np

def read_matrix(filename):
    fo = open(filename, 'r')    
    return np.matrix([list(map(float, x.strip().split(','))) for x in fo.readlines()])

def matrix_product(matrix, n):
    return matrix ** n

# filename, n = input('Filename: '), int(input('N: '))
# print(matrix_product(read_matrix(filename), n))
