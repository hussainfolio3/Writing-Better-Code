class AlertStateContext:
    def __init__(self):
        self.current_state = "Vibration"
        
    @property
    def state(self):
        return self.current_state
    
    @state.setter
    def state(self, state):
        self.current_state = state
    
    def alert(self):
        if self.current_state == "Vibration":
            print("Vibrating...")
        elif self.current_state == "Silent":
            print("Silent...")
        elif self.current_state == "Loud":
            print("Loud...")
    
