import numpy as np

a = int(input("Enter the size of array:"))
print()

array1 = []
print("Enter the elements of first array")
for i in range(a):
    array1.append(float(input("Element:")))
array1 = np.array(array1)
print()

print("First array:")
print(array1)
print()

array2 = []
print("Enter the elements of second array")

for i in range(a):
    array2.append(float(input("Element:")))
array2 = np.array(array2)
print()

print("Second array:")
print(array2)
print()

array_equal = np.allclose(array1, array2)
print(array_equal)