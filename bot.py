import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Привіт! Я ваш новий бот. Як я можу вам допомогти?"
    )

if name == '__main__':
    # Вставте сюди токен, який ви отримали від @BotFather
    TOKEN = ‘8838614527:AAGEsK-Sik8zn86WGI2ZFDR2SvvEPwi8O_E’
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("Бот запущений...")
    application.run_polling()
