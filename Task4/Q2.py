#This is a program to accept a string from the user and display characters, that are present at an even index number.

str = input("Enter a string ")
index = 0
for i in range(0, len(str)-1, 2):
    print("index[", i, "]", str[i])



