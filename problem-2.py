
def accelerate(car):
    if car.transmission == "Automatic":
        car.increase_speed_by(5)
        if car.speed > car.max_speed_for_current_gear():
            car.gear_up()
    elif car.transmission() == "Manual":
        car.increase_speed_by(10)


class Car:
    def __init__(self, max_speed, transmission, speed=0, gear=1):
        self.max_speed = max_speed
        self.transmission = transmission
        self.speed = speed
        self.gear = gear
    
    def increase_speed_by(self, value):
        self.speed += value
        if self.speed > self.max_speed:
            self.speed = self.max_speed
            
    def gear_up(self):
        # details about this function is not relavent hence this function has been implemented as `pass`
        pass
    
    def max_speed_for_current_gear(self):
        # details about this function is not relavent hence this function has been implemented as `pass`
        pass
