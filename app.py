from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import logging

# Токен твоего бота, полученный у @BotFather
TOKEN = " "

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для старта
def start(update, context):
    update.message.reply_text(
        "Привет! Я твой бот. Для оформления заказа нажми на кнопку ниже.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Заказать товар", callback_data='order')],
            [InlineKeyboardButton("Инструкция по оплате", callback_data='payment')]
        ])
    )

# Функция для обработки кнопок
def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'order':
        query.edit_message_text(text="Пожалуйста, выбери способ доставки, количество, размер и способ оплаты.")
        # Можно добавить формы для ввода данных
    elif query.data == 'payment':
        query.edit_message_text(text="Инструкция по оплате: Оплата через карту или по телефону.")

# Основной метод для запуска
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Обработчики
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

from flask import Flask, request
import os

app = Flask(__name__)

# Здесь будет логика для webhook, если хочешь использовать его
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    # Обработать JSON-данные и отправить их в Telegram API

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
