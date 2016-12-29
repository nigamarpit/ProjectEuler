#Summation of primes
def Euler10(num):
	l=[1]*(num+1)
	s=0
	for i in range(2,(num+1)):
		if l[i]==0:
			continue
		print(i)
		s+=i
		y=1
		while i*y<(num+1):
			l[i*y]=0
			y+=1
	return s

print(Euler10(2000000))