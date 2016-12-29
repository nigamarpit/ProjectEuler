def Euler3(n):
	i=2
	while i*i<=n:
		#print(i)
		#print(n)
		if n%i==0:
			n/=i
		else:
			i+=1
	return n
x=600851475143
print(Euler3(x))