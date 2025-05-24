import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import openai

TELEGRAM_TOKEN = '7470735937:AAGIjbeWfSf1-aBPFYU0vffFPtxU7smWJ4M'
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши любое слово, и я придумаю вирусную рифму в стиле 'балерина капучина'!")

async def generate_rhyme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = update.message.text.strip()

    prompt = (
        f"Придумай вирусную, абсурдную и смешную рифму к слову '{word}' в стиле интернет-мема 'балерина капучина'. "
        f"Ответ только в одну строчку, как короткий слоган."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )

    rhyme = response.choices[0].message.content.strip()
    await update.message.reply_text(rhyme)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_rhyme))
    app.run_polling()
