import os
import re

import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

input_file = 'https://adventofcode.com/2023/day/1/input'
cookies = {'session': os.getenv('session')}

response = requests.get(input_file, cookies = cookies)

if response.status_code == 200:
    lines = response.text.split('\n')
else:
    print(f"Failed to download file: {response.status_code}")

def get_calibration_value(string):
    numbers = re.findall(r'\d', string)
    if len(numbers) == 0:
        return 0
    return int(numbers[0] + numbers[-1])

calibration_values = [get_calibration_value(line) for line in lines]

calibration_value_sum = sum(calibration_values)
print(f"{calibration_value_sum=}")
# answer: 54953

# Part 2

# In part 2, the calibration numbers may not only be numeric but may also be
# word numbers, e.g. "one" or "two".

def get_calibration_value_with_words(string, debug=False):
    number_words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }
    number_words_regex = '|'.join(number_words.keys())

    regex = rf'(?=({number_words_regex}|\d))'
    numbers = re.findall(regex, string)
    # convert the number words to numbers:
    numbers = [number_words.get(i.lower(), i) for i in numbers]
    if debug:
        print(f"{string=}")
        print(f"{numbers=}")
    if len(numbers) == 0:
        return 0
    return int(numbers[0] + numbers[-1])


calibration_value_with_words = [get_calibration_value_with_words(line) for line in lines]

calibration_value_words_sum = sum(calibration_value_with_words)
print(f"{calibration_value_words_sum=}")