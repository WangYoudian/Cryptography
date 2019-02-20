alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
P = "hust"

C = ""
for i in range(len(P)):
	C+=alphabet[(3*alphabet.index(P[i])+7)%26]

print(C)