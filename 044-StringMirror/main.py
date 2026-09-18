def is_mirror(first, second):
    first_letters = ""
    second_letters = ""

    for character in first:
        if character.isalpha():
            first_letters += character

    for character in second:
        if character.isalpha():
            second_letters += character

    return first_letters == second_letters[::-1]
