"""
Ханойські башти:

Напишіть програму, яка виконує переміщення дисків з стрижня А на стрижень С, використовуючи стрижень В як допоміжний.
Диски мають різний розмір і розміщені на початковому стрижні у порядку зменшення розміру зверху вниз.

Правила:
1. За один крок можна перемістити тільки один диск.
2. Диск можна класти тільки на більший диск або на порожній стрижень.

Вхідними даними програми має бути число n — кількість дисків на початковому стрижні. Вихідними даними — логування
послідовності кроків для переміщення дисків зі стрижня А на стрижень С.
"""
import time

def hanoi(n, source, target, auxiliary, state):
    """
    Функція для переміщення дисків за допомогою рекурсії.

    :param n: кількість дисків
    :param source: стрижень, з якого переміщуються диски
    :param target: стрижень, на який переміщуються диски
    :param auxiliary: допоміжний стрижень
    :param state: поточний стан стрижнів
    """
    # Якщо залишився один диск, просто переміщаємо його
    if n == 1:
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
    else:
        # Переміщаємо n-1 дисків з source на auxiliary, використовуючи target як допоміжний
        hanoi(n - 1, source, auxiliary, target, state)

        # Переміщаємо останній диск з source на target
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")

        # Переміщаємо n-1 дисків з auxiliary на target, використовуючи source як допоміжний
        hanoi(n - 1, auxiliary, target, source, state)


def main():
    n = int(input("Введіть кількість дисків: "))

    # Замір часу
    start_time = time.time()

    # Початковий стан стрижнів
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}

    print(f"Початковий стан: {state}")
    # Викликаємо рекурсивну функцію для переміщення дисків
    hanoi(n, 'A', 'C', 'B', state)
    print(f"Кінцевий стан: {state}")

    # Обчислюємо час виконання
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Час виконання: {execution_time:.6f} секунд")


if __name__ == "__main__":
    main()
