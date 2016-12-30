#Highly divisible triangular number
import time
def Euler12(n):
	c=1
	num=1
	while findFactors(num)<n:
		c+=1
		num+=c
		#print(str(num)+'\t\t'+str(l))
	return num

def findFactors(num):
	div=2
	for i in range(2,int(num**0.5)):
		if not num%i:
			div+=2
	return div

#number of factors
n=500
start_time = time.time()
print(Euler12(n))
print("Execution time: %s "%(time.time() - start_time))