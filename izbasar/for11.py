
N = int(input())

if N > 0:
	total = 0
	for i in range(N, 2 * N + 1):
		total += i ** 2
	print(total)
else:
	print("N должно быть больше 0")


