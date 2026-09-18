def find_target(arr, target):
    for i in arr:
        try:
            position = arr.index(target - i)
            if arr.index(i) != position:
                return [arr.index(i), position]
        except ValueError:
            position = -1
    return "Target not found"
