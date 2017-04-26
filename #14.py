import Image
im=Image.open('wire.png')
l=[]
for i in range(10000):
    l.append(im.getpixel((i,0)))
print len(l)    
