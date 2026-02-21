from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import datetime

TOKEN = '8588678263:AAEzV5-0XWET32fzXhsxmc8F_RkoKUoeRSM'  # BotFather se token paste karein

# ----------------- Welcome New Users -----------------
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"🎉 Welcome {member.full_name}! Enjoy the group.")

# ----------------- Bad Word / Spam Filter -----------------
BAD_WORDS = ["chutiya", "kutta", "soja","spamlink.com"]  # Apne words daal sakte ho

async def filter_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if any(word in text for word in BAD_WORDS):
        await update.message.delete()
        await update.message.reply_text(f"⚠️ {update.message.from_user.full_name}, please avoid inappropriate words!")
        # Logging
        print(f"[{datetime.datetime.now()}] Deleted message from {update.message.from_user.full_name}: {update.message.text}")

# ----------------- Commands -----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Main aapka advanced bot hoon 🤖")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I can welcome new users and filter bad words.\n"
        "Use /rules to see group rules."
    )

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 Group Rules:\n"
        "1. Be respectful\n"
        "2. No spam or links\n"
        "3. No inappropriate words\n"
        "4. Follow admin instructions"
    )

# ----------------- Main Bot Setup -----------------
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("rules", rules))

    # Event handlers
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), filter_messages))

    # Run the bot
    print("Bot is starting... ✅")
    app.run_polling()