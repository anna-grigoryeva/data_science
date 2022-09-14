"""Игра угадай число
Компьютер сам загадывает и сам угадывает число меньше чем за 20 попыток
"""

import numpy as np

number = np.random.randint(1, 101)  # предполагаемое число

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число меньше чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min = 1
    max = 100
    count = 0

    while True:
        count += 1
        mid = round((min+max)/2)
        
        if mid > number:
            max = mid
        
        elif mid < number:
            min = mid
        
        else:
            break  # выход из цикла если угадали
    return count

print(f"Компьютер угадал число за {random_predict(number)} попыток")
    


