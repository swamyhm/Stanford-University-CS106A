"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    # TODO: your code here
    #for pixel in image:
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            R = pixel.red
            B = pixel.blue
            G = pixel.green
            pixel.red = (R * 1.5)
            pixel.blue = (B * 1.5)
            pixel.green = (G * 0.7)
    # Show the image after the transform
    image.show()
    

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == 'DEFAULT_FILE':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()