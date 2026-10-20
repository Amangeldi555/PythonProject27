#
# # Эта библиотека нужна для изменения цвета текста в терминале.
# from colorama import Fore, Style, init
#
# # Настраиваем автоматический сброс цвета после вывода текста.
# init(autoreset=True)
#
# print(Fore.GREEN + "Домашнее задание задание №6")
# print(Fore.BLUE + "Я изучаю внешние библиотеки Python.")
# print(Fore.RED + "Это сообщение красного цвета.")
# print(Fore.YELLOW + "Это сообщение жёлтого цвета.")

# from colorama import Fore, Back, init
#
# init(autoreset=True)
#
# print(Back.GREEN + Fore.RED "Geeks pro")
# print(Back.BLUE +  "Надо скооро пройти в Geek pro")
# print(Back.YELLOW + "Чтобы в дальнейшем больше погружаться в it")
# print(Back.RED + "хочу больше практиковаться")
# print(Back.BLUE + "Аман Мундузбаев")

# print(Style.RESET_ALL + "Программа завершена")
#
# from colorama import Fore, Back, init
#
# init(autoreset=True)
#
# print(Back.RED + Fore.WHITE + " Белый текст на красном фоне ")
# print(Back.GREEN + Fore.BLACK + " Чёрный текст на зелёном фоне ")
# print(Back.BLUE + Fore.WHITE + " Белый текст на синем фоне ")


from colorama import Fore, Back, init

init(autoreset=True)

print(Back.GREEN + Fore.RED + "Geeks Pro")
print(Back.BLUE + "Надо скоро поступить в Geeks Pro")
print(Back.YELLOW + "Чтобы в дальнейшем больше погружаться в IT")
print(Back.RED + "Хочу больше практиковаться")
print(Back.BLUE + "Аман Мундузбаев")
