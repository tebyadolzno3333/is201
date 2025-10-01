N = 492
E = N % 10
D = (N // 10) % 10
S = N // 100
reversed_N = E * 100 + D * 10 + S
print(reversed_N)