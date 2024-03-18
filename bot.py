import os
import dotenv
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

dotenv.load_dotenv()

BOT_TOKEN = os.environ.get('TELEGRAM_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

# Функція для відображення турнірної таблиці
def show_leaderboard(message):
    bot.reply_to(message, "Тут буде турнірна таблиця.")

# Функція для відображення результатів туру
def show_results(message):
    bot.reply_to(message, "Тут будуть результати туру.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Турнірна таблиця')
    button2 = KeyboardButton('Результати туру')
    markup.row(button1, button2)
    bot.reply_to(message, f"Привіт, {user_name}! Я бот. Оберіть одну з кнопок:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Турнірна таблиця':
        show_leaderboard(message)
    elif message.text == 'Результати туру':
        show_results(message)

bot.infinity_polling()
