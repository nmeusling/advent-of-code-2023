from typing import List


def get_differences(current_level: List):
    next_level = []
    for i in range(0, len(current_level) - 1):
        next_level.append(current_level[i+1]-current_level[i])
    return next_level


def get_all_levels(history):
    levels = [history]
    current_level = history
    while sum(current_level) != 0:
        next_level = get_differences(current_level)
        levels.append(next_level)
        current_level = next_level
    return levels


def make_prediction(history):
    all_levels = get_all_levels(history)
    for i in range(len(all_levels) - 1, 0, -1):
        all_levels[i-1].append(all_levels[i][-1] + all_levels[i - 1][-1])
    return all_levels[0][-1]

def get_historic_value(history):
    all_levels = get_all_levels(history)
    for i in range(len(all_levels) -1, 0, -1):
        historic_value = all_levels[i-1][0] - all_levels[i][0]
        all_levels[i-1].insert(0, historic_value)
    return all_levels[0][0]



def solve_day9_part1(histories):
    sum_of_predictions = 0
    for history in histories:
        sum_of_predictions += make_prediction(history)
    return sum_of_predictions

def solve_day9_part2(histories):
    sum_of_historic = 0
    for history in histories:
        sum_of_historic += get_historic_value(history)
    return sum_of_historic


def get_input():
    with open('day9input.txt') as f:
        lines = f.readlines()
    histories = []
    for line in lines:
        numbers = line.split()
        histories.append([int(number) for number in numbers])
    return histories


if __name__ == '__main__':
    print(f"Part 1: {solve_day9_part1(get_input())}")
    print(f"Part 2: {solve_day9_part2(get_input())}")