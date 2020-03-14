#подключение рандомного модуля
import random
surprise = random.randint(1,5)
if surprise == 1 :
    print("\nСаша, я тебя люблю!")
elif surprise == 2 :
    print("\nСаша, ты самый лучший на свете!")
elif surprise == 3 :
    print("\nЯ хочу быть с тобой всегда!")
elif surprise == 4 :
    print("\nЧто ты хочешь в подарок на др?")
else :
    print("\nЧто ты хочешь на нашу годовщину??")
input("\n\nНажмите Enter, чтобы выйти.")
    
