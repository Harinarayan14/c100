class Car:
    def __init__(self,color,model,company):
        self.color =color
        self.model =model
        self.company =company
    def start(self):
        print("Car has Started.")
    def stop(self):
        print("Car has Stopped.")
    def changeGear(self,gear):
        print("Gear Changed To")
        print(gear)
car1 = Car("red","camry","toyota")
print(car1.color)
car1.start()
car1.stop()
car1.changeGear(2)
