import math
def FactorialDigitSum():
	prod=1
	for i in range(1,101):
		prod*=i
	return sum([int(i) for i in str(prod)])

print("Sum of digits in the number 100!: "+str(FactorialDigitSum()))