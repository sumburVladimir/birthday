import telebot
from datetime import date,datetime

sec = datetime.now().second
print(sec)

bot = telebot.TeleBot('5065562860:AAEH8OlLINO-pzk0EPQqZrVqd800fL6KRZk')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    while True:
        if sec == 12:
            bot.send_message(message.from_user.id, 'Сработало событие по таймеру')

bot.polling(none_stop=True, interval=0)