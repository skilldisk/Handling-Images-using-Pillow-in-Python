from PIL import Image

with Image.open('../img/edu.jpg') as img:
    new_img = img.convert('CMYK')
    new_img.save('../output/edu.pdf')
    new_img.save('../output/edu_cmyk.jpg')