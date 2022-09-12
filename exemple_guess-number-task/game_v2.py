"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = np.random.randint(1,101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lst_n = [range(1,101)]

    while True:
        count += 1
        predict_number = int(np.mean(lst_n))  # предполагаемое число
        
        half = round(len(lst_n)/2)
        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number < number:
            lst_n = lst_n[:half]
        else:
            lst_n = lst_n[half:]
            
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100))  # загадали список чисел
    #print(random_array)
    for number in random_array:
        count_ls.append(random_predict(number))
        print(count_ls)

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
