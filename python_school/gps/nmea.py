
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
        "position_type": position_type,
        "sattelites_count": sattelites_count,
        "horizontal_accuracy": horizontal_accuracy,
        "altitude": f"{altitude_number} {altitude_unit}"
    }

    return formatted_info


if __name__ == "__main__":
    print("Hello nmea :D")

    nmea_message = "$GPGGA,141512.04,4713.3975,N,00500.5647,E,1,7,1.839,282.208,M,,M,0,*7E"
    nmea_info = nmea_to_coords(nmea_message)
    print(nmea_info)

    nmea_message_b = "$GPGGA,092750.000,5321.6802,N,00630.3372,W,1,8,1.03,61.7,M,55.2,M,,*76"
    nmea_info_b = nmea_to_coords(nmea_message_b)
    print(nmea_info_b)
