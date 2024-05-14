import unittest
from main import play_with_asterisk

class TestPlayWithAsterisk(unittest.TestCase):
    def test_play_with_asterisk(self):
        expected_output = "    * \n   * * \n  * * * \n * * * * \n* * * * * \n"
        result = play_with_asterisk(5)
        self.assertEqual(result, expected_output)
        
if __name__ == '__main__':
    unittest.main()