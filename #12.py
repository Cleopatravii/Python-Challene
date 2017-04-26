im=open('evil2.gfx','rb').read()
for i in range(0,5):
    open('image' +str(i), 'wb').write(im[i::5])
