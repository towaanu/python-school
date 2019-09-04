from PIL import Image

def rgb_pixel_to_grey(r, g, b):
    avg = int(round((r+g+b/3), 0))
    return (avg, avg, avg)

def image_to_grey(base_image):
    base_pixels = list(base_image.getdata())
    grey_pixels = [rgb_pixel_to_grey(r, g, b) for (r, g, b) in base_pixels]

    grey_image = Image.new('RGB', base_image.size)
    grey_image.putdata(grey_pixels)

    return grey_image


def image_to_negative(base_image):
    base_pixels = list(base_image.getdata())
    negative_pixels = [(255 - r, 255 - g, 255 - b)
                       for (r, g, b) in base_pixels]

    negative_image = Image.new('RGB', base_image.size)
    negative_image.putdata(negative_pixels)

    return negative_image


if __name__ == "__main__":
    print("Hello pictures :D")

    images_path = 'images'
    res_images_path = 'res_images'

    street_art_image = Image.open(f'{images_path}/street_art.jpeg')

    # Negative
    street_art_negative_image = image_to_negative(street_art_image)
    street_art_negative_image.save(
        f'{res_images_path}/negative_street_art.jpeg')

    # Grey
    street_art_grey_image = image_to_grey(street_art_image)
    street_art_grey_image.save(
        f'{res_images_path}/grey_street_art.jpeg')
