from observer import Observer


class Student(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} has new notification {message}")
