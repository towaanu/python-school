def move_hanoi_tower(t_from, t_to, t_tmp, nb_items):

    if nb_items == 1:
        print(f"Move {t_from} => {t_to}")
        return

    move_hanoi_tower(t_from, t_tmp, t_to, nb_items - 1)
    move_hanoi_tower(t_from, t_to, t_tmp, 1)
    move_hanoi_tower(t_tmp, t_to, t_from, nb_items - 1)

if __name__ == "__main__":
    print("Hello hanoi")
    move_hanoi_tower("A", "C", "B", 3)