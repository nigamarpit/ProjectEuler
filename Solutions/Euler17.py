#Number letter count
d=dict()
d[0]=''
d[1]='One'
d[2]='Two'
d[3]='Three'
d[4]='Four'
d[5]='Five'
d[6]='Six'
d[7]='Seven'
d[8]='Eight'
d[9]='Nine'
d[10]='Ten'
d[11]='Eleven'
d[12]='Twelve'
d[13]='Thirteen'
d[14]='Fourteen'
d[15]='Fifteen'
d[16]='Sixteen'
d[17]='Seventeen'
d[18]='Eighteen'
d[19]='Nineteen'
d[20]='Twenty'
d[30]='Thirty'
d[40]='Forty'
d[50]='Fifty'
d[60]='Sixty'
d[70]='Seventy'
d[80]='Eighty'
d[90]='Ninety'
d[100]='hundred'
d[1000]='thousand'

def countLetters(n):
	s=''
	x=str(n)
	if len(x)>2:
		s+=d[int(x[0])]+'Hundred'
		if int(x[1:])==0:
			return s
		else:
			s+='And'
			if int(x[1:])>19:			
				s+=greater19(int(x[1:]))
			else:
				s+=d[int(x[1:])]
	else:
		if int(x)>19:
			s+=greater19(int(x))
		else:
			s=d[int(x)]
	return s 

def greater19(n):
	s=d[(n//10)*10]
	s+=d[n%10]
	return s

c=0
for i in range(1,1000):
	l=countLetters(i)
	print(l)
	c+=len(l)
#print(countLetters(115))
#print(len(countLetters(115)))
c+=len('onethousand')
print(c)