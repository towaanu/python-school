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

def create_danemark_flag(width, height):
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)

    band_size = width // 10
    width_unit = width // 10

    danemark_flag = Image.new("RGB", (width, height), red_color)

    begin_vertical_band = width_unit * 3
    end_vertical_band = begin_vertical_band + band_size

    for x in range(begin_vertical_band, end_vertical_band):
        for y in range(height):
            danemark_flag.putpixel((x, y), white_color)
    

    begin_horizontal_band = (height - band_size) // 2
    end_horizontal_band = (height + band_size) // 2

    for x in range(width):
        for y in range(begin_horizontal_band, end_horizontal_band):
            danemark_flag.putpixel((x, y), white_color)
    
    return danemark_flag

def create_german_flag(width, height):
    white_color = (255, 255, 255)
    black_color = (0, 0, 0)
    yellow_color = (237, 245, 17)
    red_color = (255, 0, 0)

    height_band = height // 3

    german_flag = Image.new("RGB", (width, height), white_color)

    for y in range(height_band):
        for x in range(width):
            german_flag.putpixel((x, y), black_color)

    for y in range(height_band, height_band*2):
        for x in range(width):
            german_flag.putpixel((x, y), red_color)

    for y in range(height_band*2, height):
        for x in range(width):
            german_flag.putpixel((x, y), yellow_color)
    
    return german_flag




if __name__ == "__main__":
    print("Hello drawing :D")
    my_drawings_path = "my_drawings"

    france_flag = create_france_flag(600, 300)
    france_flag.save(f"{my_drawings_path}/france_flag.jpeg")

    japan_flag = create_japan_flag(600, 300)
    japan_flag.save(f"{my_drawings_path}/japan_flag.jpeg")

    danemark_flag = create_danemark_flag(600, 300)
    danemark_flag.save(f"{my_drawings_path}/danemark_flag.jpeg")

    german_flag = create_german_flag(600, 300)
    german_flag.save(f"{my_drawings_path}/german_flag.jpeg")
