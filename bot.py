import telebot
from telebot import types

bot = telebot.TeleBot('6930083238:AAFKrbT7_4Eqr9z5Z8zdjepG7JLkJhsLRBw')

#Тут бот говорит о себе. И тут есть кое что интересное, он обращается к тебе по твоему нику в телеграмме!
@bot.message_handler(commands=["start"])
def welcome(message):
    sti=open('/bot/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html')

#эта кнопка переходит по ссылке
@bot.message_handler(commands = ['news'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Тыкни', url='https://tengrinews.kz/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Новости", reply_markup = markup)

#этот блок отвечает за то чтобы бот отправлял тебе, что ты ему напишешь
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)