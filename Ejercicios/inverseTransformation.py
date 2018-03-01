import random

def inverseTransformation(n):
	for _ in range(n):
		r = random.uniform(0, 1)
		print(r * (99) + 1 )

inverseTransformation(int(input()))
