from PIL import Image
from math import *

#opens an image:
im = Image.open("c.png").convert("RGBA")

#creates a new empty image, (base canvas)
base_image = Image.new('RGBA',(2000,2000))

def fract(n,img,base_image,size=None):
    if n == 0:
        base_image.show()
        i = input("Save?")
        if i == "y":
            file_name = input("Input File Name:")
            base_image.save(file_name+".png")                     
    else:
         
        t = n / 50 / 3.14
        x = int((1 + 10 * t) * cos(t))
        y = int((1 + 10* t) * sin(t))
        
        #img=Image.eval(im,lambda f: f+(x+y)/30)

        #paste the image at location x,y:(add int for oanvas offset
        img.thumbnail((size,size),Image.ANTIALIAS)
        base_image.paste(img,(x+500,y+500),img)
        fract(n-1,img.rotate(10),base_image,size-20)
    
fract(100,im,base_image,2000)

    
    
