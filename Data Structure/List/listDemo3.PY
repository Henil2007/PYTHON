marks = [90,87,65,99,79,81]
print(marks)

deleteElement = marks.pop()
print(f"removed Element is : {deleteElement}")
print(marks)

deleteElement = marks.pop(3)
print(f"Removed element is : {deleteElement}")
print(marks)

marks = [90,87,65,99,87,79,81]
marks.remove(87)
print(marks)