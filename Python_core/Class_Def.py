class Team:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

buddy = Team("Buddy", 9)
miles = Team("Miles", 4)


print(f"{buddy.name} is {buddy.age} years old")  # Output: Buddy is 9 years old
print(f"{miles.name} is {miles.age} years old")  # Output: Miles is 4 years old

# Access the class attribute
print(buddy.species)  # Output: Canis familiaris
print(miles.species)  # Output: Canis familiaris

# Call the instance methods
print(buddy.description())  # Output: Buddy is 9 years old
print(miles.description())  # Output: Miles is 4 years old

print(buddy.speak("Woof Woof"))  # Output: Buddy says Woof Woof
print(miles.speak("Bark Bark"))  # Output: Miles says Bark Bark