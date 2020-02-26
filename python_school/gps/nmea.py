import sys
import folium

def remove_leading_zero_dms(dms_coord:str) -> float:
    i = 0
    while dms_coord[i] == "0":
        i += 1
    
    return dms_coord[i:]

def dms_to_dd_coordinate(dms_coord:str) -> float:

    coord_label = dms_coord[-1] 

    coef = 1 
    if coord_label == "S" or coord_label == "W":
        coef = -1

    # -2 for removing N/S/W/E
    float_dms = float(dms_coord[:-1])
    float_dd_coord = (float_dms / 100)
    int_dd_part = float_dd_coord // 1
    decimal_dd_part = float_dd_coord % 1

    dd_cord = int_dd_part + ((decimal_dd_part * 100) / 60)

    return coef * dd_cord

def nmea_to_coords(nmea_msg: str):
    splitted_nmea = nmea_msg.split(',')

    msg_type = splitted_nmea[0]
    sent_time = splitted_nmea[1]
    lat_number = splitted_nmea[2]
    lat_label = splitted_nmea[3]
    long_number = splitted_nmea[4]
    long_label = splitted_nmea[5]
    position_type = splitted_nmea[6]
    sattelites_count = splitted_nmea[7]
    horizontal_accuracy = splitted_nmea[8]
    altitude_number = splitted_nmea[9]
    altitude_unit = splitted_nmea[10]

    sent_time_hours = sent_time[:2]
    sent_time_minutes = sent_time[2:4]
    sent_time_seconds = sent_time[4:]

    formatted_info = {
        "msg_type": msg_type,
        "sent_time": f"{sent_time_hours}h {sent_time_minutes}m {sent_time_seconds}s",
        "latitude": f"{lat_number} {lat_label}",
        "longitude": f"{long_number} {long_label}",
        "dd_latitude": dms_to_dd_coordinate(f"{lat_number}{lat_label}"),
        "dd_longitude": dms_to_dd_coordinate(f"{long_number}{long_label}"),
        "position_type": position_type,
        "sattelites_count": sattelites_count,
        "horizontal_accuracy": horizontal_accuracy,
        "altitude": f"{altitude_number} {altitude_unit}"
    }

    return formatted_info

def nmea_to_osm_url(dd_latitude, dd_longitude):
    return f"http://www.openstreetmap.org/?mlat={dd_latitude}&mlon={dd_longitude}"

def display_nmea_info(nmea_message):
    nmea_info = nmea_to_coords(nmea_message)
    osm_url = nmea_to_osm_url(nmea_info["dd_latitude"], nmea_info["dd_longitude"])
    save_map_html(nmea_info['dd_latitude'], nmea_info['dd_longitude'])
    print(nmea_info)
    print(f"\n osm url : {osm_url}")

def save_map_html(latitude, longitude, filename="my_map.html"):
    m = folium.Map(location=[latitude, longitude])
    folium.Marker(location=[latitude, longitude]).add_to(m)
    m.save(filename)

def sample_data():
    return ["$GPGGA,141512.04,4713.3975,N,00500.5647,E,1,7,1.839,282.208,M,,M,0,*7E", "$GPGGA,092750.000,5321.6802,N,00630.3372,W,1,8,1.03,61.7,M,55.2,M,,*76"]

if __name__ == "__main__":
    print("Hello nmea :D")

    # get nmea from command line
    nmea_messages = sys.argv[1:]

    if not nmea_messages:
        # use sample data 
        nmea_messages = sample_data()

    # display information and osm url for nmea
    for nmea_msg in nmea_messages:
        display_nmea_info(nmea_msg)
        
    