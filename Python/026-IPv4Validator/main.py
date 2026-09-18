def is_valid_ipv4(ipv4):
    parts = ipv4.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        if len(part) > 1 and part[0] == "0":
            return False

        value = int(part)

        if value > 255:
            return False

    return True
