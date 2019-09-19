from PIL import Image


def rotateImage(base_image):
    width, height = base_image.size
    x_offset = width // 2
    y_offset = height // 2

    # rotated_image = Image.new("RGB", (2000, 2000))
    rotated_image = Image.new("RGB", (height, width))

    for x in range(width):
        for y in range(height):
            current_pixel = base_image.getpixel((x, y))

            # x_by_center = x - x_offset
            # y_by_center = y - y_offset
            # rotated_position = (-y_by_center + y_offset, x_by_center + x_offset)
            rotated_position = (-y + height - 1, x)
            # print(f"rotated position {rotated_position}")

            rotated_image.putpixel(rotated_position, current_pixel)
    
    return rotated_image 

if __name__ == '__main__':
    print("Hello pictures rotate :D")

    images_path = "images"
    res_images_path = "res_images"
    fuji_image = Image.open(f'{images_path}/fuji.jpeg')
    print(f"Image size {fuji_image.size}")
    rotated_fuji = rotateImage(fuji_image)

    rotated_fuji.save(f'{res_images_path}/fuji_rotate.jpeg')
     