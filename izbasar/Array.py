# Ввод числа N
N = int(input())
# Проверка условия N > 0
if N > 0:
	arr = []
	for i in range(N):
		arr.append(2 * i + 1)
	print(arr)
else:
	print("N должно быть больше 0")
