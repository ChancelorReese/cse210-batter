from game.actor import Actor

class Brick:
    def __init__(self):
        self._brick = ""
        self._position = Actor(0, 0)


    def create_brick(self):
        # first_brick = brick
        # first_brick = Actor(10, 10)

        # second_brick = brick
        # second_brick = Actor(100, 10)

        # third_brick = brick
        # third_brick = Actor(200, 10)
        pass    


    def get_brick(self):
        return self._brick
        
    def set_brick(brick, self):
        self._brick = brick

