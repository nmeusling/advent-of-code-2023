from day1 import extract_digits, get_calibration_value, sum_all_calibration_values

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