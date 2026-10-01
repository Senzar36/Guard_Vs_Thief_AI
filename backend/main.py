import mesa
from pydantic import BaseModel
from ui import Input_Values, InvalidLocationError
class Values(BaseModel):
    directions : bool
    alive : bool
    dead : bool
    speed : int
    time : int
    loc_guard : list
    loc_thief : list

class Guard(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.directions = True
        self.speed = 1
        self.time = 0
        self.loc_guard = []
        self.loc_thief = []

class Thief(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.directions = True
        self.alive = True
        self.dead = False
        self.speed = 1
        self.time = 0
        self.loc_guard = []
        self.loc_thief = []

    def caught(self):
        if self.alive:
            self.dead = True

class Shortest_Path(mesa.Model):
    def __init__(self, width, height):
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(5):
            guard = Guard(i, self)
            self.schedule.add(guard)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(guard, (x, y))

        for i in range(3):
            thief = Thief(i + 5, self)
            self.schedule.add(thief)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(thief, (x, y))

    def step(self):
        self.schedule.step()

class Spawn_Guard(mesa.Model):
    def __init__(self, width, height):
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.schedule = mesa.time.RandomActivation(self)

        guard = Guard(0, self)
        self.schedule.add(guard)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(guard, (x, y))

    def step(self):
        self.schedule.step()

class Reiterative_Distance_Finding(mesa.Model):
    def __init__(self, width, height):
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.schedule = mesa.time.RandomActivation(self)

    def distance(self):
        while self.alive == True:
            if Shortest_Path(thief[0], thief[1]) == True:
                self.alive = False
                print("Thief has been caught!")
                print("Game ends!")