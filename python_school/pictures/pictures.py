from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

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
