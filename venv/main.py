import random

print("что запускаем:\n"
      "    1 - игра очко")
scriptType = int(input("ваш выбор: "))

if scriptType == 1:

    again = True
    while again:
        deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
        currentBalance = 0
        while True:
            choice = input("Будете брать карту? ")
            if choice == "y" or choice == "д":
                random.shuffle(deck)
                currentCard = deck.pop()
                currentBalance += currentCard
                print('вам выпала карта достоинством %d' %currentCard)
                print('вы набрали %d' %currentBalance)
                if currentBalance == 21:
                    print('Win!!!')
                    break
                elif currentBalance > 21:
                    print('Fail!')
                    break
            else:
                break

        answer_repeat = input("ещё раз?")
        again = answer_repeat == 'y' or answer_repeat == 'д'
