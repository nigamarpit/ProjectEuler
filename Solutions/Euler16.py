#Power digit sum
def Euler16(n):
	s=0
	while n>0:
		s+=n%10
		n//=10
	return s

#number for which we need to compute sum
n=2**1000
print(Euler16(n))