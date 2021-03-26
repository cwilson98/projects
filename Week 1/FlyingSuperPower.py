from abc import ABC, ABCMeta, abstractmethod

class FlyingSuperPower(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def fly(self, distance):
        raise NotImplementedError