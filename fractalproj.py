from PIL import Image, ImageDraw
from math import *

#opens an image:


#creates a new empty image, (base canvas)
base_image = Image.new('RGBA',(2000,2000))

im = Image.open("/home/oem/Desktop/bellco-feedback/t.jpg")

def rotate_point_clockwise(x1,y1,x2,y2,degrees):
    new_x = (x2 - x1)*cos(degrees * pi / 180) - (y2 - y1)*sin(degrees * pi / 180)+x1
    new_y = (y2 - y1)*sin(degrees * pi / 180) + (x2 - x1)*cos(degrees * pi / 180)+y1
    return (new_x,new_y)

def rotate_point_counter(x1,y1,x2,y2,degrees):
    new_x = (x2 - x1)*cos(degrees * pi / 180)+(y2 - y1)*sin(degrees * pi / 180)+x1
    new_y = (y2 - y1)*sin(degrees * pi / 180)-(x2 - x1)*cos(degrees * pi / 180)+y1
    return (new_x,new_y)

def octo_fractal(loops,x,y,nx,ny,flip = True):
    draw = ImageDraw.Draw(im)
    if loops == 0:    
        draw.line((x,y,nx,ny),fill=(int(y),int(x-y),int(y+-x)))
    else:

        #succesfully finds first 3rd
        midp1 = ((nx-x)/2/2+x,(ny-y)/2/2+y)
        midp2  = (((nx-x)/4)+x,((ny-y)/4)+y)

        #rotate cordinates
        if flip == True:        
            new_x1, new_y1 =rotate_point_counter(x,y,midp1[0],midp1[1],45)
            new_x2, new_y2 =rotate_point_clockwise(nx,ny,midp2[0],midp2[1],45)
        else:
            new_x1, new_y1 =rotate_point_clockwise(x,y,midp1[0],midp1[1],45)
            new_x2, new_y2 =rotate_point_counter(nx,ny,midp2[0],midp2[1],45)

        octo_fractal(loops-1,x, y, new_x1, new_y1,flip = not flip)
        octo_fractal(loops-1,new_x1,new_y1,new_x2,new_y2,flip =  flip)
        octo_fractal(loops-1,nx, ny, new_x2, new_y2, flip =  flip)

    
   
octo_fractal(11,0,im.size[1]-50,im.size[0],im.size[1]-50,flip=True)

im.save("/home/oem/Desktop/bellco-feedback/test.png", "PNG")

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
        
        #img=Image.eval(im,lambda f: f+(x+y)/30n


        #paste the image at location x,y:(add int for nx = x+ size*sign
            
        img.thumbnail((size,size),Image.ANTIALIAS)
        base_image.paste(img,(x+500,y+500),img)
        fract(n-1,img.rotate(10),base_image,size-20)
    
#fract(100,base_image,base_image,2000)


    
    
