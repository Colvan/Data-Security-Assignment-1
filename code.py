from PIL import Image
import PIL
import numpy as np
imC = Image.open('1.jpeg').convert('RGB')
imB = Image.open('2.jpeg').convert('1')
# Split into 3 channels
r, g, b = imC.split()


#bpixel
pixels = list(b.getdata())
width, height = b.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
#binary blue channel
b_arr = [[bin(col)[2:].zfill(8) for col in row ] for row in pixels]



#rpixel
pixels = list(r.getdata())
width, height = r.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
#binary red channel
r_arr = [[bin(col)[2:].zfill(8) for col in row ] for row in pixels]



#gpixel
pixels = list(g.getdata())
width, height = g.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
#binary green channel
g_arr = [[bin(col)[2:].zfill(8) for col in row ] for row in pixels]



#binarypixel
pixels = list(imB.getdata())
width, height = imB.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
#binary channel
binary_arr = [[bin(col)[2:].zfill(8) for col in row ] for row in pixels]



#XOR 
for i in range(len(binary_arr)):
    for j in range(len(binary_arr[i])):
        x=(int(binary_arr[i][j][7]) ^ int(r_arr[i][j][7]))
        if(not(x)):
            y=1 ^ int(g_arr[i][j][7])
            if(not(y)):   
                pixel = list(b_arr[i][j])
                pixel[7] = '1'
                pixel = ''.join(pixel)
                b_arr[i][j]=pixel   
            else:
                pixel = list(b_arr[i][j])
                pixel[7] = '0'
                pixel = ''.join(pixel)
                b_arr[i][j]=pixel
        else:
            y=0 ^ int(g_arr[i][j][7])
            if(y):
                pixel = list(b_arr[i][j])
                pixel[7] = '0'
                pixel = ''.join(pixel)
                b_arr[i][j]=pixel
            else:
                pixel = list(b_arr[i][j])
                pixel[7] = '1'
                pixel = ''.join(pixel)
                b_arr[i][j]=pixel


print(b_arr[0][0])
print(b_arr[0][1])

#print(type(b_arr[0]))
#new_b = list(map(lambda x : int(x,2),b_arr))
new_b = [[int(col,2) for col in row ] for row in b_arr]
new_b=[j for i in new_b for j in i]
b.putdata(new_b)


# Recombine back to RGB image
result = PIL.Image.merge('RGB', (r,g,b))
result.save('result.png')




imCombined = Image.open('result.png').convert('RGB')


#print(np_im)

rc, gc, bc = imCombined.split()


#bpixel
pixelsC = list(bc.getdata())
width, height = bc.size
pixelsC = [pixelsC[i * width:(i + 1) * width] for i in range(height)]
#binary blue channel
b_arrC = [[bin(col)[2:].zfill(8) for col in row ] for row in pixelsC]



#rpixel
pixelsC = list(rc.getdata())
width, height = rc.size
pixelsC = [pixelsC[i * width:(i + 1) * width] for i in range(height)]
#binary red channel
r_arrC = [[bin(col)[2:].zfill(8) for col in row ] for row in pixelsC]


#gpixel
pixelsC = list(gc.getdata())
width, height = gc.size
pixelsC = [pixelsC[i * width:(i + 1) * width] for i in range(height)]
#binary green channel
g_arrC = [[bin(col)[2:].zfill(8) for col in row ] for row in pixelsC]



#y = 1 ^ int(r_arrC[0][0][7])
#print("y",y)
binary_image_arr = []
#XOR 

for i in range(len(b_arrC)):
    for j in range(len(b_arrC[i])):
        x=(int(b_arrC[i][j][7]) ^ int(g_arrC[i][j][7]))
        if(not(x)):
            y=1 ^ int(r_arrC[i][j][7])
            if(not(y)):  
                binary_image_arr.append(True)
            else:   
                binary_image_arr.append(False)
        else:
            y=0 ^ int(r_arrC[i][j][7])
            if(y):
                binary_image_arr.append(True)
            else:
                binary_image_arr.append(False)





binary_image_arr=binary_image_arr[:128*128]
nimg=PIL.Image.new('1',(128,128))
nimg.putdata(binary_image_arr)
#nimg.show()
#image=PIL.Image.fromarray(binary_image_arr)
#image.save('NewBinaryResult.png')
#image.show()
