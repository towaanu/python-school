from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")

class QueueWithList:

    def __init__(self, items: List[T] = []) -> None:
        self.queue_list = items[:]
    
    def add(self, item:T) -> None:
        self.queue_list.append(item)
    
    def get_item(self) -> Optional[T]:
        if self.is_empty():
            return None
        
        return self.queue_list.pop(0)

    def is_empty(self) -> bool:
        return self.count() == 0

    def count(self) -> int:
        return len(self.queue_list)
    
    def __str__(self) -> str:
        items_str = ""

        for item in self.queue_list:
            items_str += f"{item}, "
        
        return f"[ {items_str[:-2]} ]"

if __name__ == "__main__":
    print("Hello queue list :) ")
    my_queue = QueueWithList([-1, 0])
    my_queue.add(1)
    my_queue.add(2)
    my_queue.add(3)
    my_queue.add(4)
    my_queue.add(5)

    print(f"Get item {my_queue.get_item()}")
    print(f"Get item {my_queue.get_item()}")
    my_queue.add(6)
    my_queue.add(7)
    print(my_queue)
    print(f"Get item {my_queue.get_item()}")
    print(f"Is empty {my_queue.is_empty()}")
    print(f"Get item {my_queue.get_item()}")
    print(f"Get item {my_queue.get_item()}")
    print(f"Get item {my_queue.get_item()}")
    print(f"Get item {my_queue.get_item()}")
    print(f"Get item {my_queue.get_item()}")
    print(f"Get item {my_queue.get_item()}")
    print(f"Get item {my_queue.get_item()}")
    print(f"Get item {my_queue.get_item()}")
    print(f"Is empty {my_queue.is_empty()}")