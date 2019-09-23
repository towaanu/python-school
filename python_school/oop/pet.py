class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"Hello I'm a pet :D. My name is {self.name}")

    def description(self):
        print(f"My name is {self.name}")
    
    def __str__(self):
        return f"Name: {self.name} || Age : {self.age}"

class Dog(Pet):
    
    def speak(self):
        super().speak()
        print("Waf waf")

    def bark(self):
        print("WAF WAF")

if __name__ == "__main__":
    print("hello pet")

    my_dog = Dog("foo", 5)
    my_dog.speak()
    my_dog.description()
    print(my_dog)