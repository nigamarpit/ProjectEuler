'''
Abundant number are those for which sum of proper divisors exceeds n
e.g. 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16
all number greater than 28123 can be written as sum of two abudant number
'''
lst=list()
sumTwoAbundantNo=list()
def NonAbundantSums():
	for i in range(1,28124):
		if checkAbundantNumber(i):
			lst.append(i)
		#flag=twoAbudantNumbers(i)
		#if not flag:
		#	sumTwoAbundantNo.append(i)
	print("Sum of all the positive integers which cannot be written as the sum of two abundant numbers: "+str(compute()))

def compute():
	l=set()
	for x in lst:
		for y in lst:
			l.add(x+y)
	s=list()
	for i in range(1,28124):
		if not i in l:
			s.append(i)
	return(sum(s))



'''
def twoAbudantNumbers(n):
	flag=False
	i=0
	while(i<len(lst)):
		for j in range(len(lst)-1,-1,-1):
			if (lst[i]+lst[j])==n:
				flag=True
				break
			elif lst[i]+lst[j]<n:
				break
		if flag:
			break
		else:
			i+=1
	if flag:
		return True
	else:
		return False
'''

def checkAbundantNumber(n):
	s=findSumProperDivisor(n)
	if s>n:		
		return True
	else:
		return False

def findSumProperDivisor(n):
	l=list()
	for i in range(1,int((n+2)/2)):
		if n%i==0:
			l.append(i)
	return sum(l)

NonAbundantSums()