

class Ship:

    status = True

    def __init__(self, meta):

        self.x = meta['x']
        self.y = meta['y']
        self.size = meta['size']
        self.direction = meta['direction']
        self.cells = None

        if self.direction == 'H':

            self.cells = {[x, self.y].__str__(): self for x in range(self.x, self.x + self.size + 1)}

        elif self.direction == 'V':

            self.cells = {[self.x, y].__str__(): self for y in range(self.y, self.y + self.size + 1)}

        self.front = list(self.cells.keys())[0]
        self.rear = list(self.cells.keys())[-1]


class Board:

    def __init__(self, x_range, y_range):
        
        self.x_range = x_range
        self.y_range = y_range

        # self.ships = None
        # self.meta_ships = meta_ships

        self.occupied_cells = {}


    def spawn(self, ship):
        
        self.occupied_cells.update(ship.cells)

