# Change while for zip
# Review error durig theta1 calculation

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

def calculate_tmp0(real_prices: list[float], predicted_prices: list[float], learning_rate: float) -> float:
    i = 0
    total = 0

    while i < len(real_prices):
        total += abs(predicted_prices[i] - real_prices[i])
        i = i + 1

    tmp0 = learning_rate * (total / len(real_prices))
    return tmp0

def calculate_tmp1(real_prices: list[float], predicted_prices: list[float], mileages: list[float], learning_rate: float) -> float:
    i = 0
    total = 0

    while i < len(real_prices):
        total += (predicted_prices[i] - real_prices[i]) * mileages[i] 
        i = i + 1

    tmp1 = learning_rate * (total / len(real_prices))
    return tmp1

def new_theta0_theta1(theta0: float, theta1: float, tmp0: float, tmp1: float) -> tuple[float, float]: 
     theta0 = theta0 - tmp0
     theta1 = theta1 - tmp1
     return theta0, theta1


