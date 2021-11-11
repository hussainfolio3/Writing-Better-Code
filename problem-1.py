class Monitor:
    def __init__(self, name, limit, alarm):
        self.value = 0
        self.limit = limit
        self.isTooHigh = False
        self.name = name
        self.alarm = alarm

    def getValue(self):
        return self.value

    def setValue(self, arg):
        self.value = arg

    def getLimit(self):
        return self.limit

    def getName(self):
        return self.name

    def getAlarm(self):
        return self.alarm
    
    
class Alarm:
    def warn(self, message):
        print(message)
        
        
def main():
    alarm = Alarm()
    monitor = Monitor("Time Vortex Hocus", 2, alarm)
    monitor.setValue(3)
    if (monitor.getValue() > monitor.getLimit()):
        monitor.getAlarm().warn(monitor.getName() + " too high")
        
        
if __name__ == "__main__":
    main()
