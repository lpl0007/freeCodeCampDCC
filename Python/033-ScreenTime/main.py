def too_much_screen_time(hours):
    return (
        max(hours) >= 10
        or any(sum(hours[i:i + 3]) / 3 >= 8 for i in range(5))
        or sum(hours) / 7 >= 6
    )
