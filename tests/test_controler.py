import os, sys
import unittest

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from battleship.controler import start, shoot
from battleship.models import Board


meta = {
    "ships": [
        {
            "x": 2,
            "y": 1,
            "size": 4,
            "direction": "H"
        },
        {
            "x": 7,
            "y": 4,
            "size": 3,
            "direction": "V"
        },
        {
            "x": 3,
            "y": 5,
            "size": 2,
            "direction": "V"
        },
        {
            "x": 6,
            "y": 8,
            "size": 1,
            "direction": "H"
        }
    ]
}

total_cells = sum([ship['size'] for ship in meta['ships']])

class TestSampleClass(unittest.TestCase):

    def test_start(self):

        board = start(meta['ships'])

        self.assertIsInstance(
            board,
            Board,
            'board is an instance of class Board'
        )

        self.assertEqual(
            len(board.occupied_cells),
            total_cells,
            'length cells = length valid ships' 
        )

    def test_shoot(self):

        board = start(meta['ships'])

        result = shoot({'x': 6, 'y': 8}, board)

        self.assertEqual(result, 'SINK', "expect 'SINK'")

        result = shoot({'x': 6, 'y': 8}, board)

        self.assertEqual(result, 'HIT', "expect 'HIT'")

        result = shoot({'x': 6, 'y': 8}, board)

        self.assertEqual(result, 'WATER', "expect 'WATER'")

        # rases exception if shot coords are out of range
        self.assertRaises(
            Exception,
            shoot,
            {'x': 10, 'y': 10},
            board,
            msg="expects an exception of type Exception"
        )
        
        self.assertRaises(
            Exception,
            shoot,
            {'x': 0, 'y': -1},
            board,
            msg="expects an exception of type Exception"
        )

if __name__=="__main__":
    unittest.main()
