def evaluate(numbers, operators):
    result = numbers[0]

    for i in range(1, len(numbers)):
        operator = operators[(i - 1) % len(operators)]
        number = numbers[i]

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number
        elif operator == "*":
            result *= number
        elif operator == "/":
            result /= number
        elif operator == "%":
            result %= number

    return result
