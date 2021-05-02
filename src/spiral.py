from math import sin, cos, pi
from PIL import Image, ImageDraw

no_circle = 500

x_start = 500
y_start = 500

radius = 5

cir_radius = 2

no_spirals = 10

spiral_color = 'white'


# Open a Base Image
with Image.open('../img/base.png') as base:

    # create a transparent base for adding circles.
    spiral_base = Image.new('RGBA', base.size, '#ffffff00')

    spiral = ImageDraw.Draw(spiral_base)

    teta = 0
    del_teta = (no_spirals*2*pi) / no_circle

    for i in range(no_circle):

        x = (radius * teta) * (cos(teta))
        y = (radius * teta) * (sin(teta))

        rad = cir_radius + (i*0.005) 

        spiral.ellipse([x_start+x, y_start+y, x_start+x+rad, y_start+y+rad], fill=spiral_color)

        teta += del_teta

    out = Image.alpha_composite(base, spiral_base)

    out.show()