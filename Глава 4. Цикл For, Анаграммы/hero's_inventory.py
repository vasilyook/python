#Арсенал героя, кортеж
inventory = ()
#Рассмотрим как условие
if not inventory :
    print("Вы безоружны.")
input("\nEnter - продолжить.")
#создание кортежа
inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
#вывод кортежа
print("\nСодержимое кортежа: ")
print(inventory)
#вывод последовательно
print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)
input("\n\nEnter - выход.")
