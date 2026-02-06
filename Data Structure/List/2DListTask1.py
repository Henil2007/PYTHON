players =[["Virat",100,121,89],["Rohit",100,67,56]]
#print both player name
#print virat score 
#Print virat score total
#print rohit score total
#print total score by both player

name = []
# for i in players:
#     for j in i:
#         if(type(j) == str):
#             print(j,end=" ")
# for i in players:
#     for j in i:
#         if i[0] == "Virat" and type(j) == int:
#             print(j)
# sum = 0
# for i in players:
#     for j in i:
#         if i[0] == "Virat" and type(j) == int:
#             sum = sum + j
            # print(j,end=" ")
# print(sum)
sum = 0
for i in players:
    for j in i:
        if i[0] == "Rohit" and type(j) == int:
            sum = sum + j
            # print(j,end=" ")
print(sum)

total = 0
for i in players:
    for j in i:
        if(type(j) == int):
            total = total + j
print(total) 