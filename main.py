from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8062785436:AAGXTkPTQgogdjNJgJP92ofv7Zi-Z5O_lGI"
CASINO_URL = "https://stellular-caramel-a5a325.netlify.app/"

# أمر البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎰 دخول إلى الكازينو", url=CASINO_URL)],
        [InlineKeyboardButton("💰 المهام والرصيد", callback_data="tasks")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 أهلاً بك في *Ocean Casino*!\n\nاختر أحد الخيارات بالأسفل:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# قائمة المهام
async def tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    tasks_text = (
        "💼 *قائمة المهام اليومية:*\n\n"
        "1️⃣ تابع قناتنا الرسمية واحصل على 10 نقاط.\n"
        "2️⃣ انشر رابط الدعوة لأصدقائك واربح 5 نقاط لكل تسجيل.\n"
        "3️⃣ يمكن شحن الرصيد بعملات رقمية عبر الموقع.\n\n"
        "🔗 رابط الدعوة الخاص بك:\n"
        f"https://t.me/OceanMiningbot?start={query.from_user.id}"
    )

    keyboard = [
        [InlineKeyboardButton("⬅️ رجوع", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=tasks_text, reply_markup=reply_markup, parse_mode="Markdown"
    )

# رجوع للقائمة
async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🎰 دخول إلى الكازينو", url=CASINO_URL)],
        [InlineKeyboardButton("💰 المهام والرصيد", callback_data="tasks")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="👋 عدت إلى القائمة الرئيسية!",
        reply_markup=reply_markup
    )

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(tasks, pattern="tasks"))
    app.add_handler(CallbackQueryHandler(back_to_menu, pattern="back_to_menu"))
    app.run_polling()

if __name__ == "__main__":
    main()
