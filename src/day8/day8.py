DIRECTION_STRING = 'RL'
NETWORK = {
    'AAA': ('BBB', 'CCC'),
    'BBB': ('DDD', 'EEE'),
    'CCC': ('ZZZ', 'GGG'),
    'DDD': ('DDD', 'DDD'),
    'EEE': ('EEE', 'EEE'),
    'GGG': ('GGG', 'GGG'),
    'ZZZ': ('ZZZ', 'ZZZ')

}
DIRECTION = {
    'L': 0,
    'R': 1
}


def get_input():
    with open('day8input.txt') as f:
        lines = f.readlines()
    direction_string = lines.pop(0).strip()
    network = dict()
    lines.pop(0)
    for line in lines:
        location, directions = line.split(' = (')
        left, right = directions.split(', ')
        right = right.split(')')[0]
        network[location] = (left, right)
    return direction_string, network


def complete_navigation_step(direction_string, network, current_location='AAA'):
    for direction in direction_string:
        current_location = network[current_location][DIRECTION[direction]]
    return len(direction_string), current_location


def navigate_to_destination(direction_string, network):
    location = 'AAA'
    total_steps = 0
    while location != 'ZZZ':
        steps_taken, location = complete_navigation_step(direction_string, network, location)
        total_steps += steps_taken
    return total_steps


# def navigate_start_nodes_to_end_nodes(direction_string, network):
#     # Too slow
#     current_locations = get_start_nodes(network)
#     total_steps = 0
#     while not are_all_nodes_end_nodes(current_locations):
#         for i, location in enumerate(current_locations):
#             steps_taken, new_location = complete_navigation_step(direction_string, network, location)
#             current_locations[i] = new_location
#         total_steps += len(direction_string)
#         print(f'Step: {total_steps}, Locations: {current_locations}')
#     return total_steps


def get_min_steps_to_end_node(direction_string, network, start_node):
    current_location = start_node
    total_steps = 0
    while not is_end_node(current_location):
        steps_taken, current_location = complete_navigation_step(direction_string, network, current_location)
        total_steps += steps_taken
    return total_steps


def get_all_min_steps(direction_string, network):
    start_nodes = get_start_nodes(network)
    steps_to_end = []
    for node in start_nodes:
        steps_to_end.append(get_min_steps_to_end_node(direction_string, network, node))
    return steps_to_end


def get_start_nodes(network):
    start_nodes = []
    for location in network:
        if location[-1] == 'A':
            start_nodes.append(location)
    return start_nodes


def is_end_node(location):
    return location[-1] == 'Z'


# def are_all_nodes_end_nodes(locations):
#     for location in locations:
#         if location[-1] != 'Z':
#             return False
#     return True


def get_lcm(steps):
    i = steps[0]
    while not is_fully_divisble(i, steps[1:]):
        i += steps[0]
    return i


def is_divisible(number, factor):
    return number % factor == 0


def is_fully_divisble(number, factors):
    for factor in factors:
        if not is_divisible(number, factor):
            return False
    return True


def solve_day8_part1(direction_string, network):
    return navigate_to_destination(direction_string, network)


def solve_day8_part2(direction_string, network):
    min_steps = get_all_min_steps(direction_string, network)
    return get_lcm(min_steps)


if __name__ == '__main__':
    direction_string, network = get_input()
    print(f"Part 1: {solve_day8_part1(direction_string, network)}")
    print(f"Part 2: {solve_day8_part2(direction_string, network)}")
