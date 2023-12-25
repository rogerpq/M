from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(Client: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await Client.get_chat_member(MUST_JOIN, Client.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await Client.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await Client.reply_photo(
                    photo="https://telegra.ph/file/5eb95caa40488cea43cd3.jpg", caption=f"» عـذرًا عـزيـزي عليك الاشتـراك في قنـاة البـوت !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("- قنـاة السـورس .", url=link),
                            ]
                        ]
                    )
                )
                await Client.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
