class Car(object):
    def __init__(self, model, color, company, speedlimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print("Started")

    def stop(self):
        print("Stop")

    def accelerate(self):
        print("Accelerated")

    def change_gear(self, gear_type):
        print("Gear Changed")


audi = Car("A6", "white", "Audi", 80)
print(audi.start())
print(audi.accelerate())
print(audi.change_gear())
