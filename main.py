from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from openai import OpenAI
BOT_TOKEN = 8945547270:AAG5vN6rvQRp9tipzTyzJXMsEAlguCYp-d4"
OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇺🇿 Salom!\n🇬🇧 Hello!\n🇫🇷 Bonjour!"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": update.message.text}]
    )
    await update.message.reply_text(response.choices[0].message.content)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
