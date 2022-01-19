#problem
class Phone:
    def voice():
        pass
    def text():
        pass
    def camera():
        pass

class SmartPhone(Phone):
    def voice():
        raise NotImplementedError
    def text():
        raise NotImplementedError
    def camera():
        raise NotImplementedError

class OldSchoolPhone(Phone):
    def voice():
        raise NotImplementedError
    def text():
        raise NotImplementedError

nokia = OldSchoolPhone()


print(help(nokia)) #it shouldn't have the camera method
