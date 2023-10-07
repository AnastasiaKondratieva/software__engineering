###UTF-8###

import datetime
import time

# Запускаем цикл на 5 секунд
for _ in range(5):
    # Получаем текущее время
    current_time = datetime.datetime.now().strftime('%H:%M:%S')

    # Выводим текущее время
    print(current_time)

    # Засыпаем на 1 секунду
    time.sleep(1)
