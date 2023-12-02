import unittest

from day_01 import get_calibration_value_with_words


class TestGetCalibrationValueWithWords(unittest.TestCase):
    def test_get_calibration_value_with_words(self):
        test_dict = {
            "1abc2": 12,
            "pqr3stu8vwx": 38,
            "a1b2c3d4e5f": 15,
            "treb7uchet": 77,
            "two1nine": 29,
            "eightwothree": 83,
            "abcone2threexyz":  13,
            "xtwone3four": 24,
            "4nineeightseven2": 42,
            "zoneight234": 14,
            "7pqrstsixteen": 76, 
            'one two three': 13,
            'four five six': 46,
            'seven eight nine': 79,
            'ten eleven twelve': 0,
            '': 0,
            'eightsevenvqvzlqxkbm6rqhsgqpnine7twonex': 81}
        for key, value in test_dict.items():
            print(f"{key=}, {value=}")
            self.assertEqual(get_calibration_value_with_words(key), value)

if __name__ == '__main__':
    unittest.main()