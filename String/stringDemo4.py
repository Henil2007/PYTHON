name = "Java"
index = None
char = input("Enter character you want to search : ")
for i in range(0,len(name)):
    if(name[i] == char):
        index = i
        break

print(index)