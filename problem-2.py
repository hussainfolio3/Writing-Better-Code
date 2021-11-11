
def accelerate(car):
    if car.getTransmission() == "Automatic":
        car.increaseSpeedBy(5)
        if car.getSpeed() > car.maxSpeedForCurrentGear():
            car.gearUp()
    elif car.getTransmission() == "Manual":
        car.increaseSpeedBy(10)
