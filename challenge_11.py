from PIL import Image ,ImageDraw

im = Image.open("cave.jpg")

w = im.width
h =im.height

hidden = Image.new('RGB', (w//2, h//2)) # Image.new('RGB', (w // 2, h // 2)) : 너비 w // 2와 높이 h // 2를 가진 새로운 RGB 색상 모드의 이미지 객체를 생성합니다. 

for i in range(w):
  for j in range(h):
    im_p = im.getpixel((i,j))
    if i+j %2 !=0:
      hidden.putpixel((i//2,j//2),im_p)
  
hidden.show()
