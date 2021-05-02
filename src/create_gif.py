from math import sin, pi, cos
from PIL import Image, ImageDraw

# with Image.open('../static/assets/base.png') as base:
images = []
circle_points = []

teta = 0
no_points = 30


delta_teta = 2*pi / no_points

for i in range(no_points+1):
    line_base = Image.new('RGBA', (500,500), '#000000ff')

    d = ImageDraw.Draw(line_base)
    x = 250 + 200 * sin(teta)
    y = 250 + 200 * cos(teta)

    circle_points.append((x,y))

    d.line(circle_points, fill='red', width=2)
    
    images.append(line_base)

    teta += delta_teta


for _ in range(3):
    images.append(images[-1])
    
images[0].save('draw_circle.gif',
        save_all = True, append_images = images[1:], 
        optimize = False, duration = 100, loop=0)