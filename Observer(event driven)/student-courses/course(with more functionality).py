from subject import Subject


# this version have diffrent observer types that can happen
class Course(Subject):
    def __init__(self, name, availability="unknown", max_student=2):
        self.name = name
        self.availability = availability
        self.observers_list = []
        self.waiting_list = []
        self.max_student = max_student
        self.current_num_student = 0

    def subscribe(self, Observer):
        """add observer to observers_list"""
        if self.current_num_student >= self.max_student:
            self.waiting_list.append(Observer)
            return
        self.observers_list.append(Observer)
        self.current_num_student += 1

    def unsubscribe(self, Observer):
        """remove the observer from the observers list"""
        self.observers_list.remove(Observer)
        if self.waiting_list:
            waiting_observer = self.waiting_list.pop()
            self.observers_list.append(waiting_observer)
            self.notifywaitingsubscriber(waiting_observer)
            return
        self.current_num_student -= 1

    def notifyallsubscribers(self):
        """notify the observers in observer list"""
        for observer in self.observers_list:
            observer.update(self.availability)

    def notifywaitingsubscriber(self, Observer):
        """notify waiting observer in waiting list"""
        Observer.update(self.availability)

    def setavailability(self, available):
        """set the availability of the course (subject)"""
        self.availability = self.name + (" available" if available else " not available")
