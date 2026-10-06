class Agent : 
    def __init__(self, program, snese):
        self.sense=sense
        self.program=program
        
    def run(self): 
        percepts=sense()
        action=self.program(percepts)

        return action

class vacuumAgent(Agent):
     def __init__(self, sense): 
         def program(percepts):
             print("percepts", percepts)        
             room_number, room_state = percepts

             if room_state == "Dirty":
                 return "Suck"
             elif room_number =="A":
                 return "Right"
             elif room_number =="B":
                 return "left"
                 
             return"Do-Nothing"
     
         super().__init__(program, sense)
        
def sense():
    return "A", "Dirty"
vacuum_Cleaner = vacuumAgent(sense)
action = vacuum_Cleaner.run()
print("Action" , action) 
