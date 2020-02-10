class MyDict:
    def __init__(self, size=10):
        self.items = [[] for i in range(size)]
        self.size = size


    def add_value(self, label, value):
        print(hash(label))
        row_index = hash(label) % self.size
        self.items[row_index].append( (label, value) )
    
    def get_value(self, label):
        row_index = hash(label) % self.size
        row = self.items[row_index]

        for item in row:
            item_label, item_value = item
            if item_label == label:
                return item_value

        return None
    
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    print("Hello custom dict :D")
    my_dict = MyDict()

    print(my_dict.get_value('foo'))
    my_dict.add_value("foo", 6)
    print(my_dict.get_value('foo'))
    print(my_dict)
