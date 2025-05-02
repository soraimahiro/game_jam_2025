#entity.py
class Entity:
    def __init__(self):
        self.type = 0  # type of entity
        self.pos = (0, 0)
        self.icon = None
        self.hp = 0
        self.x_move_amount = 0  # how long do the entity move
        self.y_move_amount = 0  # only boss has this
        self.wait_time = 0  # how many rounds do the entity take to move
        self.round_pass = 0  # how many rounds pass
        def next_step(self): # pass to next position 
            self.round_pass += 1
            if self.round_pass >= self.wait_time:
                self.pos.x += self.x_move_amount
                self.pos.y += self.y_move_amount
