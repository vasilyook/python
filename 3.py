MAX = 100
def ask_number(question, low, high):
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response
def number():
    x = random.randint(1,100)
    return x
def answer():
    guess = ask_number("? ", 1, MAX)
    while guess != correct:
        if guess > correct:
            print("Less!")
        else:
            print("More")
        guess = ask_number("??", 1, MAX)
    return guess
def correctly():
    correct = x
    if correct == x:
        print("congrat")
    return correct
def main():
    ask_number(question, low, high)
    answer()
    correct = number()
    correctly()
main()

    

    
            
            
    
    

    
