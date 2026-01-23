users =["ram","arjun","krishna","sudama","bhim","ram"]
print(users)

users.append("sahadev")
print(users)

users.insert(3,"yudhistir")
print(users)

tobeadded = ["draupadi","subhdra","kunti"]
users.extend(tobeadded) 
users.extend(["dhuryodhan"])
print(users)

users.extend("bhishm")
print(users)