from day1 import extract_digits, get_calibration_value, sum_all_calibration_values, replace_first_and_last_written_numbers

def test_extract_digits():
    assert(extract_digits("1abc2")) == "12"
    assert(extract_digits("pqr3stu8vwx")) == "38"
    assert(extract_digits("a1b2c3d4e5f")) == "12345"
    assert(extract_digits("treb7uchet")) == "7"

def test_get_calibration_value():
    assert(get_calibration_value("1abc2")) == 12
    assert(get_calibration_value("pqr3stu8vwx")) == 38
    assert(get_calibration_value("a1b2c3d4e5f")) == 15
    assert(get_calibration_value("treb7uchet")) == 77

def test_sum_all_calibration_values():
    text_values = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert sum_all_calibration_values(text_values) == 142

def test_sum_all_calibration_values_with_replacement():
    text_values = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    assert sum_all_calibration_values(text_values, replace_digits=True) == 281

def test_replace_written_numbers():
    assert replace_first_and_last_written_numbers("two1nine") == "219"
    assert replace_first_and_last_written_numbers("eightwothree") == "8wo3"
    assert replace_first_and_last_written_numbers("abcone2threexyz") == "abc123xyz"
    assert replace_first_and_last_written_numbers("xtwone3four") == "x2ne34"
    assert replace_first_and_last_written_numbers("4nineeightseven2") == "49eight72"
    assert replace_first_and_last_written_numbers("zoneight234") == "z1ight234"
    assert replace_first_and_last_written_numbers("7pqrstsixteen") == "7pqrst6teen"
    assert replace_first_and_last_written_numbers("342dfafdsfead") == "342dfafdsfead"
