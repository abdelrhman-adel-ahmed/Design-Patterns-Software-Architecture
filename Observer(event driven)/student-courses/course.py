from subject import Subject


class Course(Subject):
    def __init__(self, name, availability="unknown"):
        self.name = name
        self.availability = availability
        self.observers_list = []

    def subscribe(self, Observer):
        """add observer to the observer list"""
        self.observers_list.append(Observer)

    def unsubscribe(self, Observer):
        """remove the observer from the observers list"""
        self.observers_list.remove(Observer)

    def notifyallsubscribers(self):
        """notify the observers in observer list"""
        for observer in self.observers_list:
            observer.update(self.availability)

    def setavailability(self, available):
        """set the availability of the course (subject)"""
        self.availability = self.name + (" available" if available else " not available")
