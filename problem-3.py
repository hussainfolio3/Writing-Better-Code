
class AlertStateContext:
    def __init__(self):
        self.currentState = "Vibration"
    def setState(self, state):
        self.currentState = state
    def alert(self):
        if self.currentState == "Vibration":
            print("Vibrating...")
        elif self.currentState == "Silent":
            print("Silent...")
        elif self.currentState == "Loud":
            print("Loud...")
    