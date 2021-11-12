
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