def parse_roman_numeral(numeral):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0

    for i in range(len(numeral)):
        if i + 1 < len(numeral) and values[numeral[i]] < values[numeral[i + 1]]:
            total -= values[numeral[i]]
        else:
            total += values[numeral[i]]
    return total
