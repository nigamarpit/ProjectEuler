#10001st prime
def Euler7(n):
	l=[1]*n
	primes=list()
	for i in range(2,len(l)):
		if l[i]!=1:
			continue
		#print(str(len(primes))+'\t\t'+str(i))
		primes.append(i)
		y=1
		while i*y<n:
			l[i*y]=0
			y+=1
		if len(primes)==10001:
			return primes[10000]

n=1000000
print(Euler7(n))