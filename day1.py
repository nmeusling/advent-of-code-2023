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

def replace_first_and_last_written_numbers(text: str):
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
    # replace first word digit
    updated_text = text
    for i in range(len(text)):
        to_replace = None
        substring = text[i:i+3]
        if substring in digit_replacements:
            to_replace = substring
        substring = text[i:i+4]
        if substring in digit_replacements:
            to_replace = substring
        substring = text[i:i+5]
        if substring in digit_replacements:
            to_replace = substring
        
        if to_replace:
            updated_text = text.replace(to_replace, digit_replacements[to_replace])
            break
     

    # replace last word digit
    final_text = updated_text
    for i in range(len(updated_text)-1, -1, -1):
        to_replace = None
        substring = updated_text[i-3+1:i+1]
        if substring in digit_replacements:
            to_replace = substring
        substring = updated_text[i-4+1:i+1]
        if substring in digit_replacements:
            to_replace = substring
        substring = updated_text[i-5+1:i+1]
        if substring in digit_replacements:
            to_replace = substring
            
        if to_replace:
            final_text = updated_text.replace(to_replace, digit_replacements[to_replace])
            break
    return final_text

def get_calibration_value(text: str, replace_digits: bool = False):
    if replace_digits:
        text = replace_first_and_last_written_numbers(text)
    digits = extract_digits(text)
    return int(digits[0]+digits[-1])

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
