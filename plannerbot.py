import telebot
add_deal = ['добавить','добавь', "+"]
done_deal = ["выполнила", "Удалить", "удали", "-"]
view_deal = ["покажи", "показать", "все"]


bot = telebot.TeleBot("токен")

def add(message):
    text_file = open("test.txt", "a+", encoding = 'utf-8')
    deal = message.text.lower()
    deal = '✓' + deal + ';\r'
    #print(deal)
    text_file.write(deal)
    text_file.close()


def del_deal(message):
	text_file = open("test.txt", "r", encoding = 'utf-8')
	deals = text_file.read()
    text_file.close()
    text_file = open("test.txt", "r", encoding = 'utf-8')
    bot.send_message(message.chat.id, "Какое задание Вы хотите удалить?")
    #x = int(input('Какое задание Вы хотите удалить? '))
    lines = text_file.readlines()
    text_file.close()
    if lines [x] in lines:
        del lines [x]
    text_file = open("test.txt", "w", encoding = 'utf-8')
    x = ''.join(lines)
    text_file.write(x)
    print('Вот, что Вам осталось сделать:')
    print(x)
    text_file.close()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, Оля)")
	#print(message)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text in add_deal:
        bot.send_message(message.chat.id, 'Что Вам нужно сделать?')
        # bot.message_handler(content_types=['text'])
        


    elif message.text.lower() in done_deal:
        bot.send_message(message.chat.id, 'Что Вы уже сделали?')
    # elif message.text.lower() in view_deal: 
    else:
    	add(message)

bot.polling()