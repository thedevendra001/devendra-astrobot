import imghdr
import telegram
from telegram.ext import Updater, CommandHandler
import datetime

# Devendra's Bot Token
TOKEN = "7978386504:AAFf7b8A_-o6G_jTSS2SqawTBBmjwow5rSA"

# Daily Prediction Message
def daily(update, context):
    message = (
        "🌟 *Aaj Ka Bhavishyafal* (Devendra AstroBot)\n\n"
        "🧠 *Career:* Aaj ka din naye ideas aur decisions ke liye shubh hai.\n"
        "💰 *Finance:* Chhoti savings se bada fayda ho sakta hai.\n"
        "❤️ *Love/Relations:* Purane rishte phir se majboot ban sakte hain.\n"
        "🩺 *Health:* Thoda sa stress ho sakta hai, lekin dhyan aur jal se shanti milegi.\n"
        "🕉️ *Spiritual:* Shiv mantra jaap ya tulsi pooja se man shant rahega.\n"
    )
    update.message.reply_text(message, parse_mode=telegram.ParseMode.MARKDOWN)

# Start command
def start(update, context):
    update.message.reply_text("🙏 Welcome to Devendra AstroBot! Type /daily to get today's personalized prediction.")

# Set up the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("daily", daily))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
git add render.yaml
git commit -m "Add render.yaml with python 3.10.13 config"
git push origin main
