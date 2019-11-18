def move_hanoi(tower_from, tower_to, tower_tmp, nb_items):
    
    if nb_items == 1:
        print(f"Move {tower_from} => {tower_to}")
        return
        

    move_hanoi(tower_from, tower_tmp, tower_to, nb_items - 1)
    move_hanoi(tower_from, tower_to, tower_tmp, 1)
    move_hanoi(tower_tmp, tower_to, tower_from, nb_items - 1)

# Move items from A => C
if __name__ == "__main__":
    print("Hello world :D")
    move_hanoi("A", "C", "B", 3)