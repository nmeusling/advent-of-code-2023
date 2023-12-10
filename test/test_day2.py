from src.day2.day2 import Round, get_dice_amounts


def test_get_dice_amounts():
    dice = get_dice_amounts('1 blue, 2 green')
    assert dice.blue == 1
    assert dice.green == 2
    assert dice.red == 0

    dice = get_dice_amounts('12 red, 21 blue, 2 green')
    assert dice.blue == 21
    assert dice.green == 2
    assert dice.red == 12