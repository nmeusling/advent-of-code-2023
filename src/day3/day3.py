def get_input():
    with open('day3input.txt') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def is_special_character(c):
    return c != "." and not c.isdigit()


def is_part_number(length, start_row, start_column, schematic):
    end_column = length + start_column - 1
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
    i = 0
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


def get_adjacent_parts(row, column, schematic):
    start_row = row
    end_row = row
    start_column = column
    end_column = column
    if row > 0:
        start_row = row - 1
    if row < len(schematic) - 1:
        end_row = row + 1
    if column > 0:
        start_column = column - 1
    if column < len(schematic[0]) - 1:
        end_column = column + 1

    part_numbers = []

    for i in range(start_row, end_row + 1):
        j = start_column
        while j < end_column + 1:
            if schematic[i][j].isdigit():
                part_number, skip = get_number_touching_index(schematic[i], j)
                part_numbers.append(part_number)
                j += skip
            j += 1

    return part_numbers


def get_number_touching_index(row, index):
    is_number = row[index].isdigit()
    pointer = index
    while is_number and pointer > 0:
        is_number = row[pointer - 1].isdigit()
        if is_number:
            pointer = pointer - 1
    start_index = pointer

    is_number = row[index].isdigit()
    while is_number and pointer < len(row) - 1:
        is_number = row[pointer+1].isdigit()
        if is_number:
            pointer = pointer + 1
    end_index = pointer

    return row[start_index:end_index+1], end_index - index


def solve_day3_part1(schematic):
    sum = 0
    for row_number, row_contents in enumerate(schematic):
        numbers = get_ints_from_line(row_contents)
        for start, length in numbers:
            if is_part_number(length, row_number, start, schematic):
                sum += int(row_contents[start:start + length])

    return sum


def solve_day3_part2(schematic):
    sum = 0
    for row_number, row_contents in enumerate(schematic):
        for column_number, char in enumerate(row_contents):
            if char == '*':
                parts = get_adjacent_parts(row_number, column_number, schematic)
                if len(parts) == 2:
                    sum += int(parts[0]) * int(parts[1])
    return sum

if __name__ == '__main__':
    input = get_input()
    print(f"Part 1: {solve_day3_part1(input)}")
    print(f"Part 1: {solve_day3_part2(input)}")
