# coding:utf-8
#找出一个数，使得当它被101除时余17，当它被201除时余18，当它被301除时余19
a = 101
b = 201
c = 301
x = max(a,b,c)
while True:
	if(x%101==17 and x%201==18 and x%301==19):
		print("The qualified number is:{}".format(x))
		#x+=1
		break
	else:
		x+=1
