import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def cheap(update, context):
    user = update.effective_user
    shopping = [
        "💥 You don't have enough cash. Get rekt.", 
        "🚱 DRILL NO WORK????????", 
        "✅ You made the right choice, good call! Got to your friend's research base and earned $6666."]
    msg = random.choice(shopping)
    if msg == shopping[2]:
        bal.addcoins(user,6666)
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    arctic_handler = CommandHandler('PDBetterStore', cheap)
    dp.add_handler(arctic_handler)
