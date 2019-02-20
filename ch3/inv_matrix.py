import numpy as np 

def main():
	row, col = [int(x) for x in input("Please input the row and colomn number:").split()]
	res = np.zeros((row, col))
	inv = np.zeros((row, col))
	res = get_value(res)
	inv = inv_matrix(res, inv)
	print_matrix(res, inv)

def get_value(res):
	print("Please input the value of matrix:"+'\n'+"from left to right, up and dowm")
	for i in range(len(res)):
		for j in range(len(res[0])):
			res[i][j] = int(input())
	return res

def inv_matrix(res, inv):
	inv = np.linalg.inv(res)
	return inv

def print_matrix(org, inv):
	print(org)
	det = np.linalg.det(org)
	print("The Determinat of the input matrix is:{}".format(det))
	print("And the int type of inverse matrix is:")
	print(det*inv)

if __name__=='__main__':
	main()

'''
矩阵求逆
'''