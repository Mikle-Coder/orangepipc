import time

start_time = time.monotonic()

def _run():
    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time
        seconds_elapsed = elapsed_time
        print(f"Прошло {seconds_elapsed} секунд", end="\r")

        # Вычисляем сколько времени прошло с последней секунды
        time_since_last_second = elapsed_time % 1

        # Если время до следующей секунды меньше 0.01 секунды,
        # ждем оставшееся время перед продолжением цикла
        if time_since_last_second < 0.01:
            time.sleep(0.01 - time_since_last_second)