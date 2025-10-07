# Ввод чисел A и B6
A = int(input())
B = int(input())
# Проверка условия A < B
if A < B:
	N = 0
	for i in range(A, B + 1):
		print(i)
		N += 1
	print('N =', N)
else:
	print("A должно быть меньше B")
