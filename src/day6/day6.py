def get_win_possibilities(time, record):
    win_options = 0
    for i in range(time):
        if get_distance(time, i) > record:
            win_options += 1
    return win_options

def get_distance(time, button_held):
    return button_held * (time-button_held)

def solve_day6_part1(times, distances):
    chances = 1
    for i in range(len(times)):
        chances *= get_win_possibilities(times[i], distances[i])
    return chances

def solve_day6_part2(time, record):
    return get_win_possibilities(time, record)

def get_input():
    with open('day6input.txt') as f:
        lines = f.readlines()
    times = lines[0].split(':')[-1]
    times = times.split()
    times = [int(time.strip()) for time in times]
    distances = lines[1].split(':')[-1]
    distances = distances.split()
    distances = [int(distance.strip()) for distance in distances]
    return times, distances

def get_input_pt2():
    with open('day6input.txt') as f:
        lines = f.readlines()
    time = lines[0].split(':')[-1]
    time = int(time.strip().replace(' ', ''))
    record = lines[1].split(':')[-1]
    record = int(record.strip().replace(' ', ''))
    return time, record


if __name__ == '__main__':
    times, distances = get_input()
    print(f'Part 1: {solve_day6_part1(times, distances)}')
    time, record = get_input_pt2()
    print(f'Part 1: {solve_day6_part2(time, record)}')
