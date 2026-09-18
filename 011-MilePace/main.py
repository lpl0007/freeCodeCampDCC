def mile_pace(miles, duration):
    duration = duration.split(":")
    seconds = ((int(duration[0]) * 60) + int(duration[1])) / miles
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"
