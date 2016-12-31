#Maximum path sum I
d=dict()
l=list()
def Euler18(i=0,j=0):
	if i==len(l)-1:
		return l[i][j]
	if d.get(l[i+1][j]) and d.get(l[i+1][j+1]):
		y=l[i][j]+max(d[(i+1,j)],d[(i+1,j+1)])
		d[(i,j)]=y
		return y
	elif d.get(l[i+1][j]):
		x=Euler18(i+1,j+1)
		y=l[i][j]+max(d[(i+1,j)],x)
		d[(i,j)]=y
		d[(i+1,j+1)]=x
		return y
	elif d.get(l[i+1][j+1]):
		x=Euler18(i+1,j)
		y=l[i][j]+max(d[(i+1,j+1)],x)
		d[(i,j)]=y
		d[(i+1,j)]=x
		return y
	else:
		x=Euler18(i+1,j)
		y=Euler18(i+1,j+1)
		z=l[i][j]+max(x,y)
		d[(i+1,j)]=x
		d[(i+1,j+1)]=y
		d[(i,j)]=z
		return z	

f=open('Input18.txt','r')
for line in f:
	l.append(list(map(int,line.strip().split())))
print(l)
print(Euler18())