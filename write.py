print('My plan')
print('What I do?')
deal = input('What?')
text_file = open("write_it.txt", "w", encoding = 'utf-8')
text_file.write(deal)
text_file.close()