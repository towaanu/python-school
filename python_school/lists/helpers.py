
def display_list_str(l):
    list_render_string = "[ "

    for item in l:
        list_render_string += f"{item}, "
    
    list_render_string = list_render_string[:-2] + " ]"
    return list_render_string



if __name__ == '__main__':
    items = [1, 43, 5, 4, 9, 99999, 10, 19, 88]
    print(display_list_str(items))