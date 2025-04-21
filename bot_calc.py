
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from simpleeval import SimpleEval

# Получаем токен из переменной среды
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я калькулятор-бот 🧮\n"
        "Напиши /calc выражение\n"
        "Пример: /calc (2 + 3) * 4"
    )

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    expression = " ".join(context.args)
    try:
        s = SimpleEval()
        s.functions = {}
        result = s.eval(expression)
        await update.message.reply_text(f"Результат: {result}")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("calc", calculate))
    print("Бот запущен!")
    app.run_polling()
