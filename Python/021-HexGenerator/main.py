import random


def generate_hex(color):
    if color not in ["red", "green", "blue"]:
        return "Invalid color"

    values = [random.randint(0, 255) for _ in range(3)]

    if color == "red":
        values[0] = random.randint(max(values[1], values[2]) + 1, 255)
    elif color == "green":
        values[1] = random.randint(max(values[0], values[2]) + 1, 255)
    else:
        values[2] = random.randint(max(values[0], values[1]) + 1, 255)

    return "".join(f"{value:02X}" for value in values)
