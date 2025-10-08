
N = int(input())
if N > 0:
	total = 0.0
	for i in range(1, N + 1):
		total = total + 1.0 / i
	print(total)
else:
	print("N должно быть больше 0")

