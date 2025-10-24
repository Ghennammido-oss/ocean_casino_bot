import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# تفعيل اللوق لتصحيح الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8062785436:AAGXTkPTQgogdjNJgJP92ofv7Zi-Z5O_lGI"

# قاعدة بيانات بسيطة للاعبين (يمكن تطويرها لاحقًا)
players = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in players:
        players[user_id] = {"name": update.effective_user.first_name, "balance": 0}
    keyboard = [
        [InlineKeyboardButton("🎯 المهام", callback_data='tasks')],
        [InlineKeyboardButton("🎰 الكازينو", callback_data='casino')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"👋 أهلاً {players[user_id]['name']}!\nاختر ما تريد من الخيارات أدناه:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    if query.data == 'tasks':
        await query.edit_message_text(text=f"📝 هنا يمكن إدارة المهام، رصيدك الحالي: {players[user_id]['balance']} نقطة")
    elif query.data == 'casino':
        await query.edit_message_text(text=f"🎰 مرحبًا بك في الكازينو، رصيدك: {players[user_id]['balance']} نقطة")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(app.callback_query_handler(button))

    print("البوت يعمل الآن...")
    app.run_polling()

if __name__ == '__main__':
    main()






