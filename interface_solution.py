from abc import ABC, abstractmethod

class Voice(ABC):
    @abstractmethod
    def voice():
        pass

class Text(ABC):
    @abstractmethod
    def text():
        pass

class Camera(ABC):
    @abstractmethod
    def camera():
        pass

class Smartphone(Voice, Text, Camera):
    def voice():
        raise NotImplementedError

    def text():
        raise NotImplementedError

    def camera():
        raise NotImplementedError

class OldSchoolPhone(Voice, Text):
    def voice():
        raise NotImplementedError

    def text():
        raise NotImplementedError