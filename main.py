# Telegram Bot для техподдержки

from telegram import Update, Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 6. Конфигурация токена бота (замените на свой токен)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# 7. Обработчик команды /start
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    keyboard = [["Помощь", "Связаться с оператором"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text(
        f"Привет, {user.first_name}! Чем могу помочь?", reply_markup=reply_markup
    )

# 8. Обработчик текстовых сообщений
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "помощь" in text:
        update.message.reply_text("Вы можете задать любой вопрос, и я попробую помочь!")
    elif "оператор" in text:
        update.message.reply_text("Соединяю с оператором...")
    else:
        update.message.reply_text("Извините, я не понял ваш запрос.")

# 9. Основная функция запуска бота
def main():
    # 9.1 Инициализация бота и обновлений
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # 9.2 Добавление обработчиков команд и сообщений
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # 9.3 Запуск бота
    updater.start_polling()
    updater.idle()

# 10. Запуск скрипта, если файл исполняется напрямую
if __name__ == "__main__":
    main()
