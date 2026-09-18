def rotate(matrix):
    rotated = []

    for column in range(len(matrix[0])):
        new_row = []

        for row in range(len(matrix) - 1, -1, -1):
            new_row.append(matrix[row][column])

        rotated.append(new_row)

    return rotated
