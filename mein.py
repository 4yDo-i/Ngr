import telebot
from telebot import types

bot = telebot.TeleBot('5657149485:AAEthHetvX404j7xqdOLdq3gZIYErCkr3rE')

poll_items = []  # ['text' - (name) , 0 - (scores)]
id_items = [0]  # [id - id користувачів]


@bot.message_handler(commands=['start'])
def add_id(message):
    bababoi = 1
    i = 0
    while i < len(id_items):
        if (id_items[i] == message.chat.id):
            bababoi = 1
            bot.send_message(message.chat.id, f"I hate U den4ik", parse_mode='html')
            break
        elif (id_items[i] != message.chat.id):
            bababoi = 0
            i += 1
    if (bababoi == 0):
        bot.send_message(message.chat.id, f"Your ID has been edded to the list", parse_mode='html')
        id_items.append(message.chat.id)
        bot.send_message(message.chat.id, f"{id_items}", parse_mode='html')


@bot.message_handler(commands=['vote'])
def vote(message):
    i = 1
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton("Delete", callback_data='delete')
    button_2 = types.InlineKeyboardButton("Vote", callback_data='send')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, f"Pls send {i} message", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['show'])
def show(message):
    i = 0
    while i < len(poll_items):
        bot.send_message(message.chat.id, f'{poll_items[i]} - {poll_items[i + 1]}', parse_mode='html')
        i += 2


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    global poll_items
    if call.message:
        if call.data == 'delete':
            bot.send_message(call.message.chat.id, f"Successfully deleted", parse_mode='html')
            poll_items = []

        elif call.data == 'send':
            bot.send_message(call.message.chat.id, f"Vote has begun", parse_mode='html')
            for j in range(0, len(poll_items), 2):
                for i in range(1, len(id_items)):
                    name = poll_items[j]
                    score = poll_items[j + 1]
                    but_0 = types.InlineKeyboardButton("0", callback_data='0')
                    but_1 = types.InlineKeyboardButton("1", callback_data='1')
                    but_2 = types.InlineKeyboardButton("2", callback_data='2')
                    but_3 = types.InlineKeyboardButton("3", callback_data='3')
                    markup.add(but_0, but_1, but_2, but_3 )
                    bot.send_message(id_items[i], f'{name} - {score}', parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == '0':
            pass
        elif call.data == '1':
            pass
        elif call.data == '2':
            pass
        elif call.data == '3':
            pass


@bot.message_handler()  # Функція, яка приймає назви та значення для голосування(має бути останнью)
def get_user_text(mess):
    global poll_items
    poll_items.append(f"{mess.text}")
    poll_items.append(0)


bot.polling(none_stop=True)