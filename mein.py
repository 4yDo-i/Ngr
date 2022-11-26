import telebot
from telebot import types

bot = telebot.TeleBot('5657149485:AAEthHetvX404j7xqdOLdq3gZIYErCkr3rE')

poll_items = []  # ['text' - (name) , 0 - (scores)]
id_items = [0]  # [id - id користувачів]
admin_id = [946623833, 737654582]
message_id_list = {}
photo_b = bool(False)
name_of_vote = ""


# 737654582, 946623833, 594122698, 741087377, 640266929

@bot.message_handler(commands=['start'])
def add_id(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    vote = types.KeyboardButton('/vote')
    show = types.KeyboardButton('/show')
    restart = types.KeyboardButton('/restart')
    markup.add(vote, show, restart)
    bababoi = 1
    i = 0
    while i < len(id_items):
        if (id_items[i] == message.chat.id):
            bababoi = 1
            bot.send_message(message.chat.id, f"I hate U Den4ik", parse_mode='html')
            break
        elif (id_items[i] != message.chat.id):
            bababoi = 0
            i += 1
    if (bababoi == 0):
        bot.send_message(message.chat.id, f"Your ID has been added to the list", parse_mode='html')
        id_items.append(message.chat.id)
        message_id_list.update({message.chat.id: []})
        bot.send_message(message.chat.id, f"{id_items}", parse_mode='html')

    for id_ in range(len(admin_id)):
        if (message.chat.id == admin_id[id_]):
            bot.send_message(message.chat.id, f"Hello pypsik", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['vote'])
def vote(message):
    if (message.chat.id == 946623833 or message.chat.id == 737654582):
        markup = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton("Delete", callback_data='delete')
        button_2 = types.InlineKeyboardButton("Vote", callback_data='send_name')
        markup.add(button_1, button_2)
        bot.send_message(message.chat.id, f"Please write the name of the vote", parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'I hate U Stas', parse_mode='html')


@bot.message_handler(commands=['restart'])
def restart(message):
    if (message.chat.id == 946623833 or message.chat.id == 737654582):
        bot.send_message(message.chat.id, f"Bot poll_items has been restarted", parse_mode='html')
        global poll_items
        poll_items = []
        global photo_b
        photo_b = 0
        name_of_vote = ""
    else:
        bot.send_message(message.chat.id, f'I hate U Stas', parse_mode='html')


@bot.message_handler(commands=['top'])
def top(message):
    if len(poll_items) >= 3:
        array = poll_items
        j = 0
        while j < 3:
            i = 0
            a = 0
            while i < len(array):
                if array[i][1] >= a:
                    a = int(array[i][1])
                    i = i + 1
            bot.send_message(message.chat.id, f"{j + 1}) {array[a][0]} — {array[a][1]}", parse_mode='html')
            array.pop(a)
            j = j + 1
    else:
        bot.send_message(message.chat.id, f"Sorry, but there are less than 3 items in the rating", parse_mode='html')


@bot.message_handler(commands=['show'])
def show(message):
    if (photo_b == 0):
        for i in range(len(poll_items)):
            bot.send_message(message.chat.id, f'{poll_items[i][0]} — {poll_items[i][1]}', parse_mode='html')
    else:
        for i in range(len(poll_items)):
            bot.send_photo(message.chat.id, poll_items[i][0], parse_mode='html')
            bot.send_message(message.chat.id, f'score: {poll_items[i][1]}', parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global poll_items
    if call.message:
        if call.data == 'delete':
            bot.send_message(call.message.chat.id, f"Successfully deleted", parse_mode='html')
            poll_items = []
        elif call.data == 'send_name':
            bot.send_message(call.message.chat.id, f"Vote has begun", parse_mode='html')

            for poll_item in range(0, len(poll_items)):
                for id_ in range(1, len(id_items)):
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    name = poll_items[poll_item][0]
                    but_0 = types.InlineKeyboardButton("0", callback_data=f'0_{poll_item}')
                    but_1 = types.InlineKeyboardButton("1", callback_data=f'1_{poll_item}')
                    but_2 = types.InlineKeyboardButton("2", callback_data=f'2_{poll_item}')
                    but_3 = types.InlineKeyboardButton("3", callback_data=f'3_{poll_item}')
                    markup.add(but_0, but_1, but_2, but_3)
                    # mess_id = bot.send_message(id_items[id_], f"Do U like this logo?", parse_mode='html')
                    # message_id_list[id_items[id_]].append(mess_id)
                    if (photo_b == 0):
                        mess_id = bot.send_message(id_items[id_], f'Do you like this {name_of_vote} - {name}?',
                                                   parse_mode='html',
                                                   reply_markup=markup).message_id
                    else:
                        mess_id = bot.send_photo(id_items[id_], name, f'Do you like this {name_of_vote}?',
                                                 reply_markup=markup).message_id

                    message_id_list[id_items[id_]].append(mess_id)

        id_ = call.message.chat.id
        for i in range(len(poll_items)):
            if call.data == f'0_{i}':
                bot.delete_message(id_, message_id_list[id_][i])
            # bot.delete_message(id_, message_id_list[id_][i])
            elif call.data == f'1_{i}':
                bot.delete_message(id_, message_id_list[id_][i])
                # bot.delete_message(id_, message_id_list[id_][i])
                poll_items[i][1] = poll_items[i][1] + 1

            elif call.data == f'2_{i}':
                bot.delete_message(id_, message_id_list[id_][i])
                # bot.delete_message(id_, message_id_list[id_][i])
                poll_items[i][1] = poll_items[i][1] + 2

            elif call.data == f'3_{i}':
                bot.delete_message(id_, message_id_list[id_][i])
                # bot.delete_message(id_, message_id_list[id_][i])
                poll_items[i][1] = poll_items[i][1] + 3


@bot.message_handler(content_types=['photo'])
# Функція, яка приймає фото та значення для голосування(має бути останнью)
def get_user_photo(message):
    if (message.chat.id == 946623833 or message.chat.id == 737654582):
        global poll_items
        global photo_b
        photo_b = 1
        poll_items.append([message.photo[-1].file_id, 0])
        bot.send_message(message.chat.id, f'Send next picture or send vote or delete vote', parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'I hate U Stas', parse_mode='html')
    # bot.send_photo(id_items[1], poll_items[0])
    # message.photo[-1].file_id


@bot.message_handler(content_types=['text'])
# Функція, яка приймає назви та значення для голосування(має бути останнью)
def get_user_text(message):
    global name_of_vote
    if (message.chat.id == 946623833 or message.chat.id == 737654582):
        if (name_of_vote != ""):
            global poll_items
            poll_items.append([f"{message.text}", 0])
            bot.send_message(message.chat.id, f'Send next message or send vote or delete vote', parse_mode='html')
        else:
            name_of_vote = message.text
    else:
        bot.send_message(message.chat.id, f'I hate U Stas', parse_mode='html')


bot.polling(none_stop=True)
