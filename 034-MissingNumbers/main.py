def find_missing_numbers(numbers):
    missing_numbers = []

    largest_number = max(numbers)

    for number in range(1, largest_number + 1):
        if number not in numbers:
            missing_numbers.append(number)

    return missing_numbers
