d = [[1, ' ', 0],
     [2, ' ', 0],
     [3, ' ', 0]]
#This for loop is used to collect names of the students
for i in range(3):
     for j in range(1):
        d[i][j+1]=(input("Enter the name of student {0} : ".format( int(i+1))))

#This for loop is used to collect marks of the students
for i in range(3):
     for j in range(1):
        d[i][j+2]=(input("Enter the marks of student {0} : ".format( int(i+1))))
print()
print("{:<10} {:<10} {:<10}".format('Roll no','Name','Marks') )

for v in d:
    for c in v:
        print(c,end=' '*10)
    print()
#This is used to extract the second row/record from the created list
print("From created list, the second row is : ", d[1][0], d[1][1], d[1][2])