from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    TECH_VJ_START_TEXT = """
<b>ʜᴇʟʟᴏ {} 😎

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴀᴅᴠᴀɴᴄᴇ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ 🤖

ɢɪᴠᴇ ᴍᴇ ᴀɴʏ ʟɪɴᴋ ɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ɪɴᴛᴏ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ

ᴛʜɪs ʙᴏᴛ ɪs ᴘᴏᴡᴇʀᴇᴅ ʙʏ NANO</b>
"""

    TECH_VJ_HELP_TEXT = """
<b> 🌟 ғᴇᴀᴛᴜʀᴇs :-

💫 ᴜᴘʟᴏᴀᴅ <a href="https://ytdl-org.github.io/youtube-dl/supportedsites.html">ʏᴛ-ᴅʟᴘ sᴜᴘᴘᴏʀᴛᴇᴅ ʟɪɴᴋs</a> ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ.

💫 ᴜᴘʟᴏᴀᴅ ʜᴛᴛᴘ/ʜᴛᴛᴘs ᴀs ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ.

💫 ᴜᴘʟᴏᴀᴅ ᴢᴇᴇ5, sᴏɴʏ.ʟɪᴠᴇ, ᴠᴏᴏᴛ ᴀɴᴅ ᴍᴜᴄʜ ᴍᴏʀᴇ.

💫 ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ Sᴜᴘᴘᴏʀᴛ.

💫 ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ʙʏ /broadcast ᴄᴏᴍᴍᴀɴᴅ

🧩 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ :-

🔴 How To Upload File Or Media 

➪ Send Your Link For Upload File Or Media.

🔴 How to set thumbnail

➪ Send Your Thumbnail Photo And Permanent Added Your Photo.

🔴 How To Deleting Thumbnail

➪ Send /delthumb To Delete Your Thumbnail.

🔴 How To Show Thumbnail 

➪ Send /showthumb To View Custom Thumbnail </b> 
"""

    TECH_VJ_ABOUT_TEXT = """
<b> 😎 My Name : Nano URL Uploader Bot 🤖

🗒️ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ 3.10.5</a>

🇵🇲 ғʀᴀᴍᴇᴡᴏʀᴋ : <a href="https://docs.pyrogram.org/">ᴘʏʀᴏɢʀᴀᴍ 2.0.30</a>

🥸 ᴅᴇᴠᴇʟᴏᴘᴇʀ : NANO</b>

"""

    
    TECH_VJ_START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🛑 ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('🧐 ᴀʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('❌ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    TECH_VJ_HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('🧐 ᴀʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('❌ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    TECH_VJ_ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('🧐 ʜᴇʟᴘ', callback_data='help')
        ], [
            InlineKeyboardButton('❌ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    
    TECH_VJ_ERROR = "<b>ᴇʀʀᴏʀ : {}</b>"

    
    TECH_VJ_FORMAT_SELECTION = "<b>ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇꜱɪʀᴇᴅ ғᴏʀᴍᴀᴛ: ғɪʟᴇ ꜱɪᴢᴇ ᴍɪɢʜᴛ ʙᴇ ᴀᴘᴘʀᴏxɪᴍᴀᴛᴇ \nɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ, ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ʙᴇғᴏʀᴇ ᴏʀ ǫᴜɪᴄᴋʟʏ ᴀғᴛᴇʀ ᴛᴀᴘᴘɪɴɢ ᴏɴ ᴀɴʏ ᴏғ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ.\nʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ /delthumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴀᴜᴛᴏ-ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ.</b>"
    TECH_VJ_SET_CUSTOM_USERNAME_PASSWORD = """<b>Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀᴇᴍɪᴜᴍ ᴠɪᴅᴇᴏꜱ, ᴘʀᴏᴠɪᴅᴇ ɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ғᴏʀᴍᴀᴛ:\nURL | ғɪʟᴇɴᴀᴍᴇ | ᴜꜱᴇʀɴᴀᴍᴇ | ᴘᴀꜱꜱᴡᴏʀᴅ</b>"""
    TECH_VJ_DOWNLOAD_START = "<b>ꜱᴛᴀʀᴛɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...</b>"
    TECH_VJ_NO_DOWNLOAD_LINK = "<b>ɴᴏ ᴠᴀʟɪᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴡᴀꜱ ꜰᴏᴜɴᴅ. ᴄᴀɴ ᴜꜱᴇ ᴍᴀɴᴜᴀʟ ᴍᴏᴅᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ʙʏ ꜰᴏʟʟᴏᴡɪɴɢ ᴀʙᴏᴠᴇ ꜱᴛᴇᴘꜱ.</b>"
    TECH_VJ_DOWNLOAD_UNABLE_FORMAT = "<b>ɴᴏᴛ ᴀʙʟᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ʀᴇQᴜᴇꜱᴛ. ꜱᴏʀʀʏ...</b>"
    TECH_VJ_DOWNLOADING_CUSTOM_THUMB_NAIL = "<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴜꜱᴇʀ ᴛʜᴜᴍʙɴᴀɪʟ...</b>"
    TECH_VJ_UPLOAD_START = "<b>ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ...</b>"
    TECH_VJ_DOWNLOAD_COMPLETE = "<b>ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇ!</b>"
    TECH_VJ_SAVE_THUMBNAIL_ERROR = "<b>ᴇʀʀᴏʀ : ꜱᴀᴠɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ ꜰᴀɪʟᴇᴅ...</b>"
    TECH_VJ_DOWNLOAD_ERROR = "<b>ᴇʀʀᴏʀ : {}</b>"
    TECH_VJ_SENDING_FILE_TO_TELEGRAM = "<b>ꜱᴇɴᴅɪɴɢ ғɪʟᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ...</b>"
    TECH_VJ_SENDING_FILE_ERROR = "<b>ᴇʀʀᴏʀ : ꜱᴇɴᴅɪɴɢ ғɪʟᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ꜰᴀɪʟᴇᴅ...</b>"
    TECH_VJ_SAVED_CUSTOM_THUMB_NAIL = "<b>ᴄᴜꜱᴛᴏᴍ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ. Tʜɪꜱ ɪᴍᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴜꜱᴇᴅ ɪɴ ᴛʜᴇ ᴠɪᴅᴇᴏ / ғɪʟᴇ.</b>"
    TECH_VJ_DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀᴇᴅ ꜱᴜᴄᴄᴇꜱғᴜʟʟʏ.</b>"
    TECH_VJ_CUSTOM_CAPTION_UL_FILE = "<b>{}</b>"
    TECH_VJ_NO_VOID_FORMAT_FOUND = "<b>ᴇʀʀᴏʀ...\nTᴇᴄʜ VJ ꜱᴀɪᴅ: {}</b>"
    TECH_VJ_REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "<b>ʀᴇᴘʟʏ /generatecustomthumbnail ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴀʟʙᴜᴍ, ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙᴀɪʟ</b>"
    TECH_VJ_UPLOAD_COMPLETE = "<b>ᴜᴘʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇ!</b>"
    TECH_VJ_UPLOAD_AS_DOC = "<b>ᴜᴘʟᴏᴀᴅ ᴀꜱ ᴅᴏᴄᴜᴍᴇɴᴛ...</b>"
    TECH_VJ_UPLOAD_AS_VIDEO = "<b>ᴜᴘʟᴏᴀᴅ ᴀꜱ ᴠɪᴅᴇᴏ...</b>"
    TECH_VJ_UPLOAD_AS_ERROR = "<b>ᴜᴘʟᴏᴀᴅ ʀᴇQᴜᴇꜱᴛ ɪꜱ ɴᴏᴛ ᴠᴀʟɪᴅ...</b>"
    TECH_VJ_CANCELLED_MESSAGE = "<b>ᴜᴘʟᴏᴀᴅ ᴄᴀɴᴄᴇʟʟᴇᴅ!</b>"
    TECH_VJ_EXTRACTING = "<b>ᴇxᴛʀᴀᴄᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ...</b>"
    TECH_VJ_FORMAT_SELECTION_TEXT = """<b>ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇꜱɪʀᴇᴅ ғᴏʀᴍᴀᴛ: ғɪʟᴇ ꜱɪᴢᴇ ᴍɪɢʜᴛ ʙᴇ ᴀᴘᴘʀᴏxɪᴍᴀᴛᴇ \nɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ, ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ʙᴇғᴏʀᴇ ᴏʀ ǫᴜɪᴄᴋʟʏ ᴀғᴛᴇʀ ᴛᴀᴘᴘɪɴɢ ᴏɴ ᴀɴʏ ᴏғ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ.\nʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ /delthumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴀᴜᴛᴏ-ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ.</b>"""
    TECH_VJ_SET_CUSTOM_USERNAME_PASSWORD_TEXT = """<b>Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀᴇᴍɪᴜᴍ ᴠɪᴅᴇᴏꜱ, ᴘʀᴏᴠɪᴅᴇ ɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ғᴏʀᴍᴀᴛ:\nURL | ғɪʟᴇɴᴀᴍᴇ | ᴜꜱᴇʀɴᴀᴍᴇ | ᴘᴀꜱꜱᴡᴏʀᴅ</b>"""
    TECH_VJ_EXTRACTING_TEXT = """<b>ᴇxᴛʀᴀᴄᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ...</b>"""
    TECH_VJ_EXTRACT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔗 ᴇxᴛʀᴀᴄᴛ', callback_data='extract')
        ]]
    )
    TECH_VJ_UNKNOWN_FORMAT = "<b>ᴜɴᴋɴᴏᴡɴ ꜰᴏʀᴍᴀᴛ!</b>"
    TECH_VJ_FORMAT_SELECTION_CUSTOM_THUMB_NAIL = "<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ...</b>"
    TECH_VJ_SENDING_DOC = "<b>ꜱᴇɴᴅɪɴɢ ᴠɪᴅᴇᴏ...</b>"
    TECH_VJ_SENDING_DOC_AS_VIDEO = "<b>ꜱᴇɴᴅɪɴɢ ᴠɪᴅᴇᴏ ᴀꜱ ᴅᴏᴄᴜᴍᴇɴᴛ...</b>"
    TECH_VJ_SENDING_VIDEO_AS_DOC = "<b>ꜱᴇɴᴅɪɴɢ ᴠɪᴅᴇᴏ ᴀꜱ ᴠɪᴅᴇᴏ...</b>"
    TECH_VJ_CANCEL_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❌ ᴄᴀɴᴄᴇʟ', callback_data='cancel')
        ]]
    )    

    TECH_VJ_ERROR_YTDLP = "<b>ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ᴛʜɪꜱ ɪꜱꜱᴜᴇ ᴏɴ https://yt-dl.org/bug . ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴛʜᴇ ʟᴀᴛᴇꜱᴛ ᴠᴇʀꜱɪᴏɴ; ꜱᴇᴇ  https://yt-dl.org/update ᴏɴ ʜᴏᴡ ᴛᴏ ᴜᴘᴅᴀᴛᴇ. ʙᴇ ꜱᴜʀᴇ ᴛᴏ ᴄᴀʟʟ ʏᴏᴜᴛᴜʙᴇ-ᴅʟ ᴡɪᴛʜ ᴛʜᴇ --ᴠᴇʀʙᴏꜱᴇ ғʟᴀɢ ᴀɴᴅ ɪɴᴄʟᴜᴅᴇ ɪᴛꜱ ᴄᴏᴍᴘʟᴇᴛᴇ ᴏᴜᴛᴘᴜᴛ.</b>"
