import unittest
from main import draw_xyz

class TestDrawXYZ(unittest.TestCase):
    def test_draw_xyz_3(self):
        expected_output = "Y Z X \nZ Y X \nY Z X \n"
        result = draw_xyz(3)
        self.assertEqual(result, expected_output)
    def test_draw_xyz_5(self):
        expected_output = "Y Z X Z Y \nX Y Z X Z \nY X Y Z X \nZ Y X Y Z \nX Z Y X Y \n"
        result = draw_xyz(5)
        self.assertEqual(result, expected_output)
        
if __name__ == '__main__':
    unittest.main()