import numpy as np 

def main():
	row, col = [int(x) for x in input("Please input the row and colomn number:").split()]
	res = np.zeros((row, col))
	inv_mode = np.zeros((row, col))
	print("Input the mode number")
	M = int(input())
	res = get_value(res)
	inv_mode = inv_matrix_dot(res, inv_mode)
	print_matrix(res, inv_mode, M)

def get_value(res):
	print("Please input the value of matrix:"+'\n'+"from left to right, up and dowm")
	for i in range(len(res)):
		for j in range(len(res[0])):
			res[i][j] = int(input())
	return res

def inv_matrix_dot(res, inv):
	inv = np.linalg.inv(res)
	return inv

def print_matrix(org, inv, M):
	print(org)
	det = np.linalg.det(org)
	print("The Determinat of the input matrix is:{}".format(det))
	print("Its true value is:{}".format(round(det)))
	print("And the int type of inverse matrix is:")
	print(det*inv)
	m = func_mode(round(det), M)
	print(m*det*inv)
	result = trim(m*det*inv, M)
	print("The result for the problem is:")
	print(result)

def func_mode(k, M):
	i = 1
	while True:
		if k*i % M == 1:
			return i
		else:
			i+=1

def trim(mode_matrix, M):
	for i in range(len(mode_matrix)):
		for j in range(len(mode_matrix[0])):
			if mode_matrix[i][j]<0:
				while(mode_matrix[i][j]<0):
					mode_matrix[i][j]+=M
			if mode_matrix[i][j]>=M:
				while(mode_matrix[i][j]>=M):
					mode_matrix[i][j]-=M
	return mode_matrix

if __name__=='__main__':
	main()