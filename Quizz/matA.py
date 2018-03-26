# teamorco
# Raul Mar A00512318
# Eduardo Vaca A01207563
# Javier Rodriguez A01152572

import random
import math

def getRandomNumbers(n, ones):
	opts = [(r, c) for r in range(n) for c in range(n) if r != c]
	random.shuffle(opts)
	print(opts)
	return opts[:ones]
	# return opts[random.randint(0, len(opts) - 1)]
	# while (True):
	# 	r1 = random.randint(0, n - 1)
	# 	r2 = random.randint(0, n - 1)
	# 	if r1 != r2:
	# 		break
	# return r1, r2

def numberOfOnes(p, n):
	return int(math.ceil((n*n) * (p/100)))


def fillMatrix(matrix, n, ones):
	for r, c in getRandomNumbers(n, ones):
		matrix[r][c] = 1
	# while (ones > 0):
	# 	r1, r2 = getRandomNumbers(n)
	# 	if matrix[r1][r2] != 1:
	# 		matrix[r1][r2] = 1
	# 		ones = ones - 1
	return matrix

def main():
	n = input("Valor de n: ")
	p = float(input("Porcentaje: "))
	matA = [[0 for i in range(n)] for j in range(n)]
	ones = numberOfOnes(p, n)
	print("numero de unos -> ", ones)
	ans = fillMatrix(matA, n, ones)
	min_far = 100000000000000000000000000
	max_far = -1
	for row in ans:
		total = 0
		for i in row:
			if i == 1:
				total += 1
		min_far = min(total, min_far)
		max_far = max(total, max_far)
		print(row, total)
	print("minimo: ", min_far)
	print("maximo: ", max_far)




if __name__ == "__main__":
	main()