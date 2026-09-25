def second_largest(numbers):
    largest = max(numbers)
    second = float("-inf")

    for number in numbers:
        if number < largest and number > second:
            second = number

    return second
