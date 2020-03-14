import random
WORDS = ("питон", "речка", "полка")
word = random.choice(WORDS)
hint = ""
if word == "питон":
    hint = "Это большая змея!"
elif word == "речка":
    hint = "В ней можно купаться!"
else:
    hint = "На ней много интересных книг."
     
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position +1):]
print("Добро пожаловать в игру Анаграмма.")
print("У вас есть право на подсказку, если не получится.")
print("Вот анаграмма - ", jumble)
guess = input("\nПопробуйте отгадать: ")
tries = 1
rewards = 100
while guess != correct and guess != "":
    print("К сожалению вы неправы")
    guess = input("Попробуйте снова: ")
    tries += 1
    #rewards -= 10
    if tries>2 and guess != correct:
        print("Вот подсказка. ", hint)
        #rewards -=20
if guess == correct and tries>2:
    rewards = rewards - 20 - (tries -1)*10
    print("Да, именно так!")
    print("Вы набрали ", rewards, " очков.")
elif guess == correct and tries <2:
    rewards = rewards  - (tries -1)*10
    print("Да, именно так!")
    print("Вы набрали ", rewards, " очков.")
print("\nСпасибо за игру")
input("\nEnter - exit.")
