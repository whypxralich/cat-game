print("К тебе подошел кот, что ты с ним сделаешь?")
print("a) Погладить")
print("b) Покормить")
print("c) Пройти мимо")

choice = input()

if choice == 'a':
    print("Вы погладили кота. Кот доволен.")
    print("Кот хочет, чтобы вы погладили его еще")
    print("a) Погладить еще")
    print("b) Уйти")

    choice = input()

    if choice == 'a':
        print("Кот доволен, но уже хочет уйти.")
        print("a) Погладить еще")
        print("b) Уйти")

        choice = input()

        if choice == 'a':
            print("Кот убежал...")
            exit()
        
    elif choice == 'b':
        print("Вы ушли. Кот остался доволен.")
        exit()

elif choice == 'b':
    print("Вы хотели покормить кота, но, оказывается, у вас нет еды.")
    print("a) Пойти в магазин за едой для кота")
    print("b) Уйти")

    choice = input()

    if choice == 'a':
        print("Вы покормили кота. Кот остался очень доволен.")
        print("a) Погладить")
        print("b) Уйти")

        choice = input()

        if choice == 'a':
            print("Вы погладили кота. Кот очень доволен. Теперь у вас есть кот.")
        
        elif choice == 'b':
            print("Вы погладили кота. Кот доволен. Вы ушли по своим делам.")
            exit()

    elif choice == 'b':
        print("Вы ушли. Кот понял что зря подошел.")
        exit()

elif choice == 'c':
    print("Вы прошли мимо кота. Кот недоволен. Конец игры.")
    exit()