class Person:
    name: str
    surname: str
    age: int

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        print(f"{self.name} {self.surname}, {self.age}")

    def say_as(self, message):
        return f"<{self.name} {message}>"

user = ("John", "Doe", 30)
user1 = ("Samantha", "Doe", 30)
#user = Person("John", "Doe", 30)
user.info()
say_as(user, 'hello')