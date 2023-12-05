def get_input():
    with open('day3input.txt') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def is_special_character(c):
    return c != "." and not c.isdigit()


def is_part_number(length, start_row, start_column, schematic):
    end_column = length + start_column -1
    end_row = start_row
    if start_row > 0:
        start_row = start_row - 1
    if start_column > 0:
        start_column = start_column - 1
    if end_row < len(schematic) - 1:
        end_row += 1
    if end_column < len(schematic[0]) - 1:
        end_column += 1

    for i in range(start_row, end_row + 1):
        for j in range(start_column, end_column + 1):
            if is_special_character(schematic[i][j]):
                return True
    return False


def get_ints_from_line(line: str):
    i=0
    found_numbers = []
    is_number = False
    length = 1
    start_i = -1
    while i <= len(line):
        if i == len(line):
            if is_number:
                found_numbers.append((start_i, length))
            return found_numbers

        if line[i].isdigit():
            if is_number:
                length += 1
            else:
                is_number = True
                start_i = i
        else:
            if is_number:
                found_numbers.append((start_i, length))
                is_number = False
                length = 1
        i += 1
    return found_numbers


def solve_day3_part1(schematic):
    sum = 0
    for row_number, row_contents in enumerate(schematic):
        numbers = get_ints_from_line(row_contents)
        for start, length in numbers:
            if is_part_number(length, row_number, start, schematic):
                sum += int(row_contents[start:start+length])

    return sum


if __name__ == '__main__':
    input = get_input()
    print(f"Part 1: {solve_day3_part1(input)}")
