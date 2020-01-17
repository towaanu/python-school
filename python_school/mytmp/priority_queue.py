class PriorityQueue:

    def __init__(self):
        self.cost_values = []
    
    def add(self, value, cost=0):
        new_item = (value, cost)
        self.cost_values.append(new_item)
    
    def get(self):
        if self.is_empty():
            return None

        min_item = min(self.cost_values, key=lambda item: item[1])
        self.cost_values.remove(min_item)
        (value, cost) = min_item

        return value
    
    def get_cost(self, value):
        return next((cost for (item_value, cost) in self.cost_values if item_value == value), None)

    def update_cost(self, value, new_cost):
        for i in range(len(self.cost_values)):
            if self.cost_values[i][0] == value:
                self.cost_values[i] = (value, new_cost)
                i += len(self.cost_values)
    
    def is_empty(self):
        return len(self.cost_values) == 0
    
    def count(self):
        return len(self.cost_values)

if __name__ == "__main__":
    print("Hello")

    pqueue = PriorityQueue()
    pqueue.add("a")
    pqueue.add("a", 5)
    pqueue.add("b", 12)
    pqueue.add("d", 100)
    pqueue.add("c", 50)

    print(pqueue.get())
    print(pqueue.get())
    print(pqueue.get())
    print(pqueue.get())
    print(pqueue.get())
    print(pqueue.get())