from math import sin, cos, pi
from PIL import Image, ImageDraw

base = Image.new('RGBA', (1000,1000), 'black')

d = ImageDraw.Draw(base)


d.ellipse((250,250,650,650), fill='blue', outline='red', width=5)
base.show()




# # using Line method
# point_list = []

# teta = 0
# no_points = 360


# delta_teta = 2*pi / no_points

# for i in range(no_points+1):
#     x = 500 + 200 * sin(teta)
#     y = 500 + 200 * cos(teta)

#     point_list.append((x,y))
    
#     teta += delta_teta


# d.line(point_list, fill='red', width=5)





