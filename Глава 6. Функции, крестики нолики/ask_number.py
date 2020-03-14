def ask_number(quetion,low,high):
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response
ask_number()
