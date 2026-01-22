data = "java"

print(data[0]," - ",data[-4])
print(data[1]," - ",data[-3])
print(data[2]," - ",data[-2])
print(data[3]," -- ",data[-1])

# Simple Slicing

text = "pythonProgramming"
print(text[0:6])

#Skit start
print(text[:6])

#skip end
print(text[1:])

# Full String
# print(text[:])
x = text[:]
print(x)

# negative index

print(text[:-6])
print(text[-13:-6])
print(text[10::-1])

# step param
text = "abcdef"

print(text[::2]) # increment of 2
# output : ace

print(text[::3]) # increment of 3
print(text[::-1]) # reverse increment
# output : fedcba