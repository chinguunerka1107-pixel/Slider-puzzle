import random

class Object:
    pass

class Dirt(Object):
    pass

class Agent(Object):
    def __init__(self, program):
        self.program = program

    def sense(self):
        pass

    def run(self):
        percepts = self.sense()
        action = self.program(percepts)
        print("Agent: ", percepts, action)
        return action

class VacuumCleanerAgent(Agent):
    def __init__(self):
        def program(percepts):
            room_number, room_state = percepts
        
            return random.choice(["Left", "Right", "Suck"])

        super().__init__(program)

class Environment:
    def __init__(self):
        self.obj_locs = []

    def add_object(self, obj, loc):
        print("Object added", obj, loc)
        self.obj_locs.append((obj, loc))

    def remove_object(self, obj):
        for i, (_obj, _loc) in enumerate(self.obj_locs):
            if _obj == obj:
                self.obj_locs.pop(i)

    def update(self, obj, action):
        pass

    def run(self, n=10):
        for i in range(n):
            for (obj, loc) in self.obj_locs:
                if isinstance(obj, Agent):
                    action = obj.run()
                    self.update(obj, action)

class HotelEnvironment(Environment):
    def __init__(self):
        super().__init__()

    def add_object(self, obj, loc):
        if isinstance(obj, VacuumCleanerAgent):
            def sense():
                current_loc = None
                for (_obj, _loc) in self.obj_locs:
                    if _obj == obj:
                        current_loc = _loc

                room_state = "clean"
                for (_obj, _loc) in self.obj_locs:
                    if isinstance(_obj, Dirt) and _loc == current_loc:
                        room_state = "Dirty"

                return current_loc, room_state
            obj.sense = sense
        super().add_object(obj, loc)

    def update(self, obj, action):
        if isinstance(obj, VacuumCleanerAgent):
            obj_index = None
            for i, (_obj, _loc) in enumerate(self.obj_locs):
                if _obj == obj:
                    obj_index = i
                    break
            vacuum_cleaner, vacuum_cleaner_loc = self.obj_locs[obj_index]
            if action == "Left":
               self.obj_locs[obj_index] = (obj, "A") 
            elif action == "Right":
                self.obj_locs[obj_index] = (obj, "B")
            elif action == "Suck":
                for (_obj, _loc) in self.obj_locs:
                    if isinstance(_obj, Dirt) and _loc == vacuum_cleaner_loc: 
                        self.remove_object(_obj)

    def run(self, n=10):
        for i in range(n):
            if i % 2 == 0:
                self.add_object(Dirt(), random.choice(["A", "B"]))
            for (obj, loc) in self.obj_locs:
                if isinstance(obj, Agent):
                    action = obj.run()
                    self.update(obj, action)

hotel_inveronment = HotelEnvironment()

vacuum_cleaner = VacuumCleanerAgent()
hotel_inveronment.add_object(vacuum_cleaner, "B")

hotel_inveronment.run()
