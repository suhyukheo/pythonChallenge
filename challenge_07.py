from PIL import Image
from urllib.request import urlopen

pic = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
image = Image.open(pic)
pixels =[]
for i in range(0,image.width):
  pixels.append(image.getpixel((i,image.height/2)))
pixels = pixels[::7]
for i in pixels:
  print(chr(i[0]),end="")
print("\n")


ret =[105, 110, 116, 101, 103, 114, 105, 116, 121]

for i in ret:
  print(chr(i),end="")