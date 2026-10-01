import mesa

class Guard(mesa.Agent):
    pass

class Thief(mesa.Agent):
    pass

class Shortest_Path(mesa.Model):
    def __init__(self, width, height):
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        self.schedule = mesa.time.RandomActivation(self)

        # Create guards and thieves
        for i in range(5):  # Example: 5 guards
            guard = Guard(i, self)
            self.schedule.add(guard)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(guard, (x, y))

        for i in range(3):  # Example: 3 thieves
            thief = Thief(i + 5, self)  # IDs continue from guards
            self.schedule.add(thief)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(thief, (x, y))

    def step(self):
        self.schedule.step()