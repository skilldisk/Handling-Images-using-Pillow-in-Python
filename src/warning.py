from PIL import Image

# new_cmyk_img = Image.new('CMYK', (100,100), 'red')
new_cmyk_img = Image.new('L', (100,100), 'red')

new_cmyk_img.show()