#Special Pythagorean triplet
def Euler9(sum):
	for a in range(1,sum):
		for b in range(1,sum):
			c=sum-a-b
			#print(str(a)+'\t\t'+str(b)+'\t\t'+str(c))
			if (a*a+b*b)==(c*c):
				return (a,b,c,a*b*c)

for i in range(1000,1001):
	print(str(i)+'\t\t'+str(Euler9(i)))