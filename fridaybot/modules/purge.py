# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for purging unneeded messages(usually spam or ot). """

from asyncio import sleep

from telethon.errors import rpcbaseerrors

from fridaybot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from fridaybot.utils import errors_handler, register, friday_on_cmd


@friday.on(friday_on_cmd(pattern="purge$"))
async def fastpurger(purg):
    if purg.fwd_from:
        return
    """ For .purge command, purge all messages starting from the reply. """
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )


@friday.on(friday_on_cmd(pattern="purgeme"))
async def purgeme(delme):
    if delme.fwd_from:
        return
    """ For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )
    i = 1


@friday.on(friday_on_cmd(pattern="del"))
async def delete_it(delme):
    if delme.fwd_from:
        return
    """ For .del command, delete the replied message. """
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Deletion of message was successful"
                )
        except rpcbaseerrors.BadRequestError:
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Well, I can't delete a message"
                )


@friday.on(friday_on_cmd(pattern="edit"))
async def editer(edit):
    if edit.fwd_from:
        return
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await edit.client.send_message(
            BOTLOG_CHATID, "Edit query was executed successfully"
        )


@friday.on(friday_on_cmd(pattern="sd"))
async def selfdestruct(destroy):
    if destroy.fwd_from:
        return
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID, "sd query done successfully")


CMD_HELP.update(
    {
        "purge": ".purge\
        \nUsage: Purges all messages starting from the reply."
    }
)

CMD_HELP.update(
    {
        "purgeme": ".purgeme <x>\
        \nUsage: Deletes x amount of your latest messages."
    }
)

CMD_HELP.update(
    {
        "del": ".del\
\nUsage: Deletes the message you replied to."
    }
)

CMD_HELP.update(
    {
        "edit": ".edit <newmessage>\
\nUsage: Replace your last message with <newmessage>."
    }
)

CMD_HELP.update(
    {
        "sd": ".sd <x> <message>\
\nUsage: Creates a message that selfdestructs in x seconds.\
\nKeep the seconds under 100 since it puts your bot to sleep."
    }
)
