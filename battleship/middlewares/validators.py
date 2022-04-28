
def validate_range(meta, board):
    x = meta['x']
    y = meta['y']
    
    # check if coord values are in range
    if (x not in board.xrange) or (y not in board.yrange):
        raise Exception(f'coordinates out of range: {meta}')


def validate_direction(meta):
    # check if direction is valid
    if (meta['direction'] not in ('H', 'V')):
        raise Exception(f'invalid direction: {meta}')


def validate_dims(meta, board):
    x = meta['x']
    y = meta['y']
    size = meta['size']
    direction = meta['direction']

    # check if ship dims are in range
    if (direction == 'H') and (x + size not in board.xrange):
        raise Exception(f'x-dim out of range: {meta}')

    if (direction == 'V') and (y + size not in board.yrange):
        raise Exception(f'y-dim out of range: {meta}')


def validate_position(ship, occupied_cells):

    if any(cell in occupied_cells for cell in ship.cells):
        raise Exception('ship position overlap')

