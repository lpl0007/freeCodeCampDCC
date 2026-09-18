def convert(number):
    digit1 = number // 16
    digit2 = number % 16

    if digit1 == 10:
        digit1 = "a"
    elif digit1 == 11:
        digit1 = "b"
    elif digit1 == 12:
        digit1 = "c"
    elif digit1 == 13:
        digit1 = "d"
    elif digit1 == 14:
        digit1 = "e"
    elif digit1 == 15:
        digit1 = "f"

    if digit2 == 10:
        digit2 = "a"
    elif digit2 == 11:
        digit2 = "b"
    elif digit2 == 12:
        digit2 = "c"
    elif digit2 == 13:
        digit2 = "d"
    elif digit2 == 14:
        digit2 = "e"
    elif digit2 == 15:
        digit2 = "f"

    return str(digit1) + str(digit2)


def rgb_to_hex(rgb):
    rgb = rgb[4:-1]
    rgb = rgb.split(", ")

    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])

    r = convert(r)
    g = convert(g)
    b = convert(b)

    return "#" + r + g + b
