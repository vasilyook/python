import random

count = 0
eagle = 0
tails = 0
while True:
    number = random.randint(1,2)
    count += 1
    if count>100:
        break
    if count<=100 and number == 1:
        eagle +=1
        
    if count<=100 and number == 2:
         tails +=1
         print("\nОрел ", eagle, ", Решка ", tails)
input("\n\nНажмите Enter, чтобы выйти.")
