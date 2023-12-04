def get_input():
    with open('day1input.txt') as f:
        lines = f.readlines()
    return lines


def extract_digits(text: str):
    digits = ""
    for char in text:
        if char.isdigit():
            digits += char
    return digits


def get_possible_substrings(text, i, reverse=False):
    if reverse:
        return [text[i - 3 + 1:i + 1], text[i - 4 + 1:i + 1], text[i - 5 + 1:i + 1]]
    return [text[i:i + 3], text[i:i + 4], text[i:i + 5]]


def replace_written_number(text: str, reverse=False):
    digit_replacements = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    if reverse:
        indices = range(len(text) - 1, -1, -1)
    else:
        indices = range(len(text))

    for i in indices:
        possible_substrings = get_possible_substrings(text, i, reverse=reverse)
        for substring in possible_substrings:
            if substring in digit_replacements:
                return text.replace(substring, digit_replacements[substring])
    return text


def replace_first_and_last_written_numbers(text: str):
    text = replace_written_number(text, reverse=False)
    text = replace_written_number(text, reverse=True)
    return text


def get_calibration_value(text: str, replace_digits: bool = False):
    if replace_digits:
        text = replace_first_and_last_written_numbers(text)
    digits = extract_digits(text)
    return int(digits[0] + digits[-1])


def sum_all_calibration_values(text_values: list, replace_digits: bool = False):
    sum = 0
    for text in text_values:
        calibration_value = get_calibration_value(text, replace_digits)
        sum += calibration_value
    return sum


def solve_day_1_part_1():
    text_values = get_input()
    return sum_all_calibration_values(text_values)


def solve_day_1_part_2():
    text_values = get_input()
    return sum_all_calibration_values(text_values, replace_digits=True)


if __name__ == '__main__':
    print(f"Part 1: {solve_day_1_part_1()}")
    print(f"Part 2: {solve_day_1_part_2()}")
