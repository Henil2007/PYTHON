#empty list
x = []
print(x)
print(type(x))

users =["ram","arjun","krishna","sudama","bhim","ram"]
print(users)

print(users[0])

# range loop
# for i in range(0,len(users)):
#     print(users[i])

# using for each loop
for i in users:
    print(i)

users[1] = "Arjuna"
print(users)