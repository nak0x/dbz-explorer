from threading import Lock
from abc import ABC, abstractmethod
from typing import Dict
from uuid import uuid4, UUID

# Thread safe Singletons
class ThreadSafeSingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class GenericSubject(ABC):
    pass

# Generic observer system, to use where ever I need
class GenericObserver(ABC):
    _id: UUID = uuid4()

    @abstractmethod
    def update(self, subject: GenericSubject):
        """
        Receive update from subject.
        """
        pass

class GenericSubject(ABC):
    _observers: Dict[str, GenericObserver] = {}
    _id: UUID = uuid4()

    @abstractmethod
    def attach(self, observer: GenericObserver) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, id) -> None:
        """
        Detach an observer from the subject.
        """
        try:
            del self._observers[id]
        except:
            raise Exception(f"Cannot detach observer {id} from subject {self._id}: Oberver not found.")

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass