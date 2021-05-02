from PIL import Image


img = Image.open('../img/black_1.jpeg')

print('*'*10)
print('Image Format: ', img.format)
print('Mode: ', img.mode)
print('Size: ', img.size)
print('*'*10)


#  To print Data use list method
print(list(img.getdata()))

img.close()


# Use it close the file safely
# with Image.open('../output/black_1.jpeg') as img:

