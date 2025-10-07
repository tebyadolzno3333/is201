4
A = int(input())
B = int(input())
if A < B:
	N = 0
	for i in range(B - 1, A, -1):
		print(i)
		N += 1
	print('N =', N)
else:
	print("A должно быть меньше B")
