def countstrings(a,b):
	if a== 0:
		return 1
	cnt = 0
	for i in range(b, 5):
		cnt += countstrings(a - 1, i)
	return cnt
	
def countVowelStrings(a):
	return countstrings(a, 0)

a = 2
print(countVowelStrings(a))
a= 1
print(countVowelStrings(a))
a= 33
print(countVowelStrings(a))
a = 55
print(countVowelStrings(a))
a = 52
print(countVowelStrings(a))
