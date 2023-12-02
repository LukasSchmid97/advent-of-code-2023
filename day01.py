import re
with open('inputs/day01.txt') as fp:
    input_string = fp.read()

# input_string = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"""

# input_string = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""


texts = input_string.split("\n")
nums = []
possible_nums = {str(i):str(i) for i in range(10)}
possible_nums = {
        **possible_nums,
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
        }
print(possible_nums)
for text in texts:
    current_matches = [None] * len(text)
    for p_num, p_value in possible_nums.items():
        if text.find(p_num) >= 0:current_matches[text.find(p_num)] = p_value
        if text[::-1].find(p_num[::-1]) > -1: current_matches[len(text) - 1 - text[::-1].find(p_num[::-1])] = p_value
    valid_matches = list(filter(lambda number: number is not None, current_matches))
    nums.append("".join([valid_matches[0], valid_matches[-1]]))
print(sum(map(int, nums)))
