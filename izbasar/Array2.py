# Ввод числа N
N = int(input())
# Проверка условия N > 0
if N > 0:
	arr = []
	for i in range(1, N + 1):
		arr.append(2 ** i)
	print(arr)
else:
	print("N должно быть больше 0")

