import re
from functools import reduce
with open('inputs/day02.txt') as fp:
    input_string = fp.read()

# input_string = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


games = input_string.split("\n")[:-1]

max_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
        }

valid_index_sum = 0
power_of_minima = 0
for game in games:
    valid = True
    game_index = int(game.split(' ')[1][:-1])
    game_rounds = game[game.index(':')+1:].split(";")
    min_seen = {'red': 0, 'blue':0, 'green':0}
    for game_round in game_rounds:
        draws = game_round.split(", ")
        for draw in draws:
            num, color = draw.strip().split(' ')
            num = int(num)
            min_seen[color] = max(min_seen[color], num)
            if num > max_cubes[color]:
                print(f"Number of {color} too high! {num} > {max_cubes[color]}")
                valid = False
    valid_index_sum += valid * game_index
    power_of_minima += reduce(lambda a,b:a*b, min_seen.values(), 1)

print(valid_index_sum)
print(power_of_minima)
print('------------')

index_sum = 0
power_of_minima = 0
for index, game in enumerate(games, start=1):
    index_sum += reduce(lambda boo, inp: boo and (int(inp[0])<=max_cubes[inp[1]]), re.findall(r"(\d+) (\w+)", game), True) * index
    power_of_minima += reduce(lambda a,b:a*b, reduce(lambda nums, inp: {**nums, inp[1]:max(nums[inp[1]], int(inp[0]))}, re.findall(r"(\d+) (\w+)", game), {'blue':0,'red':0,'green':0}).values(), 1)

print(index_sum)
print(power_of_minima)

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# print(sum(set(list(map(int, re.findall(r"Game (\d+)", input_string)))) - set((index + 1 if int(num) > globals()[f"MAX_{color.upper()}"] else None) for index, game in enumerate(input_string.split('\n')) for _round in game[game.index(':') + 1:].split('; ') for num, color in map(lambda r: r.strip().split(' '), _round.split(', ')))))
# print(sum([reduce(lambda x,y: x*y, reduce(lambda acc, values:{**acc, values[2]: max(acc[values[2]], int(values[1]))}, filter(lambda x: x[0] == game_index, [(index, num, color) for index, game in enumerate(input_string.split('\n')) for _round in game[game.index(':') + 1:].split('; ') for num, color in map(lambda r: r.strip().split(' '), _round.split(', '))]), {'red':0,'green':0,'blue':0}).values(), 1) for game_index in set(list(map(lambda x: x[0], [(index, num, color) for index, game in enumerate(input_string.split('\n')) for _round in game[game.index(':') + 1:].split('; ') for num, color in map(lambda r: r.strip().split(' '), _round.split(', '))])))]))
