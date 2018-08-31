from PIL import Image

img = Image.open('sunset.jpeg')

def tint(pixelTuple):
    px = pixelTuple.load()
    for i in range(pixelTuple.width):
        for j in range(pixelTuple.height):
            rgb = px[i, j]
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            gray = int(((r + g + b)/3)* 1.5)
            pixelTuple.putpixel((i, j), (0, 0, gray))
    pixelTuple.show()
    pixelTuple.save('blue.jpeg')


tint(img)
