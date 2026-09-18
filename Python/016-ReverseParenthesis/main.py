def decode(s):
    stack = []

    for char in s:
        if char == "(":
            stack.append("")
        elif char == ")":
            text = stack.pop()[::-1]

            if stack:
                stack[-1] += text
            else:
                stack.append(text)
        else:
            if stack:
                stack[-1] += char
            else:
                stack.append(char)

    return "".join(stack)
