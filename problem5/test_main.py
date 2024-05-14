import unittest
from main import mean_median

class TestMeanMedian(unittest.TestCase):

    def test_mean_median_1(self):
        input_array = [1, 2, 3, 4]
        expected_result = (2.5, 2.5)
        result = mean_median(input_array)
        msg = f"Expected: {expected_result}, Got: {result}"
        self.assertEqual(result, expected_result, msg)

    def test_mean_median_2(self):
        input_array = [1, 2, 3, 4, 5]
        expected_result = (3.0, 3)
        result = mean_median(input_array)
        msg = f"Expected: {expected_result}, Got: {result}"
        self.assertEqual(result, expected_result, msg)

    def test_mean_median_3(self):
        input_array = [7, 8, 9, 13, 15]
        expected_result = (10.4, 9)
        result = mean_median(input_array)
        msg = f"Expected: {expected_result}, Got: {result}"
        self.assertEqual(result, expected_result, msg)

    def test_mean_median_4(self):
        input_array = [10, 20, 30, 40, 50]
        expected_result = (30.0, 30)
        result = mean_median(input_array)
        msg = f"Expected: {expected_result}, Got: {result}"
        self.assertEqual(result, expected_result, msg)

    def test_mean_median_5(self):
        input_array = [15, 20, 30, 60, 120]
        expected_result = (49.0, 30)
        result = mean_median(input_array)
        msg = f"Expected: {expected_result}, Got: {result}"
        self.assertEqual(result, expected_result, msg)

    def test_mean_median_empty(self):
        input_array = []
        expected_result = None
        result = mean_median(input_array)
        msg = f"Expected: {expected_result}, Got: {result}"
        self.assertEqual(result, expected_result, msg)
        
if __name__ == '__main__':
    unittest.main()