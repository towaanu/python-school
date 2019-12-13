class QueueWithStack:
   
    def __init__(self):
        self.enqueue_stack = list()
        self.dequeue_stack = list()

    def add(self, item):
        self.enqueue_stack.append(item)
    
    def fill_dequeue_stack(self):
        while enqueue_stack:
            current_item = enqueue_stack.pop()
            self.dequeue_stack.append(current_item)
    
    def get_item(self):

        if self.is_empty():
            return None

        if not self.dequeue_stack:
            while self.enqueue_stack:
                current_item = self.enqueue_stack.pop()
                self.dequeue_stack.append(current_item)
        
        return  self.dequeue_stack.pop()
    
    def is_empty(self):
        return not self.enqueue_stack and not self.dequeue_stack
    
    def count(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

    def __str__(self):
        items_str = ""
        
        for i in range(len(self.dequeue_stack) - 1, -1, -1):
            current_item = self.dequeue_stack[i]
            items_str += f"{current_item}, "
        
        for item in self.enqueue_stack:
            items_str += f"{item}, "

        return f"[ {items_str[:-2]} ]"
        

if __name__ == "__main__":
    print("Hello Queue with stack")
    my_queue = QueueWithStack()
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
    print(f"Is empty {my_queue.is_empty()}")

