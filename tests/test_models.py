import os, sys
import unittest

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from battleship.models import Ship, Board


meta = {
    "x": 2,
    "y": 1,
    "size": 4,
    "direction": "H"
}

meta1 = {
    "x": 7,
    "y": 4,
    "size": 3,
    "direction": "V"
}

total_cells = meta['size']

class TestSampleClass(unittest.TestCase):

    def test_ship_init(self):

        ship = Ship(meta)

        self.assertDictEqual(
            {
                'x': 2,
                'y': 1,
                'size': 4,
                'direction': 'H',
                'cells': {
                    '[2, 1]': ship,
                    '[3, 1]': ship,
                    '[4, 1]': ship,
                    '[5, 1]': ship
                },
                'front': '[2, 1]',
                'rear': '[5, 1]'
            },
            ship.__dict__
        )
    
    def test_board_init(self):

        board = Board(range(100), range(100))

        self.assertDictEqual(
            {'xrange': range(0, 100), 'yrange': range(0, 100), 'occupied_cells': {}},
            board.__dict__
        )
    
    def test_board_spawn(self):

        board = Board(range(100), range(100))
        ship = Ship(meta)
        ship1 = Ship(meta1)
        total_cells = ship.cells.copy()
        total_cells.update(ship1.cells)

        board.spawn(ship).spawn(ship1)

        self.assertDictEqual(
            board.occupied_cells,
            total_cells
        )


if __name__=="__main__":
    unittest.main()