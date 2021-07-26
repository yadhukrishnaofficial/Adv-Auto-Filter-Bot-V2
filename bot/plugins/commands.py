#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
from bot import FORCESUB_CHANNEL

db = Database()
FMSG_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

🗣️ചോദിക്കുന്ന സിനിമകൾ നിങ്ങൾക്ക് ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ താഴെ കൊടുത്തിട്ടുള്ള ചാനലിൽ ജോയിൻ ചെയ്യണം. ജോയിൻ ചെയ്ത ശേഷം വീണ്ടും ഗ്രൂപ്പിൽ പോയി ആ ബട്ടനിൽ അമർത്തിയാൽ നിങ്ങൾക്ക് ഞാൻ ആ സിനിമ പ്രൈവറ്റ് ആയി അയച്ചു തരുന്നതാണ്..😍

🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈

👇 𝗖𝗹𝗶𝗰𝗸 𝗧𝗵𝗲 𝗝𝗼𝗶𝗻 & 𝗧𝗿𝘆 👇"""
@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):   
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
            update_channel = FORCESUB_CHANNEL
            if update_channel:
                try:
                    user = await bot.get_chat_member(update_channel, update.chat.id)
                    if user.status == "kicked":
                        await update.reply_text("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
                        return
                except UserNotParticipant:
                    #await update.reply_text(f"Join @{update_channel} To Use Me")
                    await update.reply_text(
                        text=FMSG_TXT,
                        parse_mode="md",
                        reply_markup=InlineKeyboardMarkup([
                            [ InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 & 𝗧𝗿𝘆", url=f"https://t.me/{update_channel}")]
                      ])
                    )
                    return
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/CrazyBotsz"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
            update_channel = FORCESUB_CHANNEL
            if update_channel:
                try:
                    user = await bot.get_chat_member(update_channel, update.chat.id)
                    if user.status == "kicked":
                        await update.reply_text("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
                        return
                except UserNotParticipant:
                    #await update.reply_text(f"Join @{update_channel} To Use Me")
                    await update.reply_text(
                        text=FMSG_TXT,
                        parse_mode="md",
                        reply_markup=InlineKeyboardMarkup([
                            [ InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 & 𝗧𝗿𝘆", url=f"https://t.me/{update_channel}")]
                      ])
                    )
                    return
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/CrazyBotsz"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
            update_channel = FORCESUB_CHANNEL
            if update_channel:
                try:
                    user = await bot.get_chat_member(update_channel, update.chat.id)
                    if user.status == "kicked":
                        await update.reply_text("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
                        return
                except UserNotParticipant:
                    #await update.reply_text(f"Join @{update_channel} To Use Me")
                    await update.reply_text(
                        text=FMSG_TXT,
                        parse_mode="md",
                        reply_markup=InlineKeyboardMarkup([
                            [ InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 & 𝗧𝗿𝘆", url=f"https://t.me/{update_channel}")]
                      ])
                    )
                    return
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/YKCineWorldOfficial"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('📌𝘎𝘳𝘰𝘶𝘱', url='https://t.me/Cine_world_official'),
        InlineKeyboardButton('📌𝘊𝘩𝘢𝘯𝘯𝘦𝘭', url ='https://t.me/YKCineWorldOfficial')
    ],[
        InlineKeyboardButton('📌𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘭𝘪𝘴𝘵', url='https://t.me/YKchannellist')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
