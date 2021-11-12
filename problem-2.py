
def accelerate(car):
    if car.getTransmission() == "Automatic":
        car.increaseSpeedBy(5)
        if car.getSpeed() > car.maxSpeedForCurrentGear():
            car.gearUp()
    elif car.getTransmission() == "Manual":
        car.increaseSpeedBy(10)


class Car:
    def __init__(self, maxSpeed, transmission, speed=0, gear=1):
        self.maxSpeed = maxSpeed
        self.transmission = transmission
        self.speed = speed
        self.gear = gear
        
    def getSpeed(self):
        return self.speed
    
    def getGear(self):
        return self.gear
    
    def getTransmission(self):
        return self.transmission
    
    def increaseSpeedBy(self, value):
        self.speed += value
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
            
    def gearUp(self):
        pass
    
    def maxSpeedForCurrentGear(self):
        pass