from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def subscribe(self, Observer):
        pass

    @abstractmethod
    def unsubscribe(self, Observer):
        pass

    @abstractmethod
    def notifyallsubscribers(self):
        pass
