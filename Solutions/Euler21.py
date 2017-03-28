d=dict()
def AmicableNumbers():
	sumAmicable=0
	for i in range(1,10001):
		if checkAmicable(i):
			sumAmicable+=i
			#print(i,True)
			continue
		#print(i,False)
	return sumAmicable

def checkAmicable(n):
	#input(n)
	b=0
	if d.get(n,False):
		b=d[n]
	else:
		b=sumProperDivisor(n)
		d[n]=b
	a=sumProperDivisor(b)
	if a==n:
		if a==b:
			return False
		else:
			return True
	else:
		return False



def sumProperDivisor(n):
	sumDivisors=0
	for i in range(1,int((n+2)/2)):
		if n%i==0:
			sumDivisors+=i
	return sumDivisors

	
print("Sum of all the amicable numbers under 10000: "+str(AmicableNumbers()))