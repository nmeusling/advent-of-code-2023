from typing import List


class Range:
    def __init__(self, destination_start, source_start, length):
        self.destination_start = destination_start
        self.source_start = source_start
        self.length = length

    def get_destination_value_from_range(self, source):
        difference = source - self.source_start
        if 0 <= difference < self.length:
            return self.destination_start + difference
        return source

    def get_source_value_from_range(self, destination):
        difference = destination - self.destination_start
        if 0 <= difference < self.length:
            return self.source_start + difference
        return destination


class Map:
    def __init__(self, ranges: List[Range]):
        self.ranges = ranges

    def get_mapped_value(self, source):
        for range_map in self.ranges:
            new_value = range_map.get_destination_value_from_range(source)
            if new_value != source:
                return new_value
        return source

    def get_mapped_source_value(self, destination):
        for range_map in self.ranges:
            new_value = range_map.get_source_value_from_range(destination)
            if new_value != destination:
                return new_value
        return destination

    def get_ranges_by_ascending_destination(self):
        return sorted(self.ranges, key=lambda x: x.destination_start)


def get_fully_mapped_value(source, maps):
    current_value = source
    for seed_map in maps:
        current_value = seed_map.get_mapped_value(current_value)
    return current_value

def get_seed_from_location(location, maps):
    current_value = location
    for seed_map in reversed(maps):
        current_value = seed_map.get_mapped_source_value(current_value)
    return current_value

def get_input():
    with open('day5input.txt') as f:
        lines = f.readlines()
    seeds = []
    maps = []
    i = 0
    while i < len(lines):
        if 'seeds: ' in lines[i]:
            seeds = extract_seeds(lines[i])
        elif 'map:' in lines[i]:
            map_end = i
            while map_end < len(lines) and lines[map_end] != '\n':
                map_end += 1
            ranges = []
            for j in range(i+1, map_end):
                ranges.append(extract_range(lines[j]))

            maps.append(Map(ranges))
            i=map_end
        i += 1

    return seeds, maps


def extract_seeds(line):
            seeds = line.split(':')[-1]
            seeds = seeds.split()
            return [int(seed) for seed in seeds]


def extract_range(line):
    destination_start, source_start, length = line.split()
    return Range(int(destination_start), int(source_start), int(length))


def solve_day5_part1(seeds, maps):
    locations = []
    for seed in seeds:
        locations.append(get_fully_mapped_value(seed, maps))
    return min(locations)


def solve_day5_part2(seeds, maps):
    locations = []
    min_location = get_fully_mapped_value(seeds[0], maps)
    for i in range(0, len(seeds), 2):
        print(f"Start Seed: {seeds[i]}. Length: {seeds[i+1]}")
        start_seed = seeds[i]
        length = seeds[i+1]
        for current_seed in range(start_seed, start_seed+length):
            location = get_fully_mapped_value(current_seed, maps)
            if location < min_location:
                min_location = location
            locations.append(location)
            # print(f"Seed: {current_seed}. Value: {location}")
    return min_location


def is_seed_in_range(seed, seeds):
    for i in range(0, len(seeds), 2):
        if seeds[i] <= seed < seeds[i]+seeds[i+1]:
            return True
    return False

def solve_day5_part2_reverse(seeds, maps):
    location_maps = maps[-1]
    sorted_location_map = location_maps.get_ranges_by_ascending_destination()
    min_location_range = sorted_location_map[0].destination_start
    for i in range(min_location_range):
        seed = get_seed_from_location(i, maps)
        if is_seed_in_range(seed, seeds):
            return i
    for location_range in sorted_location_map:
        for i in range(location_range.destination_start, location_range.destination_start + location_range.length):
            seed = get_seed_from_location(i, maps)
            if is_seed_in_range(seed, seeds):
                return i


if __name__ == '__main__':
    seeds, maps = get_input()
    print(f"Part 1: {solve_day5_part1(seeds, maps)}")
    # print(f"Part 2: {solve_day5_part2(seeds, maps)}")
    print(f"Part 2: {solve_day5_part2_reverse(seeds, maps)}")
