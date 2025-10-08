
A = int(input())
B = int(input())
if A < B:
	total = 0
	for i in range(A, B + 1):
		total += i ** 2
	print(total)
else:
	print("A должно быть меньше B")

