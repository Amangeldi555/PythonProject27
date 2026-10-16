
# Эта библиотека нужна для изменения цвета текста в терминале.
from colorama import Fore, Style, init

# Настраиваем автоматический сброс цвета после вывода текста.
init(autoreset=True)

print(Fore.GREEN + "Домашнее задание №6 выполнено!")
print(Fore.BLUE + "Я изучаю внешние библиотеки Python.")
print(Fore.RED + "Это сообщение красного цвета.")
print(Fore.YELLOW + "Это сообщение жёлтого цвета.")

print(Style.RESET_ALL + "Работа программы завершена.")
