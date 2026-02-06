units=[190,100,200,300,334,70,50,400,450,10,110]
discount = [i // 1.2 if i > 200 else i // 1.1 for i in units]
print(discount)