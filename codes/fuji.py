import PIL.Image as im
import numpy as np

image = im.open('fuji1.png')    # load image data from file
nx, ny = image.size
pixels = image.load()
blue = np.zeros((nx,ny),dtype=int)
for i in range(0,nx):
    for j in range(0,ny):
        blue[i,j] = pixels[i,j][2]

gr = np.gradient(blue)   # use only the blue band for edge detection
gradientNormSquared = gr[0]**2 + gr[1]**2
for i in range(0,nx):
    for j in range(0,ny):
        value = 255 - min(int(gradientNormSquared[i,j]),255)
        pixels[i,j] = (value, value, value)

image.show()    # display image
