# Credits @buddhhu
# This software is a part of https://github.com/buddhhu/Plus

from telethon import functions
import fridaybot.utils
from uniborg.util import admin_cmd, sudo_cmd
f_name = Var.FIRST_NAME
l_name = Var.LAST_NAME
bio = Var.DEF_BIO

@borg.on(admin_cmd(pattern="revert$"))
async def _(event):
    if event.fwd_from:
        return
    await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
    await event.client(functions.account.UpdateProfileRequest(first_name=f_name, last_name=l_name, about=bio))
    await event.reply(f"Succesfully reverted to your account back with\n**First Name :-** `{f_name}`\n**Last Name :-** `{l_name}`\n**Bio :-** `{bio}`")
    await event.delete()
    await event.client.send_message(Var.BOTLOG_CHATID, f"#REVERT\nSuccesfully reverted back to your profile")