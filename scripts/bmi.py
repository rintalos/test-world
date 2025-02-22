import sys


def calculate_bmi(weight: float, height: float) -> float:
    if height <= 0 or weight <= 0:
        raise ValueError

    return weight / (height**2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法 python bmi.py ＜身長＞ ＜体重＞")
        sys.exit(1)

    try:
        height = float(sys.argv[1])
        weight = float(sys.argv[2])
        bmi = calculate_bmi(height, weight)
        print(f"BMI: {bmi:.2f}")
    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)
