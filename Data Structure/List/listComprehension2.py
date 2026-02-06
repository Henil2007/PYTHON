users = ["ram","shyam","amit","sumit","geeta","jaya","rama"]

# filteruser = []

# for i in users:
#     if len(i) > 4:
#         filteruser.append(i)
# print(filteruser)

filterUsers = [i for i in users if len(i) > 4]
print(filterUsers)

users = ["ram","shyam","amit","sumit","naman","geeta","jaya","rama","bob"]
#label =["no",nom=,no....]

filteruser2 = ["yes" if i == i[::-1] else "No" for i in users]
print(filteruser2)

numbers = [-100,100,0,20,0,-90,98,97,67,-32]
numberlable = ["Pos" if i > 0 else "Neg" for i in numbers]
print(numberlable)

sales= [100,20,45,67,89,120,89,78]
sales50 =[i for i in sales if i>50]
print(sales50)
evenoddsalses = ["even" if i %2 ==0 else "odd" for i in sales]
#evenoddsalses = ["even" if i %2 ==0 else "odd" for i in sales if i>50]
print(evenoddsalses)