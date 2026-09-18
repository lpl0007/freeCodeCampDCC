def tribonacci_sequence(start_sequence, length):
    sequence = []
    if length != 0:
        sequence.append(start_sequence[0])
        if length != 1:
            sequence.append(start_sequence[1])
            if length != 2:
                sequence.append(start_sequence[2])
    if length > 3:
        for i in range(length-3):
            sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2] + sequence[len(sequence)-3])
    return sequence
