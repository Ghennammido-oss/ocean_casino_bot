from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# ضع توكن البوت هنا
TOKEN = "8062785436:AAGXTkPTQgogdjNJgJP92ofv7Zi-Z5O_lGI"
CASINO_URL = "https://stellular-caramel-a5a325.netlify.app/"

# قاعدة بيانات مؤقتة داخلية (يمكن لاحقًا ربطها بملف JSON أو قاعدة بيانات حقيقية)
players = {}

# بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "لا يوجد اسم"
    
    if user_id not in players:
        players[user_id] = {
            "name": username,
            "balance": 1000,  # الرصيد الافتراضي
            "tasks": []
        }

    keyboard = [
        [InlineKeyboardButton("🎰 فتح الكازينو", url=CASINO_URL)],
        [InlineKeyboardButton("💰 عرض الرصيد والمهام", callback_data="show_balance")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"👋 أهلاً {players[user_id]['name']}!\n"
        "اختر ما تريد من الخيارات أدناه:",
        reply_markup=reply_markup
    )

# معالجة الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "show_balance":
        player = players.get(user_id)
        if player:
            tasks_text = "\n".join([f"- {t}" for t in player["tasks"]]) or "لا توجد مهام بعد."
            await query.message.reply_text(
                f"💰 رصيدك: {player['balance']} نقاط\n"
                f"📝 المهام:\n{tasks_text}"
            )
        else:
            await query.message.reply_text("❌ لم يتم العثور على بياناتك.")

# إضافة مهمة (مثال: يمكن أن تضيف زر آخر في المستقبل لإضافة مهام)
async def add_task(user_id: int, task_name: str):
    if user_id in players:
        players[user_id]["tasks"].append(task_name)
        return True
    return False

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()



