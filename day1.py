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

def get_calibration_value(text: str):
    digits = extract_digits(text)
    return int(digits[0]+digits[-1])

def sum_all_calibration_values(text_values: list):
    sum = 0
    for text in text_values:
        calibration_value = get_calibration_value(text)
        sum += calibration_value
    return sum

def solve_day_1_part_1():
    text_values = get_input()
    return sum_all_calibration_values(text_values)

if __name__ == '__main__':
    print(f"Part 1: {solve_day_1_part_1()}")
