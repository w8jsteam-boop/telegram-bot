import telebot
import requests

# ============================================
# 🔴 এখানে তোমার পাসওয়ার্ড বসাও
# ============================================
TOKEN = "আপনার_পাসওয়ার্ড_এখানে_বসাও"
# উদাহরণ: TOKEN = "123456789:ABCDEFGHIJKLMNOPQRSTuvwxyz"
# ============================================

# বট তৈরি করো
bot = telebot.TeleBot(TOKEN)

# জোক আনার ফাংশন
def get_random_joke():
    try:
        response = requests.get("https://api.api-ninjas.com/v1/jokes?limit=1")
        if response.status_code == 200:
            joke_data = response.json()
            if joke_data:
                return joke_data[0]['joke']
        return "দুঃখিত, এখন জোক পাওয়া যাচ্ছে না। 😅"
    except:
        return "দুঃখিত, কোনো সমস্যা হয়েছে। 😞"

# /start কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
👋 স্বাগতম! আমি তোমার চ্যাট বট!

আমি যা করতে পারি:
/help - সাহায্য দেখো
/hello - হ্যালো বলো
/joke - মজার জোক শুনো 😄
/about - আমার সম্পর্কে জানো

কমান্ড লিখে দেখো! 🚀
    """
    bot.reply_to(message, welcome_text)

# /help কমান্ড
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
📋 কমান্ডগুলো:
/start - শুরু করো
/help - এই সাহায্য দেখো
/hello - আমাকে হ্যালো বলো
/joke - একটি মজার জোক শুনো 😄
/about - আমার সম্পর্কে জানো

সাধারণ মেসেজ লিখলেও আমি রেসপন্স করব! ✨
    """
    bot.reply_to(message, help_text)

# /hello কমান্ড
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "হ্যালো! 😊 তুমি কেমন আছো?")

# /joke কমান্ড
@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = get_random_joke()
    bot.reply_to(message, f"😄 এখানে একটি জোক:\n\n{joke}")

# /about কমান্ড
@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
🤖 আমার সম্পর্কে:

আমি একটি সহজ টেলিগ্রাম চ্যাট বট যা Python দিয়ে তৈরি।

আমি তোমাকে:
✅ জোক শুনাতে পারি
✅ সাহায্য করতে পারি
✅ চ্যাট করতে পারি

আমাকে কমান্ড দিয়ে ব্যবহার করো! 🚀
    """
    bot.reply_to(message, about_text)

# সাধারণ মেসেজ হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_text = message.text
    bot.reply_to(message, f"তুমি বলেছো: {user_text} ✨\n\n/help লিখে দেখো কী করতে পারি!")

# বট চালু করো
print("=" * 50)
print("🚀 বট চলছে... 🚀")
print("=" * 50)
print("টেলিগ্রামে @Dangesr_bot খুঁজে মেসেজ পাঠাও!")
print("=" * 50)

bot.infinity_polling()
