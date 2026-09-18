def battle(my_army, opposing_army):
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        return "We retreated"

    my_wins = 0
    opposing_wins = 0

    for my_character, opposing_character in zip(my_army, opposing_army):
        if my_character.islower():
            my_strength = ord(my_character) - ord("a") + 1
        elif my_character.isupper():
            my_strength = ord(my_character) - ord("A") + 27
        elif my_character.isdigit():
            my_strength = int(my_character)
        else:
            my_strength = 0

        if opposing_character.islower():
            opposing_strength = ord(opposing_character) - ord("a") + 1
        elif opposing_character.isupper():
            opposing_strength = ord(opposing_character) - ord("A") + 27
        elif opposing_character.isdigit():
            opposing_strength = int(opposing_character)
        else:
            opposing_strength = 0

        if my_strength > opposing_strength:
            my_wins += 1
        elif opposing_strength > my_strength:
            opposing_wins += 1

    if my_wins > opposing_wins:
        return "We won"
    elif my_wins < opposing_wins:
        return "We lost"
    else:
        return "It was a tie"
