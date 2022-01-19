class KitchenAppliance():
    def on():
        pass

    def off():
        pass

class KitchenApplianceWithTemp():
    def set_temperature():
        pass

class Toaster(KitchenApplianceWithTemp):
    def on():
        return 'toaster on'

    def off():
        return 'toaster off'

    def set_temperature():
        return 'toaster temperature changed'

class Juicer(KitchenAppliance):
    def on():
        return 'toaster on'

    def off():
        return 'toaster off'

#now we have the code refractored :)