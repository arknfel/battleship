from battleship.models import Board, Ship
from .middlewares.validators import (
    validate_range,
    validate_direction,
    validate_dims,
    validate_position
)
from battleship.settings import SETTINGS



def start(meta_ships):

    board = Board(SETTINGS['xrange'], SETTINGS['yrange'])
    
    for meta_ship in meta_ships:

        validate_range(meta_ship, board)
        validate_direction(meta_ship)
        validate_dims(meta_ship, board)

        ship = Ship(meta_ship)

        validate_position(ship, board.occupied_cells)

        board.spawn(ship)

    return board


def shoot(coords, board):

    validate_range(coords, board)

    cell = [coords['x'], coords['y']].__str__()

    print(board.occupied_cells)

    if cell not in board.occupied_cells:

        return 'WATER'
    
    else:
        target_ship = board.occupied_cells[cell]
        print(target_ship.status)
        
        if target_ship.status == 'SINK':

            for cell in target_ship.cells:
                del board.occupied_cells[cell]

            return 'HIT'
        
        elif cell == target_ship.front or cell == target_ship.rear:

            target_ship.status = 'SINK'

            return 'SINK'
        
        else:
            for cell in target_ship.cells:
                del board.occupied_cells[cell]
            
            return 'HIT'




    

