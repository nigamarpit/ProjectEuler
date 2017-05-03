def cycleLength(n):
	res = 10
	j = 0
	while res != 10 or j < 1:
		res = (res % n) * 10
		j += 1
	return j

def Euler26():
	long = 0
	for i in range(2, 1000):
		if i%2 != 0 and i%5 != 0:
			length = cycleLength(i)
			if length > long:
				long = length
				res = i
	return res

print(Euler26())