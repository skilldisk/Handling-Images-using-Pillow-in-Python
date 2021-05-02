from PIL import Image, ImageDraw

with Image.open('../img/color_RGB.jpeg') as img:

    # Create a drawing instance
    d = ImageDraw.Draw(img)

    d.ellipse((10,10,90,90), fill='white')

    img.save('../output/circle.jpeg')