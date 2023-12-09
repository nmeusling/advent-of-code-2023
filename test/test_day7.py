from src.day7.day7 import get_hand_type, HandStrengths, compare_hands, Hand, solve_day7_part1, solve_day7_part2, \
    JokerHand


def test_get_hand_type():
    assert get_hand_type('33333', use_jokers=False) == HandStrengths.five_of_a_kind
    assert get_hand_type('3333K', use_jokers=False) == HandStrengths.four_of_a_kind
    assert get_hand_type('32332', use_jokers=False) == HandStrengths.full_house
    assert get_hand_type('32T33', use_jokers=False) == HandStrengths.three_of_a_kind
    assert get_hand_type('3223K', use_jokers=False) == HandStrengths.two_pair
    assert get_hand_type('32T3K', use_jokers=False) == HandStrengths.one_pair
    assert get_hand_type('32TJK', use_jokers=False) == HandStrengths.high_card


def test_get_hand_type_with_jokers():
    assert get_hand_type('222JJ', use_jokers=True) == HandStrengths.five_of_a_kind
    assert get_hand_type('2222J', use_jokers=True) == HandStrengths.five_of_a_kind
    assert get_hand_type('222J3', use_jokers=True) == HandStrengths.four_of_a_kind
    assert get_hand_type('22JJ3', use_jokers=True) == HandStrengths.four_of_a_kind
    assert get_hand_type('2JJJ3', use_jokers=True) == HandStrengths.four_of_a_kind
    assert get_hand_type('22J33', use_jokers=True) == HandStrengths.full_house
    assert get_hand_type('22J34', use_jokers=True) == HandStrengths.three_of_a_kind
    assert get_hand_type('2JJ34', use_jokers=True) == HandStrengths.three_of_a_kind
    assert get_hand_type('2345J', use_jokers=True) == HandStrengths.one_pair


def test_compare_hands():
    assert compare_hands('3223K', '3423K', use_jokers=False) > 0
    assert compare_hands('3443K', '3223K', use_jokers=False) > 0
    assert compare_hands('3223K', '3223K', use_jokers=False) == 0
    assert compare_hands('3223K', '3333K', use_jokers=False) < 0
    assert compare_hands('3223K', '3443K', use_jokers=False) < 0


def test_compare_hands_with_jokers():
    assert compare_hands('222JJ', '33334', use_jokers=True) > 0
    assert compare_hands('222J3', '32567', use_jokers=True) > 0
    assert compare_hands('222JJ', '222JJ', use_jokers=True) == 0
    assert compare_hands('222J3', '33337', use_jokers=True) < 0


def test_day7_part1():
    hands = [Hand('32T3K', 765), Hand('T55J5', 684), Hand('KK677', 28), Hand('KTJJT', 220), Hand('QQQJA', 483)]
    assert solve_day7_part1(hands) == 6440


def test_day7_part2():
    hands = [JokerHand('32T3K', 765), JokerHand('T55J5', 684), JokerHand('KK677', 28), JokerHand('KTJJT', 220), JokerHand('QQQJA', 483)]
    assert solve_day7_part2(hands) == 5905