import random

def inver_transformation(n):
	for _ in range(n):
		r = random.uniform(0, 1)
		print(r * (99) + 1)

inver_transformation(int(input()))
