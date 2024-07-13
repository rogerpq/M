from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

class Data:
    # Start Message
    START = """
**- مرحـبـاً عـزيـزي 🙋** {},
**- لبـدء استخـراج الجلسة اختـر بـدء استخـراج الجلسـة .**
**- إذا كنـت تريـد أن يكون حسـابك في أمـان تام فاختر بايروجـرام أمـا إذا كـان رقمك حقيقـي فاختر تيرمـكس .**
** - ملاحظـة :**
**- احـذر مشاركـة الكود لأحـد لأنه يستطيـع اختراق حسـابك ⚠️ .**
المطـور : [𓆩𝐁𝐀𝐐𝐈𝐑𓆪](tg://openmessage?user_id=5502537272) !"""

    buttons = [
        [InlineKeyboardButton(text="- بـدء استخـراج الجلسـة .", callback_data="generate")],
        [InlineKeyboardButton(text="قـناة الـسورس", url="https://t.me/Repthon")],
        [InlineKeyboardButton("الـمـطـور", url="https://telegram.dog/E_7_V")],
        [
            InlineKeyboardButton(text="كيـفية استـخدامي", callback_data="HELP"),
            InlineKeyboardButton(text="معـلومات", callback_data="about")
      ]
    ]


    # Help Message
    HELP = """
✨ **Available Commands** ✨

/help - How to use this bot
/start - Start Bot
/generate - Start Generating Session
/cancel - Cancel process
/restart - Restart process
"""
