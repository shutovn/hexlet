
# 1. Приветствие
# 2. Предложить сыграть в игру.
# 2.1 Игрок соглашается, дает положительный ответ- Играем.
# 2.2 Игрок отказывается. дает отрицательный ответ - Завершаем программу.
# 2.3 Игрок дает неопределенный ответ - Выводим инф. о не правильном вводе и заканчиваем игру.
# 3. Начало игры.
# 3.1 Представляемся сами.
# 3.2 Просим представиться игрока, ввести его имя.
# 3.3 Выводим Правила игры и примеры значений которые необходимо испоьзовать.
# 4. Генерация рандомного значения карты и ее масти.
# 4.1 Проверка введеного значения, если введено неверное значение, просим ввести корректное.
# 5. Просьба ввести значения карты и масти.
# 5.1 Проверка введеного значения, если введено неверное значение, просим ввести корректное.
# 6. Сравнение сгенерированого результата с ответами пользователя.
# 7. Вывод промежуточного результата.
# 8. Запись раунда в список.
# 9. Спросить пользователя, хочет он еще попробывать сыграть.
# 9.1 Игрок соглашается, дает положительный ответ- Играем еще раунд с пункта 4-9
# 9.2 Игрок отказывается, дает отрицательный ответ или пустой - Вывод результат и Завершаем программу.
# 10. Вывод результата всех раундов по порядку.
#

from random import choice

def rules_game(name):
    print(" ")
    print("Правила игры! ")
    print("Я - Ботаныч, запоминаю в рандомном порядке значение карты и масть.")
    print(f"Вы - {name}, угадываете карту.")
    print("Значение карты надо указывать в формате: Двойка, Тройка, Четверка, Пятерка, Шестерка, Семерка, Восьмерка, Девятка, Десятка, Валет, Дама, Король, Туз ")
    print("Масть карты надо указывать в формате: Бубны, Червы, Пики, Трефы ")
    print("Желаю удачи! ")
    print(" ")

def comparison(card_value, pi_card_value, card_suit, pi_card_suit, count, name):
    print(" ")
    print(f"Ботаныч выбрал: {card_value} {card_suit}. {name} выбрал: {pi_card_value} {pi_card_suit}.")
    if card_value == pi_card_value and card_suit == pi_card_suit:
        status = "Победа"
        print(f"{name} Вы Выиграли!!!")
    elif card_value == pi_card_value:
        status = "Пол победы"
        print(f"{name} Вам удалось угадать только значение карты!")
    elif card_suit == pi_card_suit:
        status = "Пол победы"
        print(f"{name} Вам удалось угадать только масть карты!")
    else:
        status = "Не повезло"
        print(f"{name} Вам не удалось угадать карту!")
    round = (count, name, pi_card_value, pi_card_suit, status, card_value, card_suit)
    return(round)


def our_game():
    game_results = []
    count_rounds = 1
    answer = "yes"
    CARD_NUMBER = ["Двойка", "Тройка", "Четверка", "Пятерка", "Шестерка", "Семерка", "Восьмерка", "Девятка", "Десятка", "Валет", "Дама", "Король", "Туз"]
    CARD_SUIT = ["Бубны", "Червы", "Пики", "Трефы"]
    print(" ")
    print("Я Bot - Ботаныч!")
    print("Представьтесь пожалуйста,")
    name_player = input("С кем имею честь играть: ")
    rules_game(name_player)
    while answer == "yes":
        print(" ")
        print(f"{name_player}, попробуй угадать карту из полной колоды!")
        chosen_card_value = choice(CARD_NUMBER)
        chosen_card_suit = choice(CARD_SUIT)
        while True:
            player_input_card_value = input("Ведите значение карты: ")
            if player_input_card_value in CARD_NUMBER:
                break
            else:
                print("Неверное значение! Смотрите правила!")
        while True:
            player_input_card_suit = input("Ведите масть карты: ")
            if player_input_card_suit in CARD_SUIT:
                break
            else:
                print("Неверное значение! Смотрите правила!")
        game_results.append(comparison(chosen_card_value, player_input_card_value, chosen_card_suit, player_input_card_suit, count_rounds, name_player))
        print(" ")
        answer = input(f"{name_player}, хотите еще сыграть? Введите yes/да: ")
        if answer in ["Yes", "yes", "Да", "да"]:
            answer = "yes"
        count_rounds += 1
    print(" ")
    print("Результаты:")
    for result in game_results:
        print(result)

def no_game():
    print("Очень жаль, что вы не стали играть.")

def welcome_error():
    print(f"Вы ввели {answer} - что не является правильным ответом.")
    print("По этому игра закончилась даже не начавшись :( ")


print("Привет игрок!")
answer = input("Предлагаю поиграть в игру \"Угадай карту!\", введите \"Да\" или \"Нет\":  ")
if answer in ["Yes", "yes", "Да", "да"]:
    our_game()
elif answer in ["No", "no", "Нет", "нет"]:
    no_game()
else:
    welcome_error()
