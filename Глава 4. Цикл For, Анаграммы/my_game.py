import random
WORDS = ("магнит", "ключ", "рукав")
word = random.choice(WORDS)
correct = word
print("Добро пожаловать в мою новую игру")
print("под названием 'Угадай слово по буквам'.")
print("У Вас есть 5 попыток.")
print("\nКомпьютер уже загадал слово!")
print("\nВ моем слове - ", len(word), "букв/-ы.")
guess = input("Введите букву, которую хотите узнать наличие: ")
tries = 1
while tries <5:
    if guess in word:
         print("да")
    else:
         print("нет")
    guess = input("Буква? ")
    tries += 1
text = input("\nВведите предполагаемое слово: ")
if text == correct:
    print("Вы угадали")
else:
    print("Не угадали")
    

