def parse_game_data(game_data):
    games = []
    for game in game_data.strip().split("\n"):
        if ": " in game:
            game_id, turns = game.split(": ")
            game_id = int(game_id.split(" ")[1])
            turns = [turn.split(", ") for turn in turns.split("; ")]
            games.append((game_id, turns))
    return games

def count_cubes(turn):
    counts = {'red': 0, 'green': 0, 'blue': 0}
    for cube_info in turn:
        count, color = cube_info.split(" ")
        counts[color] += int(count)
    return counts

def find_minimum_cubes(game):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for turn in game:
        counts = count_cubes(turn)
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], counts[color])
    return min_cubes

def calculate_power_of_set(cubes_set):
    return cubes_set['red'] * cubes_set['green'] * cubes_set['blue']

def sum_powers_of_minimum_sets(game_data):
    games = parse_game_data(game_data)
    total_power = 0
    for _, turns in games:
        min_cubes = find_minimum_cubes(turns)
        total_power += calculate_power_of_set(min_cubes)
    return total_power

game_data = open("input.txt", "r").read()
sum_of_powers = sum_powers_of_minimum_sets(game_data)
print(f"The sum of the powers of the minimum sets of cubes for the games is: {sum_of_powers}")