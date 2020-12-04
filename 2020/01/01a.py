# https://adventofcode.com/2020/day/1


import requests

# here's where the input list of numbers comes from
input_url = 'https://adventofcode.com/2020/day/1/input'

# the list of numbers generated is unique to each user - my session ID gives me
# my list.
session_id = ***REMOVED***  # noqa
# get the list of numbers
r = requests.get(input_url, headers={'Cookie': f'session={session_id}'})

# turn the text list (e.g. '1234\n5678\n9876\n') into a list that has non-empty
# strings. Note that i drop the last item. this is because the string ends with
# a newline.
numbers = list(r.text.split("\n"))[:-1]
s
# figure out what two numbers add to 2020


def check_sum(nums, k):
    '''
    Test if a list of numbers add up to a certain value. if two of those
    numbers add up to a value, k, multiply those numbers together.
    Otherwise, return False
    '''
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if int(nums[i]) + int(nums[j]) == k:
                return int(nums[i]) * int(nums[j])
    return False


result = check_sum(numbers, 2020)

print(result)
