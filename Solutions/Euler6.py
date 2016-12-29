#Sum square difference
def Euler6(n):
	s1=0
	for i in range(1,n+1):
		s1+=i*i
	s2=0
	for i in range(1,n+1):
		s2+=i
	return s2*s2-s1


print(Euler6(100))