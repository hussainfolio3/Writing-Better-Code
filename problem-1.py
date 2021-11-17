class Alarm:
    def warn(self, message):
        print(message)
    

class Monitor:
    def __init__(self, value, limit, name, alarm):
        self.value = value
        self.limit = limit
        self.name = name
        self.alarm = alarm
    
          
if __name__ == "__main__":
    alarm = Alarm()
    monitor = Monitor("Time Vortex Hocus", 2, "Monitor", alarm)
    monitor.value = 3
    if (monitor.value > monitor.limit):
        monitor.alarm.warn(monitor.name + " too high")
        