def get_laptop_cost(laptops, budget):
    most_expensive = 0
    second_most_expensive = 0
    affordable = 0

    for laptop in set(laptops):
        if laptop <= budget and laptop > affordable:
            affordable = laptop

        if laptop > most_expensive:
            second_most_expensive = most_expensive
            most_expensive = laptop
        elif laptop > second_most_expensive:
            second_most_expensive = laptop

    if second_most_expensive <= budget:
        return second_most_expensive
    elif affordable > 0:
        return affordable
    else:
        return 0
