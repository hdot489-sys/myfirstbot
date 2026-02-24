import os
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = '8588678263:AAH4acDvWNV750ssAHnXegIEH5cPHYRuJLI'

# Welcome
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"🎉 Welcome {member.full_name}! Enjoy the group.")

# Time
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"Current time: {now}")

# Bad Word + Reply Combined
BAD_WORDS = ["chutiya", "kutta", "soja", "spamlink.com"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if any(word in text for word in BAD_WORDS):
        await update.message.delete()
        await update.message.reply_text(
            f"⚠️ {update.message.from_user.full_name}, avoid bad words!"
        )
        return

    if "hello" in text:
        await update.message.reply_text("Hello kaise ho 😎")
    else:
        await update.message.reply_text("Mujhe samajh nahi aaya 🤔")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ek joke suno 😄\nTeacher: Homework kyu nahi kiya?\nStudent: Sir network issue tha 😂")

if "tum batao" in text:
    await update.maggase.reply_text("Mai badhiya tum batao ")
    else
    await update.massage.reply_text("Jyada Juban Mat chalao")

# Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Main aapki bot Aliha hoon 🤖")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /rules to see group rules.")

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📜 Follow group rules.")

# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("time", time))
    app.add_handler(CommandHandler("joke",joke))

    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is starting... ✅")
    app.run_polling()






