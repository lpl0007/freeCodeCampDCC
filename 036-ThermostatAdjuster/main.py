def adjust_thermostat(current, target):
    if current < target:
        return "heat"
    elif current > target:
        return "cool"
    else:
        return "hold"
