def capitalize(paragraph):
    result = ""
    capitalize_next = True

    for character in paragraph:
        if capitalize_next and character.isalpha():
            result += character.upper()
            capitalize_next = False
        else:
            result += character

        if character == "." or character == "?" or character == "!":
            capitalize_next = True

    return result
