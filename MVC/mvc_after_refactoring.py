import random
import string
import tkinter as tk
import uuid
from abc import ABC, abstractmethod


def generate_uuid1():
    return uuid.uuid1()


def generate_uuid4():
    return uuid.uuid4()


def generate_lower_case_str():
    return "".join(random.choices(string.ascii_lowercase, k=30))


def generate_upper_case_str():
    return "".join(random.choices(string.ascii_uppercase, k=30))


def generate_str():
    return "".join(random.choices(string.ascii_letters, k=30))


# our storage
class Model:
    def __init__(self) -> None:
        self.uuid = []


# abstract view
class View(ABC):
    @abstractmethod
    def setUp(self, controller):
        pass

    @abstractmethod
    def insert_to_list(self, item):
        pass

    @abstractmethod
    def clear_list(self):
        pass

    @abstractmethod
    def start_main_loop(self):
        pass


# the logic
class Controller:
    def __init__(self, view: View, model: Model, generate_uuid):
        self.view = view
        self.model = model
        # zeroing the list
        self.model.uuid = []
        self.generate_uuid = generate_uuid

    def start(self):
        self.view.setUp(self)
        self.view.start_main_loop()

    def handle_click_generate_uuid(self):
        self.model.uuid.append(self.generate_uuid())
        self.view.insert_to_list(self.model.uuid[-1])

    def handle_click_clear_list(self):
        self.model.uuid = []
        self.view.clear_list()


# tkview
class TKView(View):
    def setUp(self, controller):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("UUIDGen")
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.label = tk.Label(self.frame, text="Result:")
        self.label.pack()
        self.list = tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH, expand=1)

        self.generate_uuid_button = tk.Button(
            self.frame, text="Generate UUID", command=controller.handle_click_generate_uuid
        )
        self.generate_uuid_button.pack()
        self.clear_button = tk.Button(self.frame, text="Clear list", command=controller.handle_click_clear_list)
        self.clear_button.pack()

    # append uuid at the end of the listBox
    def insert_to_list(self, item):
        self.list.insert(tk.END, item)

    # clear the listBox from the uuid's
    def clear_list(self):
        self.list.delete(0, tk.END)

    def start_main_loop(self):
        self.root.mainloop()


obj = Controller(TKView(), Model(), generate_str)
obj.start()
