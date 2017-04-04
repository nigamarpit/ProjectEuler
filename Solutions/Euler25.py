def fibonacciSequence():
	old=1
	current=1
	new=0
	i=2
	while True:
		i+=1
		new=old+current
		if checkLength(new):
			break
		old=current
		current=new
	return i

def checkLength(n):
	if len(str(n))==1000:
		return True
	else:
		return False

print("Index of the first term in the Fibonacci sequence to contain 1000 digits: "+str(fibonacciSequence()))