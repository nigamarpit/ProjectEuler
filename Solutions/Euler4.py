#Largest palindrome product
import math
def Euler4():
	n=-math.inf
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			t=i*j
			if checkPalindrome(t) and t>n:
				n=t
	return n

def checkPalindrome(num):
	s=str(num)
	for i in range(len(s)//2):
		if s[i]!=s[len(s)-i-1]:
			return False
	return True

print(Euler4())