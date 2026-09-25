def second_largest(numbers):
    largest = float("-inf")
    second = float("-inf")

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number

    return second
