from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Data import Data

#Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot: Client, msg: Message):
	user = (await bot.get_me()).mention
	await bot.send_message(
		msg.chat.id,
		Data.START.format(msg.from_user.mention, user),
		reply_markup=InlineKeyboardMarkup(Data.buttons)
    )
