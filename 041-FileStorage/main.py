def number_of_files(file_size, unit, hard_drive_capacity):
    if unit == "B":
        file_size = file_size / 1000000000
    elif unit == "KB":
        file_size = file_size / 1000000
    elif unit == "MB":
        file_size = file_size / 1000

    return int(hard_drive_capacity / file_size)
