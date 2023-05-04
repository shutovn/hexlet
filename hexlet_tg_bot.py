#import telebot
from random import choice

#print("Hello")

# 1. Приветствие
# 2. Мануал - свод правил
# 3. Генерация рандомной карты
# 4. Вопрос игроку: черная или красная масть?
# 5. Ответ игрока.
# 6. Сравнение ответа.
# 6.1 Если правильно, то поздравляем игрока.
# 6.2 Если не правильно, то расскрываем карты.
#
#

print("Привет игрок!") # 1

print("У меня есть для тебя карта. Попробуй угадать, какого цвета ее масть?") # 2

CARD_NUMBER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUIT = ["Бубны", "Червы", "Пики", "Трефы"]

chosen_card_number = choice(CARD_NUMBER)
chosen_card_suit = choice(CARD_SUIT)

#print(chosen_card_number, chosen_card_suit)
#print()

player_answer = input("Выберите между черным и красным цыетом: ")

if chosen_card_suit in ["Бубны", "Черви"] and player_answer == "красный":
    print("Поздравляю! Вы угадали цвет карты: "+ chosen_card_number + ' ' + chosen_card_suit)
elif chosen_card_suit in ["Пики", "Трефы"] and player_answer == "черный":
    print("Поздравляю! Вы угадали цвет карты: "+ chosen_card_number + ' ' + chosen_card_suit)
else:
    print("Неверно! Карта была: " + chosen_card_number + ' ' + chosen_card_suit)

#print (player_answer)
