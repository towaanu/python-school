import unittest
from typing import TypeVar, Generic, List

T = TypeVar('T')

class QueueWithStack:
    """
    Queue implemented using 2 stacks

    Attributes
    ----------
    inbox : stack
        A stack used to store items added
    outbox : stack
        Second stack filled with data from inbox

    Methods
    -------
    
    """

    def __init__(self, items: List = []):
        self.inbox = items[:]
        self.outbox = []
    
    def is_empty(self) -> bool:
        return not self.inbox and not self.outbox
    
    def count(self) -> int:
        return len(self.inbox) + len(self.outbox)

    def add(self, item) -> None:
        self.inbox.append(item)
    
    def get_item(self):
        if self.is_empty():
            return None
        # rehydrate outbox if inbox is empty
        if not self.outbox:
            while self.inbox:
                inbox_item = self.inbox.pop()
                self.outbox.append(inbox_item)
        
        return self.outbox.pop()
    
    def __str__(self) -> str:

        if self.is_empty():
            return "[]"

        items_str = ""
        for i in range(len(self.outbox) - 1, -1, -1):
            items_str += f"{self.outbox[i]}, "

        for item in self.inbox:
            items_str += f"{item}, "

        return f"[ {items_str[:-2]} ]"

class MyQueue:

    def __init__(self, items: List = []):
        self.items = items[:]
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def count(self) -> int:
        return len(self.items)
    
    def add(self, item) -> None:
        self.items.append(item)
    
    def get_item(self):
        if self.is_empty():
            return None
        
        item = self.items[0]
        self.items.pop(0)
        return item

    def __str__(self) -> str:

        if self.is_empty():
            return "[]"

        items_str = ""
        for item in self.inbox:
            items_str += f"{item}, "

        return f"[ {items_str[:-2]} ]"

class TestQueueStack(unittest.TestCase):

    def test_new_empty_queue(self):
        q = QueueWithStack()
        self.assertEqual(q.count(), 0)
        self.assertIsNone(q.get_item())

    def test_is_queue_empty(self):
        q = QueueWithStack()
        q.add(2)
        self.assertFalse(q.is_empty())
        q.get_item()
        self.assertTrue(q.is_empty())
    
    def test_queue_count(self):
        q = QueueWithStack([1, 2, 3, 90, 3, 21])
        self.assertEqual(q.count(), 6, "Count queue initialized with 6 items")

    def test_add_in_queue(self):
        q = QueueWithStack()
        q.add(1)
        q.add(60)
        self.assertEqual(q.count(), 2, "Adding two elements to stacks. Stacks should have 2 items")
    
    def test_get_item(self):
        q = QueueWithStack([10])
        self.assertEqual(q.get_item(), 10)
        self.assertIsNone(q.get_item())
        q.add(78)
        q.add(55)
        self.assertEqual(q.get_item(), 78)
        self.assertEqual(q.get_item(), 55)

class TestQueue(unittest.TestCase):

    def test_new_empty_queue(self):
        q = MyQueue()
        self.assertEqual(q.count(), 0)
        self.assertIsNone(q.get_item())

    def test_is_queue_empty(self):
        q = MyQueue()
        q.add(2)
        self.assertFalse(q.is_empty())
        q.get_item()
        self.assertTrue(q.is_empty())
    
    def test_queue_count(self):
        q = MyQueue([1, 2, 3, 90, 3, 21])
        self.assertEqual(q.count(), 6, "Count queue initialized with 6 items")

    def test_add_in_queue(self):
        q = MyQueue()
        q.add(1)
        q.add(60)
        self.assertEqual(q.count(), 2, "Adding two elements to stacks. Stacks should have 2 items")
    
    def test_get_item(self):
        q = MyQueue([10])
        self.assertEqual(q.get_item(), 10)
        self.assertIsNone(q.get_item())
        q.add(78)
        q.add(55)
        self.assertEqual(q.get_item(), 78)
        self.assertEqual(q.get_item(), 55)

if __name__ == "__main__":
    unittest.main()