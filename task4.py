numbers = [4, -7, 2, -9, 12, -5, 8, 3]

# Использование map + filter
result_map = sum(
    map(
        lambda n: n ** 2,
        filter(lambda n: n % 2 == 0, numbers)
    )
)

# Использование генераторного выражения
result_gen = sum(n ** 2 for n in numbers if n % 2 == 0)

# Получение отдельного списка квадратов
squares_list = [n ** 2 for n in numbers if n % 2 == 0]

print("Результат (map/filter):", result_map)
print("Результат (генератор):", result_gen)
print("Список квадратов:", squares_list)
# В отличие от императивной версии, здесь полностью отсутствуют явно изменяемые переменные-накопители.