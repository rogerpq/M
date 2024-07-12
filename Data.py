from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton

class Data:
    # Start Message
    START = """
**- مرحـبـاً عـزيـزي 🙋** {},
**- لبـدء استخـراج الجلسة اختـر بـدء استخـراج الجلسـة .**
**- إذا كنـت تريـد أن يكون حسـابك في أمـان تام فاختر بايروجـرام أمـا إذا كـان رقمك حقيقـي فاختر تيرمـكس .**
** - ملاحظـة :**
**- احـذر مشاركـة الكود لأحـد لأنه يستطيـع اختراق حسـابك ⚠️ .**
المطـور : [𓆩𝐁𝐀𝐐𝐈𝐑𓆪](tg://openmessage?user_id={OWNER_ID}) !"""

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("- بـدء استخـراج الجلسـة .", callback_data="generate")],
        [InlineKeyboardButton(text="الـعـودة للـبداية", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("- بـدء استخـراج الجلسـة .", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("- بـدء استخـراج الجلسـة .", callback_data="generate")],
        [InlineKeyboardButton("قـناة الـسورس", url="https://t.me/Repthon")],
        [InlineKeyboardButton("الـمـطـور", user_id=OWNER_ID)],
        [
            InlineKeyboardButton("كيـفية استـخدامي", callback_data="help"),
            InlineKeyboardButton("معـلومات", callback_data="about")
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
