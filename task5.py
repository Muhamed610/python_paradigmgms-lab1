import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        raw_input = entry.get()
        nums = [int(x) for x in raw_input.split()]
        result = sum(n ** 2 for n in nums if n % 2 == 0)
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа через пробел!")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Нажмите кнопку")

root = tk.Tk()
root.title("Парадигмы программирования")

entry_label = tk.Label(root, text="Введите числа через пробел:")
entry_label.pack(padx=20, pady=2)

entry = tk.Entry(root, width=30)
entry.insert(0, "4 -7 2 -9 12 -5 8 3")
entry.pack(padx=20, pady=5)

button_calc = tk.Button(root, text="Вычислить", command=calculate)
button_calc.pack(padx=20, pady=5)

button_clear = tk.Button(root, text="Очистить", command=clear)
button_clear.pack(padx=20, pady=5)

result_label = tk.Label(root, text="Нажмите кнопку")
result_label.pack(padx=20, pady=10)

root.mainloop()