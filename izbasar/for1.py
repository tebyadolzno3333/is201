# Ввод чисел K и N
K = int(input())
N = int(input())
# Проверка условия N > 0
if N > 0:
	for _ in range(N):
		print(K)
else:
	print("N должно быть больше 0")