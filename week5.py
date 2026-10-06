import utils.agent as agent 

class Player(agent.Agent):

class Computer(Player):
    pass

class Human(Player):
    pass

class State:
    def __init__(self):
        self.list = [None, None, None, None, None, None, None , None, None]


class TictacEnv(agent.Environment):
     def __init__(self):
         super().__init__()
         self.state = State()

Tictac_env = TictacEnv()
Computer = Computer()
human = Human()

Tictac_env.add_object(computer, None)
Tictac_env.add_object(human , None)