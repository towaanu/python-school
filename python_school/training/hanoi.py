# Divide and conquer 
# Tower of hanoi

def move_hanoi(nb_disks, tower_from, tower_to, tower_tmp):

    if nb_disks == 1:
        print(f"Move from {tower_from} to {tower_to}")
    else:
        move_hanoi(nb_disks - 1, tower_from, tower_tmp, tower_to)
        move_hanoi(1, tower_from, tower_to, tower_tmp)
        move_hanoi(nb_disks - 1, tower_tmp, tower_to, tower_from)

if __name__ == "__main__":
    print('Hello hanoi :D')
    move_hanoi(3, 'A', 'C', 'B')