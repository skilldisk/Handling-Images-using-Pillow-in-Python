from PIL import Image

with Image.open('../img/black_10x10.jpeg') as img:
    
    pixel = img.getpixel((5,5))

    print(pixel)





# #  get the size of image
# size = img.size

# # Fill White in alternate pixels
# for x in range(size[0]):
#     for y in range(size[1]):
#         if (x%2 and y%2) or (x%2==0 and y%2==0):
#             img.putpixel((x,y),255)
# img.save('../output/pixel.jpeg')