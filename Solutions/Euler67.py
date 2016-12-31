#Maximum path sum I
import time
d=dict()
l=list()
def Euler67():
	for i in range(len(l)-2,-1,-1):
		for j in range(len(l[i])):
			l[i][j]+=max(l[i+1][j],l[i+1][j+1])
			#print(str(i)+'\t\t'+str(j)+'\t\t'+str(l[i][j]))
	return l[0][0]

f=open('Input67.txt','r')
for line in f:
	l.append(list(map(int,line.strip().split())))
#print(l)
start=time.time()
print(Euler67())
print(time.time()-start)