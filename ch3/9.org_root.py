# coding_utf-8
# to verify whether n is or not a original root of k
#百度了一下,发现一个性质,就是一个数的原根个数就是phi[phi[n]],而此题n是素数,phi[n]=n - 1;
#所以直接输出phi[n - 1]就行了
import sys
a = 3
k = 65537

test = set()
for p in range(1,k):
	res = (a**p)%k
	if res in test:
		print("You input the wrong number")
		sys.exit()
	else:
		test.add(res)
	#print(test)
print("Verification completed!")