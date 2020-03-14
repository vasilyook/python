money = []
choice = None
total = 0
while choice != "0"  :
        
	print(
	"""
	0 - EXIT
	1 - ALL PERSONS
	2 - ADD PERSON
	"""
	)
	choice = input("Your choice? ")
	print()
	if choice == "0":
		print("Good Bye!")
	elif choice == "1":
		print("People:")
		print("Name\tMoney")
		for entry in money:
			summ,name = entry
			print(name, "\t",summ)
	elif choice == "2":
		name = input("What's your name? ")
		summ = int(input("Money? "))
		entry = [summ,name]
		money.append(entry)
		
	#else:
               # print("I dont know")
input("enter - exit")
