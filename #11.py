import Image
im=Image.open('cave.jpeg')
img=Image.new('RGB',(640,480),'black')
pixell=img.load()
for x in range(640):
    for y in range(480):
        if (x+y)%2==0:
            pixell[x,y]=im.getpixel((x,y))
img.show()            
