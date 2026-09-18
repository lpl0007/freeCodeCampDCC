def to_camel_case(s):
    words = s.replace("-", " ").replace("_", " ").split()

    result = words[0].lower()

    for word in words[1:]:
        result += word.capitalize()

    return result
