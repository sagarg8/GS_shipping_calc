def calculate(options: list, order: int) -> dict:
    options.sort(reverse=True)
    smallest_option = options[-1]
    results = {o: 0 for o in options}
    remainder = order
    for option in options:
        quotient, remainder = divmod(remainder, option)
        if quotient > 0:
            results[option] += quotient

    if 0 < remainder < smallest_option:
        results[smallest_option] += 1

    return results
