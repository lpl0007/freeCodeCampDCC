def digits_or_letters(text):
    digits = 0
    letters = 0

    for character in text:
        if character.isdigit():
            digits += 1
        elif character.isalpha():
            letters += 1

    if digits > letters:
        return "digits"
    elif letters > digits:
        return "letters"
    else:
        return "tie"
