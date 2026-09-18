def decode(message, shift):
    shift %= 26
    text = ""

    for char in message:
        if char.islower():
            base = ord("a")
            text += chr((ord(char) - base - shift) % 26 + base)
        elif char.isupper():
            base = ord("A")
            text += chr((ord(char) - base - shift) % 26 + base)
        else:
            text += char

    return text
