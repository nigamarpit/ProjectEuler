def Euler13(n):
	f=open('Input13.txt','r')
	l=list()	
	for line in f:
		l.append(int(line.strip()))
	return int(''.join(list(str(sum(l)))[:n]))

#first n digits of sum
n=10
print(Euler13(n))
