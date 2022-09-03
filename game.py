"""  Игры отгодай число.  """
import numpy as np

random = np.random.randint(1,101)

count = 0

while True:
    count +=1
    p_random = int(input("Угадай число от 1 до 100: 2"))
    if p_random > random:
        print("Число должно быть меньше")
    elif p_random < random:
        print("Число должно быть больше")
    else:
        print(f"Вы угадали число. Это число {random}, за {count} попыток.")