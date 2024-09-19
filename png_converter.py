from os import path
from PIL import Image

image_name = 'Rickroll.jpg'
scale = 16


current_directory = path.dirname(path.abspath(__file__))
file_path = path.join(current_directory, "images/" + image_name)
im = Image.open(file_path)
im.thumbnail((im.size[0]/scale, im.size[1]/scale), Image.Resampling.LANCZOS)
size = im.size
pix = im.load()

printlist = []

def conv(value:int):
    return(f'{value:08b}')

printlist.append(conv(size[0]))
printlist.append(conv(size[1]))
printlist.append('00011000')

for y in range(size[1]):
    for x in range(size[0]):
        pixelvalue = conv(pix[x,y][0])
        pixelvalue += conv(pix[x,y][1])
        pixelvalue += conv(pix[x,y][2])
        printlist.append(pixelvalue)

file_path = path.join(current_directory, "output.txt")
output = open(file_path, "w")
output.write(''.join(printlist))

print("Done")