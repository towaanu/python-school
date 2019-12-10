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


if __name__ == "__main__":
    print("Hello grey :D")

    mario_art_img = Image.open("./mario_art.jpg")

    mario_art_grey_rgb_img = image_to_grey_rgb(mario_art_img)
    mario_art_grey_rgb_img.save("./mario_art_grey_rgb.jpg")

    mario_art_grey_img = image_to_grey(mario_art_img)
    mario_art_grey_img.save("./mario_art_grey.jpg")

    mario_art_negative_img = image_to_negative(mario_art_img)
    mario_art_negative_img.save('./mario_art_negative.jpg')

