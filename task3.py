from typing import List

class NumberCollection:
    def __init__(self, numbers: List[int]):
        # Атрибут self._numbers является защищенным (protected) 
        # и хранит внутреннее состояние объекта
        self._numbers = list(numbers)

    def get_even_numbers(self) -> List[int]:
        return [n for n in self._numbers if n % 2 == 0]

    def count_even_numbers(self) -> int:
        return len(self.get_even_numbers())

    def find_maximum(self) -> int:
        return max(self._numbers) if self._numbers else 0

    def calculate_average(self) -> float:
        return sum(self._numbers) / len(self._numbers) if self._numbers else 0.0

    def sum_even_squares(self) -> int:
        return sum(n ** 2 for n in self._numbers if n % 2 == 0)

if __name__ == "__main__":
    col1 = NumberCollection([4, -7, 2, -9, 12, -5, 8, 3])
    print("Коллекция 1 - Чётные:", col1.get_even_numbers())
    print("Коллекция 1 - Кол-во чётных:", col1.count_even_numbers())
    print("Коллекция 1 - Максимум:", col1.find_maximum())
    print("Коллекция 1 - Среднее:", col1.calculate_average())
    print("Коллекция 1 - Сумма квадратов чётных:", col1.sum_even_squares())

    # Второй объект с другим набором чисел
    col2 = NumberCollection([10, 15, 20, 25, 30])
    print("\nКоллекция 2 - Сумма квадратов чётных:", col2.sum_even_squares())