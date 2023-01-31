import telebot
from telebot import types
from random import choice

bot = telebot.TeleBot('5953495215:AAFSoicvfc6roL_Msj9BkNiPXGfIJpNSkHo')

begin = 221
total = begin
limit = 28

@bot.message_handler(commands=['start'])
def star(message):
    man = message.from_user.first_name
    bot.send_message(message.chat.id, f'Привет, {man}!')
    rules(message)
    button(message)
    print(total)


def rules(message):
    rules = f'Будем играть в конфеты!\nПравила игры:\n\
    Количество наших конфет: {total}.\n\
    Берем по очереди не больше {limit} конфет.\n\
    Кто заберет последние конфеты - тот и победил!'
    bot.send_message(message.chat.id, str(rules))


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton('кинуть жребий')
    markup.add(but)
    bot.send_message(message.chat.id, 'Для начала кинем жребий!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def fate(message):
    lot = choice(['bot', 'man'])
    if lot == 'bot':
        bot.send_message(message.chat.id, 'Я хожу первым!')
        take_bot(message)
    else:
        take_man(message)


def take_bot(message):
    global begin
    global total
    global limit

    bot.send_message(message.chat.id, f'Осталось {total} конфет.')
    if total > 0 and total <= limit:
        bot.send_message(message.chat.id, f'Я забираю все оставшиеся конфеты и побеждаю!')
        total = begin
        return total
    elif total > 0 and total > limit:
        take = total % (limit + 1)
        total -= take
        bot.send_message(message.chat.id, f'Я беру {take} конфет.')
        take_man(message)

        
def count(message):
    global total
    global limit
    if 0 < int(message.text) < 29:
        take = int(message.text)
        total -= take
        take_bot(message)
    else:
        bot.send_message(message.chat.id, f'Можно взять от 1 до {limit} конфет.')


def take_man(message):
    global begin
    global total
    global limit

    man = message.from_user.first_name
    bot.send_message(message.chat.id, f'Осталось {total} конфет.')
    if total > 0 and total <= limit:
        bot.send_message(message.chat.id, f'Поздравляю, {man}, ты победил! Забирай свои {total} конфет.')
        total = begin
        return total
    elif total > 0 and total > limit:
        bot.send_message(message.chat.id, f'Ok, {man}, твой ход!\nСколько хочешь забрать конфет?')
        bot.register_next_step_handler(message, count)


bot.infinity_polling()
