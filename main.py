import telebot

bot = telebot.TeleBot('1184393666:AAF688UCMz5JUOyjE98gdI9jqurxXSgkdq8')

node = {'Категория' :['A, B, C - 1$']}


def createKeyboard(dict):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for key in dict.keys():
        keyboard.add(telebot.types.InlineKeyboardButton(text=key, callback_data=key))
    return keyboard


def printRes(l):
    text1 = 'Совет для вас:'
    text2 = ''
    for el in l:
        text2 = text2 + '\n' + el
    return text1 + text2


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(telebot.types.InlineKeyboardButton(text='Узнать стоимость обучения', callback_data='courses_cost'))
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def main_query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)

    if call.data == 'courses_cost':
        typeKey = createKeyboard(node)
        bot.send_message(call.message.chat.id, '\nстоимость:', reply_markup=typeKey)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


    elif call.data in node.keys():
        result = printRes(node.get(call.data))
        bot.send_message(call.message.chat.id, result)


bot.polling()