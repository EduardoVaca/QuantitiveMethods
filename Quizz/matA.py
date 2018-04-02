# teamorco
# Raul Mar A00512318
# Eduardo Vaca A01207563
# Javier Rodriguez A01152572

import random
import math

def getRandomNumbers(n, ones):
	opts = [(r, c) for r in range(n) for c in range(n) if r != c]
	random.shuffle(opts)
	return opts[:ones]

def numberOfOnes(p, n):
	return int(math.ceil((n*n) * (p/100)))


def fillMatrix(matrix, n, ones):
	for r, c in getRandomNumbers(n, ones):
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
	ans = fillMatrix(matA, n, ones)
	min_far = 100000000000000000000000000
	max_far = -1
	total_ones = 0
	for row in ans:
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