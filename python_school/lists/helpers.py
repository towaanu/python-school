
def display_list(l):
    list_render_string = "[ "

    for item in l:
        list_render_string += f"{item}, "
    
    list_render_string = list_render_string[:-2] + " ]"

    print(list_render_string)




if __name__ == '__main__':
    items = [1, 43, 5, 4, 9, 99999, 10, 19, 88]
    display_list(items)