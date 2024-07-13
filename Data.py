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
        [InlineKeyboardButton(text="الـمـطـور", url="https://telegram.dog/E_7_V")],
    ]
