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

def is_game_possible(game, limits):
    for turn in game[1]:
        counts = count_cubes(turn)
        if any(counts[color] > limits[color] for color in counts):
            return False
    return True

def sum_possible_game_ids(game_data, red_limit, green_limit, blue_limit):
    games = parse_game_data(game_data)
    limits = {'red': red_limit, 'green': green_limit, 'blue': blue_limit}
    return sum(game[0] for game in games if is_game_possible(game, limits))

game_data = open("input.txt", "r").read()

sum_of_ids = sum_possible_game_ids(game_data, 12, 13, 14)
print(f"The sum of the IDs of the games that are possible: {sum_of_ids}")
