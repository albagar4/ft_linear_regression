import sys
import math

# For now, list reads only the mileage of the car

def read_column(path: str, column: int = 0) -> list[float]:
    data_list = []
    with open(path, "r", encoding="utf-8") as file:
        next(file, None)
        for index, line in enumerate(file):
            line = line.strip()
            if not line:
                continue
            try:
                data_list.append(float(line.split(",")[0]))
            except (ValueError, IndexError) as error:
                raise ValueError(f"{path}, line {index}: invalid data") from error
        return data_list

def compute_mean_std(data_list: list[float]) -> tuple[float, float]:
    if not data_list:
        raise ValueError("cannot compute statistics of an empty list")
    
    mean = math.fsum(data_list) / len(data_list)
    variance = math.fsum((v - mean) ** 2 for v in data_list) / len(data_list)
    return mean, math.sqrt(variance)

def standardize(values: list[float], mean: float, std_dev: float) -> list[float]:
    return [(v - mean) / std_dev for v in values]

def main() -> None:
    try:
        mileages = read_column("data.csv", column=0)
        mean, std_dev = compute_mean_std(mileages)
        standardized = standardize(mileages, mean, std_dev)
    except FileNotFoundError:
        print("Error: data.csv not found", file=sys.stderr)
        sys.exit(1)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"mean={mean} std_dev={std_dev}")

if __name__ == '__main__':
    main()