word = input("Введите Ваше слово: ")
#length = len(word)
jumble = ""
while word:
    position = len(word) - 1
    jumble += word[position]
    word = word[:position ]
print("Вот обратное: ", jumble)
input("\n\nEnter - выход")


