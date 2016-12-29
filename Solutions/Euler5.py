#Smallest multiple
def Euler5(n):
	l=list(range(n+1))[2:]
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[j]%l[i]==0:
				l[j]//=l[i]
	p=1
	for x in l:
		p*=x
	return p

print(Euler5(100))