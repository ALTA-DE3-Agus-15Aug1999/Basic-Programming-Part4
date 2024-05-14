import unittest
from main import cetak_table_perkalian

class TestCetakTablePerkalian(unittest.TestCase):
    def test_cetak_table_perkalian_9(self):
        expected_output = (
            " 1 2 3 4 5 6 7 8 9\n"
            " 2 4 6 8 10 12 14 16 18\n"
            " 3 6 9 12 15 18 21 24 27\n"
            " 4 8 12 16 20 24 28 32 36\n"
            " 5 10 15 20 25 30 35 40 45\n"
            " 6 12 18 24 30 36 42 48 54\n"
            " 7 14 21 28 35 42 49 56 63\n"
            " 8 16 24 32 40 48 56 64 72\n"
            " 9 18 27 36 45 54 63 72 81\n"
        )
        result = cetak_table_perkalian(9)
        self.assertEqual(result, expected_output)
        
if __name__ == '__main__':
    unittest.main()