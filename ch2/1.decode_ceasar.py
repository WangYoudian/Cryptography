alphabet = ['a','b','c','d','e','f','g','h','i','j','k',\
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C = "ycvejqwvhqtdtwvwu"

for i in range(26):
	temp = ''
	for j in range(len(C)):		
		temp+=alphabet[(alphabet.index(C[j])+i)%26]
	print(temp)
