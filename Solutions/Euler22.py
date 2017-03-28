import time

def namesScores():
	f=open('Input22.txt','r')
	lst=[s[1:-1] for s in f.readline().split(',')]
	lst.sort()
	grandSumScore=0
	for i in range(len(lst)):
		sumScore=0
		for x in lst[i]:
			sumScore+=ord(x)-64
		sumScore*=(i+1)
		grandSumScore+=sumScore
	return grandSumScore

start=time.time()
print("Total of all the names scores in the file: "+ str(namesScores()))
print("Execution Time: "+str(round(time.time()-start,6))+" seconds")
