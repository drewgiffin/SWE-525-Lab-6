def calculate_total(prices):
    """Return the average price, or 0 if prices is empty."""
    if not prices:
        return 0
    return sum(prices) / len(prices)