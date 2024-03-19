import os
import dotenv
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

dotenv.load_dotenv()

BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


def show_leaderboard(message):
    bot.reply_to(message, "Тут буде турнірна таблиця.")


def show_results(message):
    bot.reply_to(message, "Тут будуть результати туру.")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Турнірна таблиця")
    button2 = KeyboardButton("Результати туру")
    button3 = KeyboardButton("Календар")
    button4 = KeyboardButton("Кубок")
    button5 = KeyboardButton("Адмінпанель")

    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Hello", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def send_message(message):
    if message.chat.type == "private":
        if message.text == "Турнірна таблиця":
            bot.send_message(message.chat.id, "Це турнірна таблиця")
        elif message.text == "Результати туру":
            bot.send_message(message.chat.id, "Це Результати туру")
        elif message.text == "Календар":
            bot.send_message(message.chat.id, "Це Календар")
        elif message.text == "Кубок":
            bot.send_message(message.chat.id, "Це Кубок")
        elif message.text == "Адмінпанель":
            bot.send_message(message.chat.id, "Це Адмінпанель")


bot.infinity_polling()
