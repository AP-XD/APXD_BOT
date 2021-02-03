# Credits @buddhhu
# This software is a part of https://github.com/buddhhu/Plus

from telethon import functions
from uniborg.util import admin_cmd

f_name = Config.FIRST_NAME
l_name = Config.LAST_NAME
bio = Config.DEF_BIO


@borg.on(admin_cmd(pattern="revert$"))
async def _(event):
    if event.fwd_from:
        return
    await event.client(
        functions.photos.DeletePhotosRequest(
            await event.client.get_profile_photos("me", limit=1)
        )
    )
    reply_message = await event.get_reply_message()
    photo = None
    photo = await borg.download_media(  # pylint:disable=E0602
        reply_message, Config.TMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
    )
    file = await borg.upload_file(photo)  # pylint:disable=E0602
    await event.client(
        functions.account.UpdateProfileRequest(
            first_name=f_name, last_name=l_name, about=bio
        )
    )
    await borg(functions.photos.UploadProfilePhotoRequest(file))  # pylint:disable=E0602
    await event.reply(
        f"Succesfully reverted to your account back with\n**First Name :-** `{f_name}`\n**Last Name :-** `{l_name}`\n**Bio :-** `{bio}`"
    )
    await event.delete()
    await event.client.send_message(
        Config.BOTLOG_CHATID, f"#REVERT\nSuccesfully reverted back to your profile"
    )
