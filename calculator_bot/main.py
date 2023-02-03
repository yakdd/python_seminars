import telebot
from telebot import types
import controller, my_logging


bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')   
    bot.send_message(message.chat.id, f'Запускаем калькулятор...\n\
Введите строку с математическим выражением для вычисления результата. (Например: 12 * 4)\n\
Операции возможны как с действительными, так и с комплексными (a + bi) числами!')
    bot.register_next_step_handler(message, calc)


def calc(message):
    my_logging.log(message)
    result = controller.calculator(message)
    bot.send_message(message.chat.id, result)
    bot.send_message(message.chat.id, f'нажми, чтобы перезапустить: /start')


bot.infinity_polling()
