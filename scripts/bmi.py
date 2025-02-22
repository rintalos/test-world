import os


def calculate_bmi(weight: float, height: float) -> float:
    if height <= 0 or weight <= 0:
        raise ValueError

    return weight / (height**2)


if __name__ == "__main__":
    try:
        height = float(os.environ["HEIGHT"])
        weight = float(os.environ["WEIGHT"])
    except KeyError:
        print("Error: 環境変数 HEIGHT または WEIGHT が設定されていません")
        exit(1)
    except ValueError:
        print("Error: HEIGHT または WEIGHT が数値ではありません")
        exit(1)

    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi:.2f}")
