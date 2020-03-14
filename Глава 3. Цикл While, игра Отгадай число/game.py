import random
print("\t\tДобро пожаловать в игру 'Отгадай число!'")
print("\nПравила игры:")
print("Компьютер загадает число от 1 до 100.")
print("Вы попытаетесь его отгадать за 7 попыток,")
print("если Вам это удастся, то Вы победили!")
the_number = random.randint(1,100)
guess = int(input("\nВведите предполагаемое число: "))
tries = 1
while guess != the_number:   
    if guess > the_number:
        print("Неее, меньше..")
    else: 
        print("Неа, больше:)")
    guess = int(input("Ваше предположение: "))
    tries += 1
    if guess == the_number:    
        print("Мои поздравления, Вы угадали число")
        print("за ", tries, " попыток!") 

    if tries>6:
        print("Вы проиграли, очень жаль.")
        break
                   
input("\n\nНажмите Enter, чтобы выйти.")
