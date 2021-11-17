class Alarm:
    def warn(self, message):
        print(message)
    

class Monitor:
    def __init__(self, value, limit, name, alarm):
        self.value = value
        self.limit = limit
        self.name = name
        self.alarm = alarm
    
    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, value):
        self.value = value
        
    @property
    def limit(self):
        return self.limit
    
    @limit.setter
    def limit(self, limit):
        self.limit = limit
        
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name = name
        
    @property
    def alarm(self):
        return self.alarm
    
    @alarm.setter
    def alarm(self, alarm):
        self.alarm = alarm
            

if __name__ == "__main__":
    alarm = Alarm()
    monitor = Monitor("Time Vortex Hocus", 2, "Monitor", alarm)
    monitor.value = 3
    if (monitor.value > monitor.limit):
        monitor.alarm.warn(monitor.name + " too high")
        