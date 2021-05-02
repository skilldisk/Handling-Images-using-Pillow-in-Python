from PIL import Image

# Mode of the image ( '1', 'L', 'RGB', 'RGBA', 'CMYK' ..etc )
mode = '1'

# Size interms of (x,y)
size = (10, 10)

######### Colors #########
#   0 for Black | 1 for White in Mode '1'
#   0 or #000000 for Black | 255 or #ffffff for white | 'L'
#   (0,0,0) or #000000 for Black | (255,255,255) or #ffffff for White | 'RGB'
#   (0,0,0,255) or #000000ff for Black | (255,255,255,255) or #ffffffff for White | 'RGBA'
#   CSS color names can also be used
color = 0

new_image = Image.new(mode, size, color)

new_image.save('../output/black_10x10.jpeg')
