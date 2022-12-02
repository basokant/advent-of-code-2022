move_to_points_map = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

move_beats_map = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

p_move_map = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

o_move_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

def get_move_beats(move: str) -> str:
    return move_beats_map[move]

def get_move_points(move: str) -> int:
    return move_to_points_map[move]

def get_outcome_points(player: str, opponent: str) -> int:
    if player == opponent:
        return 3
    elif get_move_beats(player) == opponent:
        return 6
    else:
        return 0

def get_round_points(player: str, opponent: str) -> int:
    move_points = get_move_points(player)
    outcome_points = get_outcome_points(player, opponent)

    return move_points + outcome_points


# Part 1
def get_total_points1(file_path: str) -> int:
    total_points = 0
    with open(file_path) as file:
        for line in file:
            opponent = o_move_map[line[0]]
            player = p_move_map[line[2]]

            total_points += get_round_points(player, opponent)
    
    return total_points

print(get_total_points1("./test.txt"))
print(get_total_points1("./input.txt"))


# Part 2
outcome_map = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

move_loses_map = {
    'scissors': 'rock',
    'rock': "paper",
    'paper': "scissors"
}

def player_action(opponent: str, outcome: int) -> str:
    if (outcome == 0):
        return move_beats_map[opponent]
    elif (outcome == 3):
        return opponent
    elif (outcome == 6):
        return move_loses_map[opponent]

def get_total_points2(file_path: str) -> int:
    total_points = 0
    with open(file_path) as file:
        for line in file:
            opponent = o_move_map[line[0]]
            outcome = outcome_map[line[2]]
            move = player_action(opponent, outcome)
            # print(opponent, outcome, move)

            move_points = get_move_points(move)
            total_points += move_points + outcome

    return total_points


print(get_total_points2("./test.txt"))
print(get_total_points2("./input.txt"))