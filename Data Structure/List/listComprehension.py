#single line code...
users = ["ram","shyam","amit","sumit","jaya","divya"]

#uppercase

uppercase = []
for i in users:
    uppercase.append(i.upper())
print(uppercase)

# Comprehension version
uppercase1 = [i.upper() for i in users]
print(uppercase1)

# initial letter

users = ["ram","shyam","amit","sumit","jaya","divya"]
usersInitial = []
for i in users:
    usersInitial.append(i[0])
print(usersInitial)

#comprehension version
usersInitial1 = [i[0] for i in users]
print(usersInitial1)

#numric
sales = [100,200,300,400,500,600,700] 
#10...
# sales1 = [110,210]
sales1 = []
for i in sales:
    sales1.append(i+10)
print(sales1)

#comprehensive version
sales2 = [i+10 for i in sales]
print(sales2)