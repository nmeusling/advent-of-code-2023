from src.day5.day5 import Range, Map


def test_range_get_destination_value_from_range():
    range_map = Range(50, 98, 2)
    assert range_map.get_destination_value_from_range(97) == 97
    assert range_map.get_destination_value_from_range(98) == 50
    assert range_map.get_destination_value_from_range(99) == 51
    assert range_map.get_destination_value_from_range(100) == 100

def test_map_get_mapped_value():
    seed_map = Map([Range(50, 98, 2), Range(52, 50, 48)])
    assert seed_map.get_mapped_value(49) == 49
    assert seed_map.get_mapped_value(50) == 52
    assert seed_map.get_mapped_value(97) == 99
    assert seed_map.get_mapped_value(98) == 50
    assert seed_map.get_mapped_value(99) == 51
    assert seed_map.get_mapped_value(100) == 100