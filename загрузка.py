import time


def progress_bar(percent):
    # определение длины полосы загрузки
    bar_length = 20
    block = int(round(bar_length * percent / 100))
    # определение отображения загрузки в виде строки
    text = "\rLoading: [{0}] {1}%".format("#" * block + "-" * (bar_length - block), percent)
    # печать на экран отображения процесса загрузки
    print(text, end="", flush=True)
# демонстрация отображения прогресс-бара в цикле
for i in range(101):
    progress_bar(i)
    time.sleep(0.1)  # для задержки в 0.1 секунды