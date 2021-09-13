from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CUJU0dgACAppgyWsRKZJ0W4hbRKdVMYuxwb50wwACgxcAAtqjlSw9sWir1m6CTx8E")
    await message.reply_text(
        f"""**Dear {message.from_user.first_name}!

😁 I am Miss Rose Music Player. 

🥳 I can play music in your Telegram Group's Voice Chat😉


⚜️You can write to the music player account to get support 🔱

💎 Miss Rose Music PLAYER @missroseMusicPlayer


My commands - type  /help to get commands, which work in grp

Thanks for using .

Regrards [MİSS KİNG](https://t.me/telewistkral)
**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 SUPPORT 🛠", url="https://t.me/telegram")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/MarieNews"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/MarieNews"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/MissRoseMusic_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⭐MİSSROSEBOT MUSIC PLAYER IS ALWAYS ACTIVE!!⭐**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/MarieNews")
                ]
            ]
        )
   )
