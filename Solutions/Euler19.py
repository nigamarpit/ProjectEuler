d={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def CountingSundays():
	Sundays1900=0
	countSundays=0
	days=0
	for i in range(1900,2001):
		for j in range(1,13):
			if (days+1)%7==0:
				if i==1900:
					Sundays1900+=1
				countSundays+=1
			if j==2:
				if i%4==0:
					if i%100==0:
						if i%400==0:
							days+=29
						else:
							days+=28
					else:
						days+=29
				else:
					days+=28
			else:
				days+=d[j]
	return countSundays-Sundays1900

print("Number of Sundays falling on first of month: "+str(CountingSundays()))

'''
1 Jan
2 Feb
3 Mar
4 Apr
5 May
6 Jun
7 Jul
8 Aug
9 Sep
10 Oct
11 Nov
12 Dec
'''