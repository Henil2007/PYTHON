import qrcode

url = input("ENter text or url : ")

img = qrcode.make(url)

img.save('qrcode.png')
print("qrcode created sucessfully")