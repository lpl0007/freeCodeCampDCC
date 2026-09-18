def squares_with_three(n):
    threes = 0
    for i in range(1, n + 1):
        if str(i * i).count("3") > 0:
            threes += 1
    return threes
