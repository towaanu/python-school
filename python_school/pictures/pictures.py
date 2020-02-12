from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import math

def rgb_pixel_to_grey(r, g, b):
    avg = (r+g+b)/3
    rounded_avg = int(round(avg, 0))
    return (rounded_avg, rounded_avg, rounded_avg)

def image_to_grey(base_image):
    base_pixels = list(base_image.getdata())
    grey_pixels = [rgb_pixel_to_grey(r, g, b) for (r, g, b) in base_pixels]
    grey_image = Image.new('RGB', base_image.size)
    grey_image.putdata(grey_pixels)

    return grey_image

def image_to_grayscale(base_image):
    base_pixels = list(base_image.getdata())
    grayscale_pixels = [(r+g+b)/3 for (r, g, b) in base_pixels]

    grayscale_image = Image.new('L', base_image.size)
    grayscale_image.putdata(grayscale_pixels)

    return grayscale_image

def image_to_negative(base_image):
    base_pixels = list(base_image.getdata())
    negative_pixels = [(255 - r, 255 - g, 255 - b)
                       for (r, g, b) in base_pixels]

    negative_image = Image.new('RGB', base_image.size)
    negative_image.putdata(negative_pixels)

    return negative_image

def get_h_square_pixels(x, y, default_coef=1):
    return [
        ((x-1, y-1), -1 * default_coef), ((x, y-1), -1 * default_coef), ((x+1, y-1), -1 * default_coef),
        ((x-1, y), 0 * default_coef),             ((x+1, y), 0),
        ((x-1, y+1), 1 * default_coef), ((x, y+1), 1 * default_coef), ((x+1, y), 1 * default_coef)
    ]

def get_v_square_pixels(x, y, default_coef=1):
    return [
        ((x-1, y-1), -1 * default_coef), ((x, y-1), 0 * default_coef), ((x+1, y-1), 1 * default_coef),
        ((x-1, y), -1 * default_coef),                 ((x+1, y), 1 * default_coef),
        ((x-1, y+1), -1 * default_coef), ((x, y+1), 0 * default_coef), ((x+1, y), 1 * default_coef)
    ]
def filter_square_pixel_in_image(square_coords, image_size):
    (width, height) = image_size
    return [
                ((square_x, square_y), coef) for ((square_x, square_y), coef) in square_coords 
                if square_x >= 0 and square_y >= 0 and square_x < width and square_y < height
            ]

def avg_rgb_pixels(pixel_square_coords, image):
    r_sum = 0
    g_sum = 0
    b_sum = 0
    for (coord, coef) in pixel_square_coords:
        (r, g, b) = image.getpixel(coord)
        r_sum += r * coef
        g_sum += g * coef
        b_sum += b * coef
    pixels_len = len(pixel_square_coords)

    return (r_sum//pixels_len, g_sum//pixels_len, b_sum//pixels_len)

def add_h_v(h_value, v_value):
    return int(math.sqrt(h_value ** 2 + v_value ** 2))

def image_to_contour(base_image):
    (width, height) = base_image.size

    contour_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r_sum, g_sum, b_sum = (0, 0, 0)
            square_h_coords = filter_square_pixel_in_image(get_h_square_pixels(x, y, 3), (width, height))
            square_v_coords = filter_square_pixel_in_image(get_v_square_pixels(x, y, 3), (width, height))
            
            (rh, gh, bh) = avg_rgb_pixels(square_h_coords, base_image)
            (rv, gv, bv) = avg_rgb_pixels(square_v_coords, base_image)
            new_pixel_value = (add_h_v(rh, rv), add_h_v(gh, gv), add_h_v(bv, gv))
            contour_image.putpixel((x, y), new_pixel_value)
    return contour_image


# EXIF
def get_exif(img):
    return img._getexif()

def get_labeled_geotagging(exif_geotagging_value):
    labeled_geotagging = {}

    for (key, tag) in GPSTAGS.items():
        if key in exif_geotagging_value:
            labeled_geotagging[tag] = exif_geotagging_value[key]
    
    return labeled_geotagging

def get_labeled_exif(img):
    raw_exif = get_exif(img)
    labeled_exif = {}
    for (key, val) in raw_exif.items():
        tag = TAGS.get(key)
        if tag == 'GPSInfo':
            labeled_exif[tag] = get_labeled_geotagging(val)
        else:
            labeled_exif[tag] = val

    return labeled_exif

# Get gps data from geotagging
def get_decimal_from_dms(dms, ref):

    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)

if __name__ == "__main__":
    print("Hello pictures :D")

    images_path = 'images'
    res_images_path = 'res_images'

    street_art_image = Image.open(f'{images_path}/street_art.jpeg')
    mario_art_image = Image.open(f'{images_path}/mario_art.jpg')

    # Contours
    street_art_contour_image = image_to_contour(street_art_image)
    street_art_contour_image.save(
        f'{res_images_path}/street_art_contour.jpeg')

    # Exif
    labeled_exif = get_labeled_exif(mario_art_image)
    print(f'Exif : {labeled_exif}')
    print(f'Exif coordinate (lat, lon) : {get_coordinates(labeled_exif["GPSInfo"])}')

    # Negative
    street_art_negative_image = image_to_negative(street_art_image)
    street_art_negative_image.save(
        f'{res_images_path}/negative_street_art.jpeg')

    # Grey
    street_art_grey_image = image_to_grey(street_art_image)
    street_art_grey_image.save(
        f'{res_images_path}/grey_street_art.jpeg')
    
    # Grayscale
    street_art_grayscale_image = image_to_grayscale(street_art_image)
    street_art_grayscale_image.save(
        f'{res_images_path}/grayscale_street_art.jpeg')
