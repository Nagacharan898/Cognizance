import numpy as np
print()
vector = np.array([10,11,12,13,14])
print("Original vector is")
print(vector)
print()
z=5     # z is no. of zeroes
new_vector = np.zeros(len(vector) + (len(vector)-1)*(z))
new_vector[::z+1] = vector
print("New vector is")
print(new_vector)