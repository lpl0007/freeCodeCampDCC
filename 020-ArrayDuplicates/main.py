def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for number in arr:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return sorted(duplicates)
