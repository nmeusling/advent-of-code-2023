from typing import List

BLUE = 14
GREEN = 13
RED = 12


class Round:
    def __init__(self, blue, red, green):
        self.blue = blue
        self.red = red
        self.green = green

    def is_possible(self):
        return self.blue <= BLUE and self.red <= RED and self.green <= GREEN


class Game:
    def __init__(self, id, rounds: List[Round]):
        self.rounds = rounds
        self.id = id
        self.power = self.get_power_of_cubes()

    def is_possible(self):
        for game_round in self.rounds:
            if not game_round.is_possible():
                return False
        return True

    def get_power_of_cubes(self):
        min_required_red = self.rounds[0].red
        min_required_blue = self.rounds[0].blue
        min_required_green = self.rounds[0].green

        i = 1
        while i < len(self.rounds):
            if self.rounds[i].red > min_required_red:
                min_required_red = self.rounds[i].red
            if self.rounds[i].green > min_required_green:
                min_required_green = self.rounds[i].green
            if self.rounds[i].blue > min_required_blue:
                min_required_blue = self.rounds[i].blue
            i += 1
        return min_required_red * min_required_blue * min_required_green

def get_dice_amounts(round_details: str):
    round_details = round_details.strip()
    rounds = round_details.split(',')
    blue = 0
    red = 0
    green = 0

    for game_round in rounds:
        if 'blue' in game_round:
            blue = int(game_round.replace('blue', ''))
        elif 'red' in game_round:
            red = int(game_round.replace('red', ''))
        elif 'green' in game_round:
            green = int(game_round.replace('green', ''))
    return Round(blue, red, green)


def get_input():
    with open('day2input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split(':')[-1] for line in lines]
    game_lines = [line.split(';') for line in lines]
    games = []
    for i, game_line in enumerate(game_lines):
        game_rounds = []
        for game_round in game_line:
            game_rounds.append(get_dice_amounts(game_round))
        games.append(Game(i+1, game_rounds))

    return games


def solve_day2_part1(games):
    sum = 0
    for game in games:
        if game.is_possible():
            sum += game.id
    return sum


def solve_day2_part2(games):
    sum = 0
    for game in games:
        sum += game.power
    return sum


if __name__ == '__main__':
    print(f"Part 1: {solve_day2_part1(get_input())}")
    print(f"Part 2: {solve_day2_part2(get_input())}")
