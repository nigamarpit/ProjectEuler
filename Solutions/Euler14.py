#Longest Collatz sequence
def Euler14(num):
	m=0
	mn=2
	for i in range(2,num+1):
		c=collatz(i)
		#print(str(i)+'\t\t'+str(c))
		if c>m:
			mn=i
			m=c
	return (mn)

def collatz(x):
	c=0
	while x!=1:
		#print(x)
		c+=1
		#odd number
		if not x%2:
			x/=2
		#even number
		else:
			x=3*x+1
			
	return c

#largest number under which we want maximum chain
num = 1000000
print(Euler14(num))