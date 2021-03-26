from abc import ABC, ABCMeta, abstractmethod

class InvisibilitySuperPower(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def turnInvisible(self) -> None:
        raise NotImplementedError

    def turnVisible(self) -> None:
        raise NotImplementedError