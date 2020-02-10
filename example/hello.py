class Hello:
    def __init__(self, world):
        self.world = world
        
    def say_something(self, optional=True):
        """
        I'm saying something from the world I have
        """
        self.world.says()