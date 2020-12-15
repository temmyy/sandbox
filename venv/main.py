import random

print("что запускаем:\n"
      "    1 - игра очко")
scriptType = int(input("ваш выбор: "))

if scriptType == 1:

    again = True
    while again:
        deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
        currentBalance = 0
        random.shuffle(deck)
        while True:

            if currentBalance == 0:
                k1 = deck.pop()
                k2 = deck.pop()
                print('\n'
                      'ваша раздача: %d + %d' % (k1, k2))
                currentBalance = k1 + k2
                print('вы набрали %d' % currentBalance)

            if input("будете брать карту? ") == "д":
                currentCard = deck.pop()
                currentBalance += currentCard
                print('вам выпало %d' % currentCard)
                print('вы набрали %d' % currentBalance)
                if currentBalance == 21:
                    print('вы победили :)')
                    break
                elif currentBalance > 21:
                    print('вы проиграли :(')
                    break
            else:
                break

        again = input("ещё раз?") == 'д'
