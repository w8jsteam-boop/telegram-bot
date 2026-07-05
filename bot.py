import telebot
import os

# BotFather থেকে পাওয়া Token এখানে বসাও
TOKEN = "আপনার_TOKEN_এখানে_বসাও"

# বট তৈরি করো
bot = telebot.TeleBot(TOKEN)

# /start কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "স্বাগতম! 👋 আমি একটি সহজ চ্যাট বট। /help লিখো সাহায্যের জন্য।")

# /help কমান্ড
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    আমি যা করতে পারি:
    /start - শুরু করো
    /help - এই সাহায্য দেখো
    /hello - আমাকে হ্যালো বলো
    /about - আমার সম্পর্কে জানো
    """
    bot.reply_to(message, help_text)

# /hello কমান্ড
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "হ্যালো! 😊 তুমি কেমন আছো?")

# /about কমান্ড
@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "আমি একটি সহজ টেলিগ্রাম চ্যাট বট যা Python দিয়ে তৈরি। 🤖")

# সাধারণ মেসেজ হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"তুমি বলেছো: {message.text} ✨")

# বট চালু করো
print("বট চলছে... 🚀")
bot.infinity_polling()
