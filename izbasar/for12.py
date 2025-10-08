
N = int(input())
if N > 0:
    product = 1.0
    for i in range(1, N + 1):
        product *= 1 + i / 10
    print(product)
else:
    print("N должно быть больше 0")
