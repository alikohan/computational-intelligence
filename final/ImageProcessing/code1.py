from PIL import Image
import math


def convert(pixels, width, height, type):
    type = type.upper()
    if not (type == "GRAYSCALE" or type == "BLACKANDWHITE"):
        print("wrong type!")
        return
    for i in range(width):
        for j in range(height):
            # value = int(math.sqrt((pixels[i, j][0]) ** 2 + (pixels[i, j][1]) ** 2 + (pixels[i, j][2]) ** 2) * 255/ 441)
            value = int((pixels[i, j][0] + pixels[i, j][1] + pixels[i, j][2]) / 3)
            # for grayscale
            if type == "GRAYSCALE":
                pixels[i, j] = (value, value, value) # Set the RGB channels value of the image (tuple)
            # for black and white
            if type == "BLACKANDWHITE":
                if value & 128: # if value >= 128:
                    pixels[i, j] = (255, 255, 255) # Set the RGB channels value of the image (tuple)
                else:
                    pixels[i, j] = (0, 0, 0) # Set the RGB channels value of the image (tuple)

def mse(pixels1, width1, height1, pixels2, width2, height2): # Mean Squared Error
    sum = 0 # sum of distance between pixels
    if not (width1 == width2 and height1 == height2):
        print("images width and height aren't equal")
        return
    for i in range(width1):
        for j in range(height1):
            sum += (pixels1[i, j][0] - pixels2[i, j][0]) ** 2
            sum += (pixels1[i, j][1] - pixels2[i, j][1]) ** 2
            sum += (pixels1[i, j][2] - pixels2[i, j][2]) ** 2
    return sum / (width1 * height1)



image = Image.open('original.jpg') # Can be many different formats.
pixels = image.load()
convert(pixels, image.width, image.height, "blackandwhite")
image.save('blackandwhite.png') # Save the modified pixels as .png or .jpg or ...
# image.convert("1").save("new.png") # P for 8bit pixels (for RGB)

image1 = Image.open('original.jpg')
image2 = Image.open('original-compressed.jpg')
pixels1 = image1.load()
pixels2 = image2.load()
print(mse(pixels1, image1.width, image1.height, pixels2, image2.width, image2.height))