from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def exif_numbers_to_labels(raw_exif):
    exif_info = {}
    for exif_number in raw_exif.keys():
        current_label = TAGS[exif_number]
        exif_info[current_label] = raw_exif[exif_number]

    raw_gps_info = exif_info["GPSInfo"]
    gps_info = {}
    for gps_number in raw_gps_info.keys():
        current_label = GPSTAGS[gps_number]
        gps_info[current_label] = raw_gps_info[gps_number]
    
    exif_info["GPSInfo"] = gps_info

    return exif_info

def dms_to_dd(exif_dms, exif_ref):
    coef = 1
    if exif_ref == "W" or exif_ref == "S":
        coef = -1

    degree = exif_dms[0][0]
    minutes = exif_dms[1][0]
    seconds = exif_dms[2][0] / exif_dms[2][1]

    return coef * (degree + (minutes/60) + (seconds/3600))

def nmea_to_osm_url(dd_latitude, dd_longitude):
    return f"http://www.openstreetmap.org/?mlat={dd_latitude}&mlon={dd_longitude}"

def exif_to_osm_url(exif_info):
    gps_info = exif_info["GPSInfo"]
    dd_latitude = dms_to_dd(gps_info["GPSLatitude"], gps_info['GPSLatitudeRef'])
    dd_longitude = dms_to_dd(gps_info["GPSLongitude"], gps_info['GPSLongitudeRef'])

    return nmea_to_osm_url(dd_latitude, dd_longitude)

def display_image_info(exif_info):
    print(f"Camera model : {exif_info['Model']}")
    print(f"Position url : {exif_to_osm_url(exif_info)}")
    print(f"Date : {exif_info['DateTimeOriginal']}")
    print(f"Image height : {exif_info['ExifImageHeight']}")
    print(f"Image width : {exif_info['ExifImageWidth']}")
    print(f"X Resolution : {exif_info['XResolution']}")
    print(f"Y Resolution : {exif_info['YResolution']}")

if __name__ == "__main__":
    print("Hello exzim :D")

    mario_art_img = Image.open("./mario_art.jpg")
    raw_exif = mario_art_img._getexif()
    mario_art_exif_info = exif_numbers_to_labels(raw_exif)
    # print(mario_art_exif_info)
    display_image_info(mario_art_exif_info)
