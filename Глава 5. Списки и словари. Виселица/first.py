import random
FRUITS =["яблоко", "банан", "киви", "Груша", "апельсин"]
while len(FRUITS)!=0:
    yourfruit = random.choice(FRUITS)
    print(yourfruit)
    FRUITS.remove(yourfruit)
    
    
