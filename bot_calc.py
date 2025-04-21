
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from simpleeval import SimpleEval
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я калькулятор-бот 🧮\n"
        "Просто напиши команду:\n"
        "/calc выражение\n"
        "Например: /calc (2 + 3) * 4"
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

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("calc", calculate))
    print("Бот запущен!")
    await app.run_polling()

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except RuntimeError:
        asyncio.run(main())
