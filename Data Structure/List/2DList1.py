data =[[1,2,3],[4,5,6],[7,8,9]] #3*3
#3 rows 3 columns

# print(data[0])
# print(data[1])
# print(data[2])

# for i in range(0,len(data)):
#     print(data[i])

# print(data[0][0])
# print(data[0][1])
# print(data[2][0])

for i in range(0,len(data)):
    for j in range(0,len(data[i])):
        print(data[i][j],end=" ")
    print()

#for each member
for i in data:
    for j in i:
        print(j,end=" ")
    print()