choice = None
print ('Добрый день!')
print('Добро пожаловать в Ваш планировщик дел!')
name = input ("Как я могу к Вам обращаться? ")
while choice != "0" :
    print('Что хотите сделать,', name, '?')
    print(
    """
    Меню:
    0 - Выход
    1 - Просмотреть список дел
    2 - Добавить дело 
    3 - Удалить выполненное дело
    
    """
    )
    choice = input("Выберите пункт меню: ")
    if choice == "0":
        print("До свидания, друг!")
    elif choice == "1":
        text_file = open("test.txt", "r", encoding = 'utf-8')
        lines = text_file.read()
        # print(len(lines))
        if len(lines) == 1:
            print("File is empty")
        else:
            print(lines)
        text_file.close()
    elif choice == "2":
        text_file = open("test.txt", "a+", encoding = 'utf-8')
        deal = input("Введите, что Вам необходимо сделать? \n")
        deal = '✓' + deal + ';\r'
        text_file.write(deal)
        text_file.close()
    else:
        text_file = open("test.txt", "r", encoding = 'utf-8')
        print('Вот какие дела у Вас еще есть:')
        print(text_file.read())
        print('Так-с..')
        text_file.close()
        text_file = open("test.txt", "r", encoding = 'utf-8')
        x = int(input('Какое задание Вы хотите удалить? '))
        lines = text_file.readlines()
        text_file.close()
        if lines [x] in lines:
            del lines [x]
        text_file = open("test.txt", "w", encoding = 'utf-8')
        x = ''.join(lines)
        text_file.write(x)
        print('Вот, что Вам осталось сделать', name, ':')
        print(x)
        text_file.close()
        

