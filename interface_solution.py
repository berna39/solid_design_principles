from abc import ABC, abstractmethod

class Voice(ABC):
    @abstractmethod
    def voice():
        pass

class text(ABC):
    @abstractmethod
    def text():
        pass

class Camera(ABC):
    @abstractmethod
    def camera():
        pass