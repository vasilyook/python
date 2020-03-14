total = ["*", "*", "*", "*","*","*", "*", "*", "*","*","*", "*", "*", "*","*","*", "*", "*", "*","*","*", "*", "*", "*","*","*", "*", "*", "*","*"]
print("В вашем распоряжении 30 звезд, чтобы создать")
print("своего суперЗЛОДЕЯ! Вам нужно распределить")
print("эти 30 звезд по четырем характеристикам:")
print("\nСила\nЗдоровье\nМудрость\nЛовкость")
health = []
strength = []
dexterity = []
wisdom = []
slice_ = []
choice = None

while choice != "0" :
    print(
    """

    Меню:
    0 - Выход
    1 - Добавление
    2 - Просмотр
    3 - Изменение
    4 - Удаление
    """

    )
    
    choice = input("Выберите пункт меню: ")
    if choice == "0":
        print("До свидания, друг!")
    elif choice == "1":
        character = input("На какую характеристику хотите добавить звезд? ")
        finish = int(input("Сколько будем добавлять звезд скиллу? "))
        if character == "ловкость":
            slice_ = total[:finish]
            dexterity += slice_
            del total[:finish]
            print("В вашем распоряжении осталось - ", len(total), "звезд/-ы.")
        elif character == "сила":
            slice_ = total[:finish]
            strength += slice_
            del total[:finish]
            print("В вашем распоряжении осталось - ", len(total), "звезд/-ы.")     
        elif character == "здоровье":
            slice_ = total[:finish]
            health += slice_
            del total[:finish]
            print("В вашем распоряжении осталось - ", len(total), "звезд/-ы.")
        elif character == "мудрость": 
            slice_ = total[:finish]
            wisdom += slice_
            del total[:finish]
            print("В вашем распоряжении осталось - ", len(total), "звезд/-ы.")
        else:
             print("У меня нет такой характеристики - ", character)
    elif choice == "2":
        print("Здоровье - ", len(health))
        print("Мудрость - ", len(wisdom))
        print("Сила - ", len(strength))
        print("Ловкость - ", len(dexterity))
    elif choice == "3":
        character = input("С какого скилла будем убирать звезды?")
        finish = int(input("Сколько будем убирать звезд? "))
        if character == "ловкость":
            slice_ = dexterity[:finish]
            total += slice_
            del dexterity[:finish]
            print("В вашем распоряжении осталось - ", len(total), "звезд/-ы.")
        elif character == "сила":
            slice_ = strength[:finish]
            total += slice_
            del strength[:finish]
            print("В вашем распоряжении осталось - ", len(total), "звезд/-ы.")     
        elif character == "здоровье":
            slice_ = health[:finish]
            total += slice_
            del health[:finish]
            print("В вашем распоряжении осталось - ", len(total), "звезд/-ы.")
        else: 
            slice_ = wisdom[:finish]
            total += slice_
            del wisdom[:finish]
            print("В вашем распоряжении осталось - ", len(total), "звезд/-ы.")
    elif choice == "4":
        total = total + wisdom + health + strength + dexterity
        del wisdom[:]
        del strength[:]
        del health[:]
        del dexterity[:]
        print("Все звезды снова в наличии!")
        print("У Вас ", len(total), " звезд.")
    else:
        print("У меня нет такого пункта!!")
input("\n Enter - выход!")        
        
        

        
