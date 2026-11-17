class Person:
    def __init__(self,name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")

person1= Person("Lina", 20)
person1.display_info()