from PIL import Image, ImageDraw, ImageFilter

base = Image.new('RGBA', (1000,1000), 'black')

#  intiate draw instance
d = ImageDraw.Draw(base)

# Draw frame with padding of 20px
d.rectangle([(20,20), (980,980)], fill="#2a2a2aff")

# Draw Moon at top left
d.ellipse([(100,100), (300,300)], fill='white')


# Draw mountain-1
points = [(500,980), (750,300), (900,500), (980,800), (980,980)]
d.polygon(points, fill='#00aa00',outline='black' )


# Draw mountain-2
points = [(20,980), (20,800), (450,500), (500,500), (700,980)]
d.polygon(points, fill='#00aa00',outline='black' )

# base.show()
x=base.convert('L')
x.show()
x.filter(ImageFilter.FIND_EDGES() ).show()