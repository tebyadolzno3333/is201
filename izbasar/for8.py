
A = int(input())
B = int(input())
if A < B:
	product = 1
	for i in range(A, B + 1):
		product *= i
	print(product)
else:
	print("A должно быть меньше B")


