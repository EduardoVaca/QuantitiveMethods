# teamorco
# Raul Mar A00512318
# Eduardo Vaca A01207563
# Javier Rodriguez A01152572

import random
import math

def getRandomCoords(n, ones):
	"""
	This method creates a list with tuples of all the possible valid spaces
	where a 1 can be stored
	PARAMS:
	- n: size of square matrix
	- ones: total number of ones that need to be filled
	RETURNS:
	- opts: list with spaces to change
	"""
	opts = [(r, c) for r in range(n) for c in range(n) if r != c]
	random.shuffle(opts)
	return opts[:ones]

def numberOfOnes(p, n):
	"""
	This method computes the total number of ones
	that will need to be filled by the matrix
	PARAMS:
	- p: probability given by the user
	- n: size of square matrix
	RETURNS:
	- total number of ones rounded up
	"""
	return int(math.ceil((n*n) * (p/100)))


def fillMatrix(matrix, coords):
	"""
	This method fills the ones on the matrix
	PARAMS:
	- matrix: matrix that will be filled
	- coords: list of tuples with coords that need to be filled
	RETURNS:
	- matrix: matrix filled with ones on given coords
	"""
	for r, c in coords:
		matrix[r][c] = 1
	return matrix

def main():
	n = int(input("Valor de n: "))
	p = float(input("Porcentaje: "))
	ones = numberOfOnes(p, n)
	if (n*n) - n < ones:
		print("El porcentaje debe de ser menor")
		return
	matA = [[0 for i in range(n)] for j in range(n)]
	print("numero de unos -> ", ones)
	coords = getRandomCoords(n, ones)
	newMatrix = fillMatrix(matA, coords)
	min_far = 100000000000000000000000000
	max_far = -1
	total_ones = 0
	for row in newMatrix:
		total = 0
		for i in row:
			if i == 1:
				total += 1
		min_far = min(total, min_far)
		max_far = max(total, max_far)
		total_ones += total
		print(row, total)
	print("minimo: ", min_far)
	print("maximo: ", max_far)
	print("total de unos: ", total_ones)

if __name__ == "__main__":
	main()