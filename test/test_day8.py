from src.day8.day8 import complete_navigation_step, navigate_to_destination, get_lcm, solve_day8_part2

def test_complete_navigation_step():
    direction_string = 'RL'
    network = {
        'AAA': ('BBB', 'CCC'),
        'BBB': ('DDD', 'EEE'),
        'CCC': ('ZZZ', 'GGG'),
        'DDD': ('DDD', 'DDD'),
        'EEE': ('EEE', 'EEE'),
        'GGG': ('GGG', 'GGG'),
        'ZZZ': ('ZZZ', 'ZZZ')

    }
    assert complete_navigation_step(direction_string, network) == (2, 'ZZZ')

def test_navigate_to_destination():
    direction_string = 'LLR'
    network = {
        'AAA': ('BBB', 'BBB'),
        'BBB': ('AAA', 'ZZZ'),
        'ZZZ': ('ZZZ', 'ZZZ')
    }
    assert navigate_to_destination(direction_string, network) == 6

def test_solve_day8_part2():
    direction_string = 'LR'
    network = {
        '11A': ('11B', 'XXX'),
        '11B': ('XXX', '11Z'),
        '11Z': ('11B', 'XXX'),
        '22A': ('22B', 'XXX'),
        '22B': ('22C', '22C'),
        '22C': ('22Z', '22Z'),
        '22Z': ('22B', '22B'),
        'XXX': ('XXX', 'XXX'),
    }
    assert solve_day8_part2(direction_string, network) == 6


def test_get_lcm():
    assert get_lcm([7, 8, 9]) == 504
    assert get_lcm([12, 9]) == 36
