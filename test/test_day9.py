from src.day9.day9 import make_prediction, solve_day9_part1, get_historic_value, solve_day9_part2


def test_make_prediction():
    history = [0, 3, 6, 9, 12, 15]
    assert make_prediction(history) == 18
    history = [1, 3, 6, 10, 15, 21]
    assert make_prediction(history) == 28
    history = [10, 13, 16, 21, 30, 45]
    assert make_prediction(history) == 68

def test_get_historic_value():
    history = [10, 13, 16, 21, 30, 45]
    assert get_historic_value(history) == 5

def test_solve_day9_part1():
    histories = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
    assert solve_day9_part1(histories) == 114

def test_solve_day9_part2():
    histories = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
    assert solve_day9_part2(histories) == 2