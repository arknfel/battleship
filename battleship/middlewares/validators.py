
def validate_coords(ship, board):
    x = ship['x']
    y = ship['y']
    size = ship['size']
    direction = ship['direction']

    failed = []

    # check if direction is valid
    if direction in ('H', 'V'):
        failed.append(f'invalid direction')

    # check if coord values are in range
    if (x not in board.x_range) or (y not in board.y_range):
        failed.append('invalid coordinates')

    # check if ship dims are in range
    if (direction == 'H') and (x + size not in board.x_range):
        failed.append('x-dim out of range')

    if (direction == 'V') and (y + size not in board.y_range):
        failed.append('y-dim out of range')
    
    # raise failed checks if any
    if failed:
        raise Exception(f'Error: {failed}\nparsed: {ship}')


def validate_position(ship, occupied_cells):

    if any(cell in occupied_cells for cell in ship.cells):
        raise Exception('Error: ship position overlap')

