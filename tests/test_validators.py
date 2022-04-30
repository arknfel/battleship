import os, sys
import unittest

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from battleship.middlewares import validators





if __name__=="__main__":
    unittest.main()