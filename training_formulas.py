theta0 = 0
theta1 = 0

def estimate_price(mileage_list: list[float], theta0: float, theta1: float) -> list[float]:
    predicted_prices = []

    for mileage in mileage_list:
        predicted_prices.append((mileage * theta1) + theta0)

    return predicted_prices

def calculate_mae(real_prices: list[float], predicted_prices: list[float]) -> float:
    i = 0
    total = 0
    # Protect empty list and different sizes lists

    while i < len(real_prices):
        total += abs(predicted_prices[i] - real_prices[i])
        i = i + 1

    mae = total / len(real_prices)
    return mae

# Next: Implement subject formulas and training loop