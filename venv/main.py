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
            if input("будете брать карту? ") == "д":
                random.shuffle(deck)
                currentCard = deck.pop()
                currentBalance += currentCard
                print('вам выпало %d' %currentCard)
                print('вы набрали %d' %currentBalance)
                if currentBalance == 21:
                    print('вы победили :)')
                    break
                elif currentBalance > 21:
                    print('вы проиграли :(')
                    break
            else:
                break

        again = input("ещё раз?") == 'д'
