from PIL import Image
imC = Image.open('1.jpeg').convert('RGB')
imB = Image.open('2.jpeg').convert('1')
# Split into 3 channels
r, g, b = imC.split()


#bpixel
pixels = list(b.getdata())
width, height = b.size
#binary blue channel
b_arr = [bin(col)[2:].zfill(8) for col in pixels]

#rpixel
pixels = list(r.getdata())
width, height = r.size
#binary red channel
r_arr = [bin(col)[2:].zfill(8) for col in pixels ]



#gpixel
pixels = list(g.getdata())
width, height = g.size
#binary green channel
g_arr = [bin(col)[2:].zfill(8) for col in pixels ]



#binarypixel
pixels = list(imB.getdata())
width, height = imB.size
#binary channel
binary_arr = [bin(col)[2:].zfill(8) for col in pixels ]

# print(r_arr[127])
# print(g_arr[127])
# print(b_arr[128])
# print(binary_arr[127])

#XOR 
for i in range(len(binary_arr)):
        x=(int(binary_arr[i][7]) ^ int(r_arr[i][7]))
        if(not(x)):
            y=1 ^ int(g_arr[i][7])
            if(not(y)):   
                pixel = list(b_arr[i])
                pixel[7] = '1'
                pixel = ''.join(pixel)
                b_arr[i]=pixel   
            else:
                pixel = list(b_arr[i])
                pixel[7] = '0'
                pixel = ''.join(pixel)
                b_arr[i]=pixel
        else:
            y=0 ^ int(g_arr[i][7])
            if(y):
                pixel = list(b_arr[i])
                pixel[7] = '0'
                pixel = ''.join(pixel)
                b_arr[i]=pixel
            else:
                pixel = list(b_arr[i])
                pixel[7] = '1'
                pixel = ''.join(pixel)
                b_arr[i]=pixel





new_b = [int(col,2) for col in b_arr ]
b.putdata(new_b)
# Recombine back to RGB image
result = Image.merge('RGB', (r,g,b))
result.save('result.png')




imCombined = Image.open('result.png')

rc, gc, bc = imCombined.split()


#bpixel
pixelsC = list(bc.getdata())
widthC, heightC = bc.size
#binary blue channel
b_arrC = [bin(col)[2:].zfill(8) for col in pixelsC]



#rpixel
pixelsC = list(rc.getdata())
widthC, heightC = rc.size
#binary red channel
r_arrC = [bin(col)[2:].zfill(8) for col in pixelsC]


#gpixel
pixelsC = list(gc.getdata())
widthC, heightC = gc.size
#binary green channel
g_arrC = [bin(col)[2:].zfill(8) for col in pixelsC]




binary_image_arr = []
#XOR 

for i in range(len(b_arrC)):
        x=(int(b_arrC[i][7]) ^ int(g_arrC[i][7]))
        if(not(x)):
            y=1 ^ int(r_arrC[i][7])
            if(not(y)):  
                binary_image_arr.append(1)
            else:   
                binary_image_arr.append(0)
        else:
            y=0 ^ int(r_arrC[i][7])
            if(y):
                binary_image_arr.append(0)
            else:
                binary_image_arr.append(1)





binary_image_arr=binary_image_arr[:128*128]
nimg=Image.new('1',(128,128))
nimg.putdata(binary_image_arr)
nimg.show()
