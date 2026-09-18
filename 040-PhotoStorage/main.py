def number_of_photos(photo_size, hard_drive_capacity):
    capacity_mb = hard_drive_capacity * 1000
    return int(capacity_mb / photo_size)
