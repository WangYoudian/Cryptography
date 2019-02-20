# coding:utf-8
#Euler数E(n)定义为小于n且与n互素的正整数个数
import numpy as np 

def Euler(m):
	d = set()
	for i in range(1,m):
		if np.gcd(i,m) == 1:
			d.add(i)
	return len(d)

print(Euler(231))