from PIL import Image

def rgb_to_grey(rgb_px):
    (r, g, b) = rgb_px
    return (r + g + b)//3

def image_to_grey_rgb(img):
    grey_values = [rgb_to_grey(rgb_color) for rgb_color in img.getdata()]
    rgb_grey_values = [(grey, grey, grey) for grey in grey_values]
    grey_img = Image.new("RGB", img.size)
    grey_img.putdata(rgb_grey_values)

    return grey_img

def image_to_grey(img):
    grey_values = [(r + g + b)/3 for (r, g, b) in img.getdata()]
    grey_img = Image.new('L', img.size)
    grey_img.putdata(grey_values)
    return grey_img

def image_to_negative(img):

    negative_values = [(255 - r, 255 - g, 255 - b) for (r, g, b) in img.getdata()]

    negative_img = Image.new('RGB', img.size)
    negative_img.putdata(negative_values)

    return negative_img

def pixel_to_sepia(rgb_pixel):
    (r, g, b) = rgb_pixel
    sepia_red = r*0.393 + g*0.769 + b*0.189
    sepia_green = r*0.349 + g*0.686 + b*0.168
    sepia_blue = r*0.272 + g*0.534 + b*0.131

    return (int(sepia_red), int(sepia_green), int(sepia_blue))

def image_to_sepia_data(img):
    sepia_values = [pixel_to_sepia(rgb_pixel) for rgb_pixel in img.getdata()]
    sepia_img = Image.new('RGB', img.size)
    sepia_img.putdata(sepia_values)

    return sepia_img

def image_to_sepia(img):
    (width, height) = img.size
    sepia_img = Image.new('RGB', img.size)

    for x in range(width):
        for y in range(height):
            pixel_position = (x, y)
            current_pixel = img.getpixel(pixel_position)
            sepia_img.putpixel(pixel_position, pixel_to_sepia(current_pixel))
    
    return sepia_img

if __name__ == "__main__":
    print("Hello grey :D")

    my_img_img = Image.open("./my_img.jpg")

    my_img_grey_rgb_img = image_to_grey_rgb(my_img_img)
    my_img_grey_rgb_img.save("./my_img_grey_rgb.jpg")

    my_img_grey_img = image_to_grey(my_img_img)
    my_img_grey_img.save("./my_img_grey.jpg")

    my_img_negative_img = image_to_negative(my_img_img)
    my_img_negative_img.save('./my_img_negative.jpg')

    my_img_sepia_img = image_to_sepia(my_img_img)
    my_img_sepia_img.save('./my_img_sepia.jpg')

    

