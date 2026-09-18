def array_diff(arr1, arr2):
    return sorted(set(arr1) ^ set(arr2))