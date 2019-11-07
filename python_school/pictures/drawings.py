from PIL import Image
import math

def euclidean_distance(a, b):
    euclidean_sum = 0
    for i in range(len(a)):
        euclidean_sum += (a[i] - b[i])**2
    
    euclidean_distance = math.sqrt(euclidean_sum)

    return euclidean_distance


def create_france_flag(width, height):

    blue_color = (0, 0, 255)
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)

    france_flag = Image.new("RGB", (width, height))
    band_width = width // 3

    # blue part
    for x in range(band_width):
        for y in range(height):
            france_flag.putpixel((x, y), blue_color)
    
    for x in range(band_width, 2*band_width):
        for y in range(height):
            france_flag.putpixel((x, y), white_color)
    
    for x in range(2*band_width, width):
        for y in range(height):
            france_flag.putpixel((x, y), red_color)

    return france_flag

def create_japan_flag(width, height):
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)
    radius = height*0.3

    japan_flag = Image.new("RGB", (width, height), white_color)

    center = (width//2, height//2)
    
    # draw circle
    for x in range(width):
        for y in range(height):
            if euclidean_distance(center, (x, y)) <= radius:
                japan_flag.putpixel((x, y), red_color)
    
    return japan_flag


if __name__ == "__main__":
    print("Hello drawing :D")
    my_drawings_path = "my_drawings"

    france_flag = create_france_flag(600, 300)
    france_flag.save(f"{my_drawings_path}/france_flag.jpeg")

    japan_flag = create_japan_flag(600, 300)
    japan_flag.save(f"{my_drawings_path}/japan_flag.jpeg")
