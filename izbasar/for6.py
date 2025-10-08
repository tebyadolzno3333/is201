
price = float(input())
weight = 1.2
while weight <= 2.0:
	cost = weight * price
	print(f"{weight:.1f} кг стоит {cost}")
	weight += 0.2

