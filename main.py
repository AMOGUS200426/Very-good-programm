import telebot
import config
import ya
import random
API_TOKEN = config.API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, чем я могу помочь?")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, ya.gpt(message.text))

@bot.message_handler(content_types=['photo'])
def input_photo(message):
    file_path = bot.get_file(message.photo[-1].file_id).file_path
    file = bot.download_file(file_path)
    with open(f"images/{random.randint(1000000,10000000000000)}.png", "wb") as code:
        code.write(file)
    bot.reply_to(message, 'Картинка сохранена.')

@bot.message_handler(commands=['advice'])
def send_adivece(message):
    advices = ['jgbdfjkg','skjgfnfkdjg','sopfksdlf;g']
    bot.send_message(message.chat.id, random.choice(advices))

bot.infinity_polling()
