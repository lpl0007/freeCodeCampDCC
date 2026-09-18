def is_valid_number(n, base):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    validDigits = digits[:base]
    count = 0
    n = n.upper()
    for j in validDigits:
        count += n.count(j)
    if count == len(n):
        return True
    else:
        return False
