# a delivered class can assume the place of it's super class
from time import clock_settime


class KitchenAppliance():
    def on():
        pass

    def off():
        pass

    def set_temperature():
        pass

class Toaster(KitchenAppliance):
    def on():
        return 'toaster on'

    def off():
        return 'toaster off'

    def set_temperature():
        return 'toaster temperature changed'

#given that the juicer doesn't have the set_temperature, we should refractor the code
class Juicer(KitchenAppliance):
    def on():
        return 'toaster on'

    def off():
        return 'toaster off'


juicer = Juicer()
print(help(juicer)) # the juicer shouldn't 
