import telebot
from telebot import types


bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')   
    bot.send_message(message.chat.id, f'Запускаем калькулятор...')
    bot.send_message(message.chat.id, f'/button')
    """
    bot.send_message(куда, сообщение) => отправка сообщения
    bot.register_next_step_handler(ответ пользователя, функция) => вызов функции на ответ от пользователя
    @bot.message_handler(commands=['start', 'help']) => список триггерных команд на вызов функции под декоратором
    """

def summa(message):
    nums = list(map(int, message.text.split()))
    summ = sum(nums)
    bot.send_message(message.chat.id, f'{str(nums[0])} + {str(nums[1])} = {str(summ)}')
    button(message)
    
def different(message):
    nums = list(map(int, message.text.split()))
    diff = nums[0] - nums[1]
    bot.send_message(message.chat.id, f'{str(nums[0])} - {str(nums[1])} = {str(diff)}')
    button(message)

def multiple(message):
    nums = list(map(int, message.text.split()))
    diff = nums[0] * nums[1]
    bot.send_message(message.chat.id, f'{str(nums[0])} * {str(nums[1])} = {str(diff)}')
    button(message)

def devision(message):
    nums = list(map(int, message.text.split()))
    if nums[1] == 0:
        bot.send_message(message.chat.id, f'А-я-яй, {message.from_user.first_name}! На ноль делить нельзя!')
    else:
        diff = nums[0] / nums[1]
        bot.send_message(message.chat.id, f'{str(nums[0])} / {str(nums[1])} = {str(diff)}')
    button(message)


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but_summ = types.KeyboardButton('СЛОЖИТЬ')
    but_diff = types.KeyboardButton('ВЫЧЕСТЬ')
    but_mult = types.KeyboardButton('УМНОЖИТЬ')
    but_divr = types.KeyboardButton('РАЗДЕЛИТЬ')
    markup.add(but_summ)
    markup.add(but_diff)
    markup.add(but_mult)
    markup.add(but_divr)
    bot.send_message(message.chat.id, 'выбери операцию', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    answer = f'/start - старт бота;\n/help - вывод всех доступных команд;\n/button - вызов клавиатуры.'
    bot.send_message(message.chat.id, str(answer))


@bot.message_handler(content_types=['text'])
def controller(message):
    bot.send_message(message.chat.id, 'Введи два числа через пробел...')
    if message.text == 'СЛОЖИТЬ':
        bot.register_next_step_handler(message, summa)

    elif message.text == 'ВЫЧЕСТЬ':
        bot.register_next_step_handler(message, different)
    
    elif message.text == 'УМНОЖИТЬ':
        bot.register_next_step_handler(message, multiple)
    
    elif message.text == 'РАЗДЕЛИТЬ':
        bot.register_next_step_handler(message, devision)
    


bot.infinity_polling()
