import qrcode

url = input("enter ur url : ")
filename = input("enter the file name u want : ")

if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)

print("QR Code Generated Successfully!")