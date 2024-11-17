import math

def compare_hypotenuses(a1, b1, a2, b2):
    hypotenuse1 = math.sqrt(a1 ** 2 + b1 ** 2)
    hypotenuse2 = math.sqrt(a2 ** 2 + b2 ** 2)

    print(f"Гипотенуза 1: {hypotenuse1}, Гипотенуза 2: {hypotenuse2}")
    print(
        "Гипотенуза 1 больше." if hypotenuse1 > hypotenuse2 else "Гипотенуза 2 больше." if hypotenuse1 < hypotenuse2 else "Гипотенузы равны.")

compare_hypotenuses(3, 4, 6, 8)