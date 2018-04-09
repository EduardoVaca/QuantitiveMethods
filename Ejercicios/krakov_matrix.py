
import numpy as np

def read_matrix(filename):
    fo = open(filename, 'r')    
    return np.matrix([list(map(float, x.strip().split(','))) for x in fo.readlines()])

def matrix_product(matrix, n):
    original_matrix = np.matrix(matrix)
    for _ in range(n-1):
        matrix *= original_matrix
    print(matrix)        
    return matrix

filename, n = input('Filename: '), int(input('N: '))
matrix_product(read_matrix(filename), n)
