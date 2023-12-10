from dataclasses import dataclass
from typing import List

RELATIVE_STRENGTHS = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
RELATIVE_STRENGTHS_JOKER = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1,}


@dataclass
class HandStrengths:
    five_of_a_kind = 7
    four_of_a_kind = 6
    full_house = 5
    three_of_a_kind = 4
    two_pair = 3
    one_pair = 2
    high_card = 1


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def __cmp__(self, other):
        return compare_hands(self.cards, other.cards, use_jokers=False)

    def __lt__(self, other):
        return self.__cmp__(other) < 0

class JokerHand(Hand):
    def __cmp__(self, other):
        return compare_hands(self.cards, other.cards, use_jokers=True)


def compare_hands(first, second, use_jokers):
    if use_jokers:
        relative_strengths = RELATIVE_STRENGTHS_JOKER
    else:
        relative_strengths = RELATIVE_STRENGTHS
    first_hand_type = get_hand_type(first, use_jokers)
    second_hand_type = get_hand_type(second, use_jokers)
    if first_hand_type == second_hand_type:
        for i in range(len(first)):
            if relative_strengths[first[i]] != relative_strengths[second[i]]:
                return relative_strengths[first[i]] - relative_strengths[second[i]]
        return 0
    else:
        return first_hand_type - second_hand_type


def get_hand_type(hand, use_jokers=True):
    cards = dict()
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if use_jokers:
        has_jokers = 'J' in cards
    else:
        has_jokers = False

    if len(cards) == 1 or (len(cards) == 2 and has_jokers):
        return HandStrengths.five_of_a_kind
    elif len(cards) == 2 or (len(cards) == 3 and has_jokers):
        if has_jokers:
            num_jokers = cards.pop('J')
        if 1 in cards.values():
            if has_jokers:
                cards['J'] = num_jokers
            return HandStrengths.four_of_a_kind
        elif 2 in cards.values():
            if has_jokers:
                cards['J'] = num_jokers
            return HandStrengths.full_house

    elif len(cards) == 3 or (len(cards) == 4 and has_jokers > 0):
        if 3 in cards.values() or has_jokers > 0:
            return HandStrengths.three_of_a_kind
        elif 2 in cards.values():
            return HandStrengths.two_pair
    elif len(cards) == 4 or (len(cards) == 5 and has_jokers > 0):
        return HandStrengths.one_pair
    return HandStrengths.high_card


def solve_day7_part1(hands: List[Hand]):
    hands.sort()
    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i+1) * hand.bid
    return winnings

def solve_day7_part2(hands: List[JokerHand]):
    hands.sort()
    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i+1) * hand.bid
    return winnings

def get_input(use_jokers = True):
    with open('day7input.txt') as f:
        lines = f.readlines()
    hands = []
    for line in lines:
        hand, bid = line.split()
        if use_jokers:
            hands.append(JokerHand(hand, (int(bid))))
        else:
            hands.append(Hand(hand, int(bid)))
    return hands


if __name__ == '__main__':
    print(f'Part 1: {solve_day7_part1(get_input(use_jokers=False))}')
    print(f'Part 2: {solve_day7_part2(get_input(use_jokers=True))}')
