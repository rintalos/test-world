import os
from scripts.validate import Height, Weight


def calculate_bmi(weight: float, height: float) -> float:
    if height <= 0 or weight <= 0:
        raise ValueError

    return weight / (height**2)


if __name__ == "__main__":
    try:
        height_input = float(os.environ["HEIGHT"])
        weight_input = float(os.environ["WEIGHT"])

        height = Height(height_input)
        weight = Weight(weight_input)

    except KeyError:
        print("Error: 環境変数 HEIGHT または WEIGHT が設定されていません")
        exit(1)
    except ValueError:
        print("Error: HEIGHT または WEIGHT が数値ではありません")
        exit(1)

    bmi = calculate_bmi(weight.value, height.value)
    print(f"BMI: {bmi:.2f}")
