l=list()
def Euler11(n):
	f=open('Input11.txt','r')

	for line in f:
		l.append(list(map(int,line.split())))
	#print(l)
	m=0
	for i in range(20):
		for j in range(20):
			#right
			p=rightProduct(i,j)
			if p>m:
				m=p
			#bottom
			p=bottomProduct(i,j)
			if p>m:
				m=p
			#right diagonal
			p=rightDiagonalProduct(i,j)
			if p>m:
				m=p
			#left diagonal
			p=leftDiagonalProduct(i,j)
			if p>m:
				m=p
	return m

def rightProduct(i,j):
	if j>16:
		return 0
	return l[i][j]*l[i][j+1]*l[i][j+2]*l[i][j+3]
	

def bottomProduct(i,j):
	if i>16:
		return 0
	return l[i][j]*l[i+1][j]*l[i+2][j]*l[i+3][j]

def rightDiagonalProduct(i,j):
	if i>16 or j>16:
		return 0
	return l[i][j]*l[i+1][j+1]*l[i+2][j+2]*l[i+3][j+3]

def leftDiagonalProduct(i,j):
	if i>16 or j<4:
		return 0
	return l[i][j]*l[i+1][j-1]*l[i+2][j-2]*l[i+3][j-3]

n=4 #continous numbers in grid
print(Euler11(n))