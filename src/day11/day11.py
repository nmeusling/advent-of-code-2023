import itertools


def get_input():
    with open('day11input.txt') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get_galaxy_free_rows_and_columns(space_map):
    rows = []
    columns = []
    for i, row in enumerate(space_map):
        if not has_galaxy(row):
            rows.append(i)

    for i in range(len(space_map)):
        column = [row[i] for row in space_map]
        if not has_galaxy(column):
            columns.append(i)
    return rows, columns


def duplicate_galaxy_free_rows_and_columns(space_map):
    rows, columns = get_galaxy_free_rows_and_columns(space_map)
    for i in reversed(rows):
        space_map.insert(i, space_map[i])

    for i in reversed(columns):
        for row_number in range(len(space_map)):
            space_map[row_number]=space_map[row_number][:i] + "." + space_map[row_number][i:]
    return space_map


def get_all_galaxy_locations(space_map):
    galaxies = []
    for i, row in enumerate(space_map):
        for j, column in enumerate(row):
            if space_map[i][j] == "#":
                galaxies.append((i, j))
    return galaxies


def has_galaxy(row):
    for spot in row:
        if spot == "#":
            return True


def get_shortest_path_between_two_galaxies(first_galaxy, second_galaxy):
    path = abs(first_galaxy[0] - second_galaxy[0]) + abs(first_galaxy[1] - second_galaxy[1])
    return path


def get_shortest_path_with_expansion(first_galaxy, second_galaxy, rows, columns, expansion_amount):
    first_row, first_column = first_galaxy
    second_row, second_column = second_galaxy
    expansions = 0
    for expansion_row in rows:
        if first_row > second_row:
            if second_row < expansion_row < first_row:
                expansions += 1
        else:
            if first_row < expansion_row < second_row:
                expansions += 1
    for expansion_column in columns:
        if first_column > second_column:
            if second_column < expansion_column < first_column:
                expansions += 1
        else:
            if first_column < expansion_column < second_column:
                expansions += 1

    return get_shortest_path_between_two_galaxies(first_galaxy, second_galaxy) + (expansion_amount -1)*expansions


def solve_day11_part1(space_map):
    expanded_space_map = duplicate_galaxy_free_rows_and_columns(space_map)
    galaxies = get_all_galaxy_locations(expanded_space_map)
    total_shortest_path = 0
    for galaxy_pair in itertools.combinations(galaxies, 2):
        total_shortest_path += get_shortest_path_between_two_galaxies(*galaxy_pair)
    return total_shortest_path

def solve_day11_part2(space_map, expansion_amount):
    rows, columns = get_galaxy_free_rows_and_columns(space_map)
    galaxies = get_all_galaxy_locations(space_map)
    total_shortest_path = 0
    for galaxy_pair in itertools.combinations(galaxies, 2):
        new_path = get_shortest_path_with_expansion(*galaxy_pair, rows, columns, expansion_amount)
        total_shortest_path += new_path
    return total_shortest_path


if __name__ == '__main__':
    space_map = get_input()
    print(solve_day11_part1(space_map))
    space_map = get_input()
    print(solve_day11_part2(space_map, 1000000))
