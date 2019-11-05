
def get_char_for_digit(n):
    integer_n = int(n)
    if n < 10:
        return str(integer_n)
    else:
        # chr(97) = a and chr(97 + 25) = z
        return chr(integer_n + 87)

def decimal_to_binary(n, base=2):
    # int part
    current_int_part = n // 1
    int_part_binary = ""
    while current_int_part > 0:
        int_part_binary += get_char_for_digit(current_int_part % base)
        current_int_part = current_int_part // base
    
    if not int_part_binary:
        int_part_binary = "0"
    
    # float part
    current_float_part = n % 1
    float_part_binary = ""
    i = 0
    while i < 10 and current_float_part != 0:
        current_float_part *= base

        if current_float_part >= 1:
            float_part_binary += get_char_for_digit(current_float_part // 1)
        else:
            float_part_binary += "0"

        current_float_part = current_float_part % 1
        i += 1

    res = int_part_binary[::-1]

    if float_part_binary:
        res += f",{float_part_binary}"

    return res



if __name__ == "__main__":
    print("Hello")
    print(decimal_to_binary(10.5))
    print(decimal_to_binary(315.2, 16))
    print(decimal_to_binary(9, 8))


      
    
