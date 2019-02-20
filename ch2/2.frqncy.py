alphabet = ['a','b','c','d','e','f','g','h','i','j','k',\
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C = "lcllewljazlnnzmvyiylhrmhza"
d = dict()
#calculate the frequency of each character in string
for i in range(len(C)):
	if C[i] in d:
		count=d[C[i]]
	else:
		count=0
	count=count+1
	d[C[i]]=count

print(d)