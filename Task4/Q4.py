#This is a program to check whether the given number is a palindrome number.

n = int(input("Enter number:"))
temp = n
reverse = 0
while (n > 0):
    s = n % 10
    reverse = reverse * 10 + s
    n = n // 10
if (temp == reverse):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")