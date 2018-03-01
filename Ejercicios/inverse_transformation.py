import random

def inverseTransformation(n, a, b):
	for _ in range(n):
		r = random.uniform(0, 1)
		print(r * (b-a) + a )

inverseTransformation(int(input()), 1, 100)
