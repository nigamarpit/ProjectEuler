import itertools as it
def lexicographicPermutations():
	l=list(range(10))
	r=[''.join(map(str,x)) for x in list(it.permutations(l))]
	#print(len(r))
	print("Millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9: "+r[999999])
lexicographicPermutations()