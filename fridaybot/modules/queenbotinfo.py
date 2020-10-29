

import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from fridaybot.utils import admin_cmd
import time
from fridaybot import ALIVE_NAME

naam = str(ALIVE_NAME)

bot = "@queendevilbot"

@borg.on(admin_cmd("qinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return    
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/info")
              audio = await conv.get_response()
              final = ("If you would like to know more about this user, use /info <userid/username> in @queendevilbot." , "")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @queendevilbot `and retry!")
    elif "@" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/info " + sysarg)
              audio = await conv.get_response()
              final = ("If you would like to know more about this user, use /info <username/userid> in @queendevilbot." , "")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @queendevilbot `and try again!")
    elif "" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/info " + sysarg)
              audio = await conv.get_response()
              final = ("If you would like to know more about this user go to PM hahahah." , "")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @queendevilbot `and try again!")