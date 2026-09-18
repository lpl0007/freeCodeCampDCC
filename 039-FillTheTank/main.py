def cost_to_fill(tankSize, fuelLevel, pricePerGallon):
    gallons_needed = tankSize - fuelLevel
    cost = gallons_needed * pricePerGallon

    return f"${cost:.2f}"
