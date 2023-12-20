class Pole:
    def __init__(self, screen, color, in_x, in_y, pos_x, pos_y, width, length, free):
        self.screen = screen
        self.color = color
        self.in_x = in_x
        self.in_y = in_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.length = length
        self.free = free
        self.discovered = False
        self.bombs_nearby = '-1'
        self.checking = -1
