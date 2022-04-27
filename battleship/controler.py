from models import Board, Ship
from middlewares.validators import validate_coords, validate_position


def start(SETTINGS, meta_ships):

    board = Board(SETTINGS.x_range, SETTINGS.y_range, meta_ships)
    
    for meta_ship in meta_ships:

        validate_coords(meta_ship, board)

        ship = Ship(
            [meta_ship['x'], meta_ship['y']],
            meta_ship['size'],
            meta_ship['direction']
        )
   
        validate_position(ship, board.occupied_cells)

        board.spawn(ship)
    
    return board


def shoot(coords, board):

    if [coords['x'], coords['y']].__str__() not in board.occupied_cells:
        return 'WATER'
    
    
    

