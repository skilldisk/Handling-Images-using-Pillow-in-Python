from math import sin, pi, cos
from PIL import Image, ImageDraw

images = []
r_points = []
y_points = []
b_points = []
str_points = []
teta = 0

for i in range(30):
    line_base = Image.new('RGBA', (500,500), '#000000ff')

    d = ImageDraw.Draw(line_base)

    x = int(20 + (teta*50))
    r_y = 500 - int((sin(teta)*150)+250)
    y_y = 500 - int((sin(((4*pi)/3)+teta)*150)+250)
    b_y = 500 - int((sin(((2*pi)/3)+teta)*150)+250)

    r_points.append((x,r_y))
    y_points.append((x,y_y))
    b_points.append((x,b_y))
    str_points.append((x,250))

    d.line(r_points, fill='red', width=2)
    d.line(y_points, fill='yellow', width=2)
    d.line(b_points, fill='blue', width=2)
    d.line(str_points, fill='white', width=1)

    
    images.append(line_base)

    teta += (3*pi)/30


for _ in range(5):
    images.append(images[-1])
    
images[0].save('sinewave.gif',
        save_all = True, append_images = images[1:], 
        optimize = False, duration = 400, loop=0)
    

