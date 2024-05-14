import unittest
from main import ubah_huruf

class TestUbahHuruf(unittest.TestCase):
    def test_ubah_huruf_sentence_1(self):
        input_sentence = "SEPULSA OKE"
        expected_output = "COZEVCK YUO"
        result = ubah_huruf(input_sentence)
        msg = f"Expected: {expected_output}, Got: {result}"
        self.assertEqual(result, expected_output, msg)

    def test_ubah_huruf_sentence_2(self):
        input_sentence = "ALTERRA ACADEMY"
        expected_output = "KVDOBBK KMKNOWI"
        result = ubah_huruf(input_sentence)
        msg = f"Expected: {expected_output}, Got: {result}"
        self.assertEqual(result, expected_output, msg)

    def test_ubah_huruf_sentence_3(self):
        input_sentence = "INDONESIA"
        expected_output = "SXNYXOCSK"
        result = ubah_huruf(input_sentence)
        msg = f"Expected: {expected_output}, Got: {result}"
        self.assertEqual(result, expected_output, msg)

    def test_ubah_huruf_sentence_4(self):
        input_sentence = "GOLANG"
        expected_output = "QYVKXQ"
        result = ubah_huruf(input_sentence)
        msg = f"Expected: {expected_output}, Got: {result}"
        self.assertEqual(result, expected_output, msg)
        
    def test_ubah_huruf_sentence_5(self):
        input_sentence = "PROGRAMMER"
        expected_output = "ZBYQBKWWOB"
        result = ubah_huruf(input_sentence)
        msg = f"Expected: {expected_output}, Got: {result}"
        self.assertEqual(result, expected_output, msg)
        
if __name__ == '__main__':
    unittest.main()