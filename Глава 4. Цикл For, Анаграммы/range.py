print("Давайте посчитаем! Сейчас Вы введете отправную точку,")
print("конечную точку и интервал, который захотите!")
start = int(input("Введите начальную точку: "))
finish = int(input("Введите конечную точку: "))
interval = int(input("Введите интересующий интервал: "))
for i in range(start, finish, interval):
    print(i, end=" ")
input("\nEnter - exit")

