from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""**- مرحـبـًا عـزيـزي 🙋** {msg.from_user.mention},
في {me2},
**- لبـدء استخـراج الجلسة اختـر بـدء استخـراج الجلسـة .**
**- إذا كنـت تريـد أن يكون حسـابك في أمـان تام فاختر بايروجـرام أمـا إذا كـان رقمك حقيقـي فاختر تيرمـكس .**
** - ملاحظـة :**
**- احـذر مشاركـة الكود لأحـد لأنه يستطيـع اختراق حسـابك ⚠️ .**
المطـور : [مـحـمد](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="- بـدء استخـراج الجلسـة .", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("- قنـاة السـورس .", url="https://t.me/Tepthon"),
                    InlineKeyboardButton("- المطـور .", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
