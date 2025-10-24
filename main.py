from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8062785436:AAGXTkPTQgogdjNJgJP92ofv7Zi-Z5O_lGI"
CASINO_URL = "https://stellular-caramel-a5a325.netlify.app/"

# أمر البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎰 فتح الكازينو", url=CASINO_URL)],
        [InlineKeyboardButton("📋 مهامي", url=CASINO_URL + "#tasks")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 مرحبًا بك في كازينو تيليغرام!\nاضغط على الزر أدناه لفتح الكازينو أو المهام:",
        reply_markup=reply_markup
    )

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()




