# teamorco
# Raul Mar A00512318
# Eduardo Vaca A01207563
# Javier Rodriguez A01152572

import random
import math

def getRandomNumbers(n, ones):
	"""
	Creates a list of tuples of all the posible placings for the ones
	in the symetrical matrix.
	Only the botom part of the matrix is beeing asigned and then mirrored
	PARAMS:
		-n: Size of the symetrical matrix of nxn
 		-ones: Total number of ones that need to be filled
	RETURNS:
		-opts: all the spaces where 1's might be placed divided by 2
	"""
	opts = [(r, c) for r in range(n) for c in range(n) if r != c and r < c]
	random.shuffle(opts)
	return opts[:int(ones/2)]

def numberOfOnes(p, n):
	"""
	Computes the total number of 1's that will be placed on the MATRIX
	PARAMS:
		-p: probability of 1's given by the user
		-n: size of the matrix in nxn
	RETURNS:
		- total number of ones rounded up which are also pairs
	"""
	ones = int(math.ceil((n*n) * (p/100.0)))
	return  ones if ones % 2 == 0 else ones - 1


def fillMatrix(matrix, n, ones):
	"""
	This method fills the matrix with the values generated, it does it symetricaly
	because on getRandomNumbers() only the bottom part of the matrix was created
	and in this function it gets filled normally and inverse.
	PARAMS:
		-matrix:Matrix that will be filled
		-n: size of the matrix in nxn
		-ones:the amount of ones about to be placed
	"""
	for r, c in getRandomNumbers(n, ones):
		matrix[r][c] = 1
		matrix[c][r] = 1
	return matrix

def main():
	"""
	Main function:
 		-gets the necesary inputs
		-calls numberOfOnes()
		-calls fillMatrix()
		-looks for the min and max number of ones:
		-prints total of total_ones
	"""
	n = int(input("Valor de n: "))
	p = float(input("Porcentaje: "))
	ones = numberOfOnes(p, n)
	if (n * n) - n < ones:
		print("El porcentaje debe de ser menor")
		return
	print("numero de unos -> ", ones)
	matB = [[0 for i in range(n)] for j in range(n)]
	ans = fillMatrix(matB, n, ones)
	min_far = 100000000000000000000000000
	max_far = -1
	total_ones = 0
	for row in ans:
		total = 0
		for i in row:
			if i == 1:
				total += 1
		total_ones += total
		min_far = min(total, min_far)
		max_far = max(total, max_far)
		print(row, total)
	print("minimo: ", min_far)
	print("maximo: ", max_far)
	print("total de unos: ", total_ones)

if __name__ == "__main__":
	main()
