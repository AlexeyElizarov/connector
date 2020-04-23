from abc import ABCMeta


class Observable(metaclass=ABCMeta):
    """
    Abstract observable
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.observers = []

    def register(self, observer) -> None:
        """
        Register new observer.
        """
        self.observers.append(observer)

    def post(self, message) -> None:
        """
        Notify observers.
        """
        for observer in self.observers:
            observer.refresh(message)