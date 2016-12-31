#Lattice Paths
d=dict()
def Euler15(m,n):
	#print(str(m)+'\t\t'+str(n))
	if m==1 or n==1:
		return 1
	if d.get((m-1,n)) and d.get((m,n-1)):
		return d[(m-1,n)]+d[(m,n-1)]
	elif d.get((m-1,n)):
		x=Euler15(m,n-1)
		d[(m,n-1)]=x
		return d[(m-1,n)]+x
	elif d.get((m,n-1)):
		x=Euler15(m-1,n)
		d[(m-1,n)]=x
		return d[(m,n-1)]+x
	else:
		x=Euler15(m-1,n)
		y=Euler15(m,n-1)
		d[(m-1,n)]=x
		d[(m,n-1)]=y
		d[(m,n)]=x+y
		return x+y
#number of sides of grids
n=20
print(Euler15(n+1,n+1))