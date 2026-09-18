def number_of_videos(video_size, video_unit, drive_capacity, drive_unit):
    if video_unit not in ["B", "KB", "MB", "GB"]:
        return "Invalid video unit"

    if drive_unit not in ["GB", "TB"]:
        return "Invalid drive unit"

    if video_unit == "B":
        video_size = video_size / 1000000000
    elif video_unit == "KB":
        video_size = video_size / 1000000
    elif video_unit == "MB":
        video_size = video_size / 1000

    if drive_unit == "TB":
        drive_capacity = drive_capacity * 1000

    return int(drive_capacity / video_size)
