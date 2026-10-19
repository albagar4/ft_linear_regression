import sys
import math

def read_data(path: str) -> tuple[list[float], list[float]]:
    mileage_list = []
    price_list = []
    with open(path, "r", encoding="utf-8") as file:
        header = next(file, None)
        if header != "km,price" and header != "km,price\n":
            raise ValueError("Header is not correct")
        
        for index, line in enumerate(file, start=2):
            line = line.strip()
            if not line:
                continue
            try:
                mileage, price = line.split(",")
                if not math.isfinite(float(mileage)) or not math.isfinite(float(mileage)):
                    raise ValueError()
                line = line.split(",")
                mileage_list.append(float(mileage))
                price_list.append(float(price))
            except (ValueError, IndexError) as error:
                raise ValueError(f"{path}, line {index}: invalid data") from error
                
    return mileage_list, price_list

def compute_mean_std(mileages: list[float]) -> tuple[float, float]:
    if not mileages:
        raise ValueError("cannot compute statistics of an empty list")
    
    mean = math.fsum(mileages) / len(mileages)
    variance = math.fsum((v - mean) ** 2 for v in mileages) / len(mileages)
    return mean, math.sqrt(variance)

def standardize(values: list[float], mean: float, std_dev: float) -> list[float]:
    return [(v - mean) / std_dev for v in values]

def main() -> None:
    try:
        mileages, prices = read_data("test.csv")
        print(prices)
        mean, std_dev = compute_mean_std(mileages)
        standardized = standardize(mileages, mean, std_dev)
    except FileNotFoundError:
        print("Error: file not found", file=sys.stderr)
        sys.exit(1)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"mean={mean} std_dev={std_dev}")

if __name__ == '__main__':
    main()