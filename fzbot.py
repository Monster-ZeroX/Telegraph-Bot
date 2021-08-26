import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Fzbot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Fzbot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Fzbot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm Telegraph Bot

I can upload photos or videos to telegraph.

Hit help button to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "💠Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "🖤Channel", url="https://t.me/FZBOTS")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Fzbot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Fzbot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!

Just send a photo or video less than 5mb file size, I'll upload it to telegraph.

@FZBOTS</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "🧮About", callback_data="about"),
                                  ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Fzbot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Fzbot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b>⚜️Developer:</b> <a href="https://t.me/FZBOTS">FZ BOTS🇱🇰</a>

<b>🔆Language:</b> <a href="https://www.python.org/">Python 3</a>

<b>♻️Library:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>@FZBOTS</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "❌Close", callback_data="close")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Fzbot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Your File Is Successfully Uploaded To Telegraph!\n\n📚https://telegra.ph{response[0]}\n\nJoin @FZBOTS**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Fzbot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Your File Is Successfully Uploaded To Telegraph!\n\n📚https://telegra.ph{response[0]}\n\nJoin @FZBOTS**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Fzbot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Your File Is Successfully Uploaded To Telegraph!\n\n📚https://telegra.ph{response[0]}\n\nJoin @FZBOTS**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Fzbot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @FZBOTS
"""
)

Fzbot.run()
