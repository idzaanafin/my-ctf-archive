import pickle

# Define a sample class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
person_obj = Person("John Doe", 30)

# Pickle the object to a file
with open("person.pkl", "wb") as file:
    pickle.dump(person_obj, file)
