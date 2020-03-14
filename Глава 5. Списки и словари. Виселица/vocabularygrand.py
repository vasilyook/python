vocabulary = {"Елена": "Георгий","Валерий": "Вадим","Ольга": "Валерий"}
choice = None
while choice != "0" :
    print(
    """

    Меню:
    0 - Выход
    1 - Узнать отчество
    2 - Добавить имя 
    3 - Изменить отчество
    4 - Удалить имя
    5 - Узнать деда
    """

    )
    choice = input("Выберите пункт меню: ")
    if choice == "0":
        print("До свидания, друг!")
    elif choice == "1":
        name = input("У какого имени хотите узнать отчество? ")
        name = name.title()
        if name in vocabulary:
            definition = vocabulary[name]
            print(name,": имя отца -", definition)
        else:
            print("\nУвы, нет такого имени в моем словаре,")
            print("но Вы можете его добавить!")
    elif choice == "2":
        print("Вот какие есть имена в моем словаре:")
        #print(vocabulary)
        print(vocabulary.keys())
        name = input("Какое имя хотите добавить в словарь?")
        name = name.title()
        if name not in vocabulary:
            definition = input("\nВпишите отчество: ")
            definition = definition.title()
            vocabulary[name] = definition
            print("Имя ",name, " добавлено в словарь.")
        else:
            print("\nТакое имя уже есть!")
    elif choice == "3":
        name = input("У какого имени хотите изменить отца? ")
        name = name.title()
        if name in vocabulary:
            definition = input("Впишите нового отца: ")
            definition = definition.title()
            vocabulary[name] = definition
            print("У имени - ",name, " изменился отец!")
        else:
            print("\nУвы, нет такого имени в моем словаре,")
            print("но Вы можете его добавить!")
    elif choice == "4":
        name = input("Какое имя хотите удалить? ")
        name = name.title()
        if name in vocabulary:
            del vocabulary[name]
            print("Имени ",name, " больше нет в моем словаре.")
        else:
            print("\nУвы, нет такого имени в моем словаре,")
            print("но Вы можете его добавить!")

    elif choice == "5":
        name = input("У какого имени хотите узнать деда? ")
        name = name.title()
        #definition = vocabulary[name]
        if name  in vocabulary:
            definition = vocabulary[name]
            #if definition in vocabulary:
            last_name = vocabulary[definition]
            print("Деда зовут - ",last_name,".")
        else:
            print("\nУвы, нет такого имени в моем словаре,")
            print("но Вы можете его добавить!")
        
    else:
        print("У меня нет такого пункта!!")
input("\n Enter - выход!")  
        
        
