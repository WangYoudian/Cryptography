alphabet = ['A','T','C','G']
seq = "GAATTCGCGGCCGCAATTAACCCTCACTAAAGGGATCTCTAGAACT"

trans_seq = ""
for i in range(len(seq)):
	trans_seq += alphabet[alphabet.index(seq[i])]
print(trans_seq)
print("Here are the Affine Cipher codes")

A = [1,3]
B = [1,2,3,4]
for i in range(len(A)):	
	for j in range(len(B)):
		test = ""
		for m in range(len(seq)):
			test += alphabet[(A[i]*alphabet.index(seq[m])+B[j])%4]
		print(test)