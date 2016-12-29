#Largest product in a series
def Euler8(n):
	f=open('Input8.txt','r')
	s=list()
	for line in f:
		s.append(line.rstrip())
	num=list(map(int,list(''.join(s))))
	#print(num)
	p=buildWindow(num,0,n)
	m=p
	i=n
	while i<=(len(num)-n):
		p=buildWindow(num,i,n)
		if p>m:
			m=p
		i+=1
	return m

def buildWindow(num,j,n):
	p=1
	for i in range(n):
		p*=num[j+i]
	return p

print(Euler8(13))