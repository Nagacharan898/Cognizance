from numpy import size

def IdentityMatrix(size):
	for row in range(0, size):
		for column in range(0, size):
			if (row == column):
				print("1 ", end=" ")
			else:
				print("0 ", end=" ")
		print()

size = 3
IdentityMatrix(size)