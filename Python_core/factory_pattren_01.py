class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError("Unknown animal type")

# Usage
animal = animal_factory("dog")
print(animal.speak())  # Output: Woof!

animal1 = Cat().speak()
print(type(animal1))
print(animal1)