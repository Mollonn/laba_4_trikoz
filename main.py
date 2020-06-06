import telebot

bot = telebot.TeleBot('1184393666:AAF688UCMz5JUOyjE98gdI9jqurxXSgkdq8')

breakage = {'Cтучит подвеска': ['Поменть резину', 'Проверить развал/схождение', 'Заменить подшипник'],
            'Гул двигателя во время езды': ['Вам необходимо обратиться в автосервис'],
            'Горит лампочка масла': ['Вам необходимо купить масло и заменить его'],
            'Горит лампочка аккумулятора': ['Вам необходимо купить аккумулятор и заменить его']}
node = {'Ходовая': ['Поменть резину', 'Проверить развал/схождение', 'Заменить подшипник'],
        'Двигатель': ['Вам необходимо обратиться в автосервис'],
        'Коробка': ['Вам необходимо обратиться в автосервис'],
        'Расходники': ['Замена масла двигателя', 'Замена масла коробки', 'Замена аккумулятора']}


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

    keyboard.add(telebot.types.InlineKeyboardButton(text='Найти деталь по узлу', callback_data='searchByNode'))
    keyboard.add(telebot.types.InlineKeyboardButton(text='Найти деталь по типу поломки', callback_data='searchByType'))
    bot.send_message(message.chat.id, 'Привет, выберите как искать деталь', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def main_query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)

    if call.data == 'searchByType':
        typeKey = createKeyboard(breakage)
        bot.send_message(call.message.chat.id, '\nВыберите тип поломки:', reply_markup=typeKey)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data in breakage.keys():
        result = printRes(breakage.get(call.data))
        bot.send_message(call.message.chat.id, result)

    elif call.data == 'searchByNode':
        typeKey = createKeyboard(node)
        bot.send_message(call.message.chat.id, '\nВыберите тип узла:', reply_markup=typeKey)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data in node.keys():
        result = printRes(node.get(call.data))
        bot.send_message(call.message.chat.id, result)


bot.polling()