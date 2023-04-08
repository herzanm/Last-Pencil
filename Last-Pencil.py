from random import randint


def check_amount_of_pencils(players_input):
    while True:
        if not players_input.isdigit():
            print("The number of pencils should be numeric")
            players_input = input()
        elif int(players_input) == 0:
            print("The number of pencils should be positive")
            players_input = input()
        else:
            return int(players_input)


def set_players():
    first = str(input("Who will be the first (John, Jack):"))

    while first != "John" and first != "Jack":
        print("Choose between 'John' and 'Jack'")
        first = str(input())

    if first == "John":
        second = str("Jack")
    else:
        second = str("John")

    return first, second


def check_discarded_pencils(pencils, discard):
    possible_options = ['1', '2', '3']
    while True:
        if discard not in possible_options:
            print("Possible values: '1', '2' or '3'")
            discard = input()
        elif int(discard) > int(pencils):
            print("Too many pencils were taken")
            discard = input()
        else:
            return int(discard)


def bots_move(pencils):
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 1 and pencils != 1:
        return randint(1, 3)
    elif pencils % 4 == 2 or pencils == 1:
        return 1
    else:
        return 2


# Get amount of pencils to start with and check the conditions
amount_of_pencils = input("How many pencils would you like to use:")
amount_of_pencils = check_amount_of_pencils(amount_of_pencils)

# Getting name of the first player
first_player, second_player = set_players()

player_turn = int(0)
discard_pencils = int(0)

while amount_of_pencils > 0:
    print('|' * amount_of_pencils)
    if player_turn == 0:
        print(first_player + "'s turn:")
        if first_player == "John":
            discard_pencils = input()
            discard_pencils = check_discarded_pencils(amount_of_pencils, discard_pencils)
        else:
            discard_pencils = bots_move(amount_of_pencils)
            print(discard_pencils)
        amount_of_pencils = amount_of_pencils - discard_pencils
        player_turn += 1
    else:
        print(second_player + "'s turn:")
        if second_player == "John":
            discard_pencils = input()
            discard_pencils = check_discarded_pencils(amount_of_pencils, discard_pencils)
        else:
            discard_pencils = bots_move(amount_of_pencils)
            print(discard_pencils)
        amount_of_pencils = amount_of_pencils - discard_pencils
        player_turn -= 1

if player_turn == 0:
    print(first_player + " won!")
else:
    print(second_player + " won!")
