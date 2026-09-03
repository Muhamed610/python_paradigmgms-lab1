"""
Индивидуальный вариант № 1: Найти сумму квадратов положительных чисел.
"""

numbers = [4, -7, 2, -9, 12, -5, 8, 3]

# 1. Императивный стиль
def solve_imperative(data):
    total = 0
    for n in data:
        if n > 0:
            total += n ** 2
    return total

# 2. Процедурный стиль
def is_positive(n: int) -> bool:
    return n > 0

def square(n: int) -> int:
    return n ** 2

def solve_procedural(data: list) -> int:
    total = 0
    for n in data:
        if is_positive(n):
            total += square(n)
    return total

# 3. Объектно-ориентированный стиль
class PositiveSquareSummator:
    def __init__(self, data):
        self._data = list(data)

    def calculate(self) -> int:
        return sum(n ** 2 for n in self._data if n > 0)

# 4. Функциональный стиль
def solve_functional(data):
    return sum(map(lambda n: n ** 2, filter(lambda n: n > 0, data)))


if __name__ == "__main__":
    print("Императивный:", solve_imperative(numbers))
    print("Процедурный:", solve_procedural(numbers))
    print("ООП:", PositiveSquareSummator(numbers).calculate())
    print("Функциональный:", solve_functional(numbers))