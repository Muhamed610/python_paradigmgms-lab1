from typing import List

def is_even(number: int) -> bool:
    return number % 2 == 0

def square(number: int) -> int:
    return number ** 2

def get_even_numbers(values: List[int]) -> List[int]:
    return [n for n in values if is_even(n)]

def sum_even_squares(values: List[int]) -> int:
    total = 0
    for number in values:
        if is_even(number):
            total += square(number)
    return total

if __name__ == "__main__":
    numbers = [4, -7, 2, -9, 12, -5, 8, 3]
    # Отдельная проверка функций
    print("Проверка is_even(4):", is_even(4))
    print("Проверка square(5):", square(5))
    print("Чётные числа:", get_even_numbers(numbers))
    print("Сумма квадратов чётных чисел:", sum_even_squares(numbers))