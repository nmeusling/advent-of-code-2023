from typing import List


class ScratchCard:
    def __init__(self, winning_numbers, your_numbers):
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers
        self.matches = self.count_matches()
        self.score = self.score()

    def count_matches(self):
        matches = 0
        for number in self.your_numbers:
            if number in self.winning_numbers:
                matches += 1
        return matches

    def score(self):
        if self.matches == 0:
            return 0
        return 2 ** (self.matches - 1)


def get_input():
    with open('day4input.txt') as f:
        lines = f.readlines()
    scratch_cards = []
    for line in lines:
        winning_numbers, your_numbers = line.split(': ')[-1].split(' | ')
        extracted_winning = [number for number in winning_numbers.split(' ') if number]
        extracted_winning = [int(number) for number in extracted_winning]
        extracted_your = [number for number in your_numbers.split(' ') if number]
        extracted_your = [int(number) for number in extracted_your]
        scratch_cards.append(ScratchCard(extracted_winning, extracted_your))
    return scratch_cards


def score_all_cards(scratch_cards: List[ScratchCard]):
    total_score = 0
    for card in scratch_cards:
        total_score += card.score
    return total_score


def solve_day_4_part_1():
    scratch_cards = get_input()
    return score_all_cards(scratch_cards)


def add_cards_for_matches(scratch_card_counter, matches, index, copies):
    for i in range(matches):
        scratch_card_counter[index + i + 1] += copies


def solve_day_4_part_2():
    scratch_cards = get_input()
    num_cards = (len(scratch_cards))
    scratch_card_counter = dict(zip([i for i in range(num_cards)], [1]*num_cards))
    for i in range(num_cards):
        matches = scratch_cards[i].matches
        copies = scratch_card_counter[i]
        add_cards_for_matches(scratch_card_counter, matches, i, copies)
    return sum(scratch_card_counter.values())



if __name__ == '__main__':
    print(f"Part 1: {solve_day_4_part_1()}")
    print(f"Part 2: {solve_day_4_part_2()}")