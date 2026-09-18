def burn_candles(candles, leftovers_needed):
    total = candles
    leftovers = candles

    while leftovers >= leftovers_needed:
        new_candles = leftovers // leftovers_needed
        leftovers = leftovers % leftovers_needed + new_candles
        total += new_candles

    return total
