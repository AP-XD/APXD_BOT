#    Copyright (C) 2020  sandeep.n(π.$)
# baning spmmers plugin for catfridaybot by @sandy1709 and @mrconfused
# included both cas(combot antispam service) and spamwatch (need to add more feaututres)


from requests import get
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

from .. import LOGS
from . import spamwatch

if Config.PRIVATE_GROUP_BOT_API_ID is None:
    BOTLOG = False
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID

if Config.ANTISPAMBOT_BAN:

    @borg.on(events.ChatAction())
    async def _(event):
        chat = event.chat_id
        if event.user_joined or event.user_added:
            user = await event.get_user()
            catadmin = await is_admin(bot, chat, bot.uid)
            if not catadmin:
                return
            catbanned = None
            adder = None
            ignore = False
            if event.user_added:
                try:
                    adder = event.action_message.from_id
                except AttributeError:
                    return
            async for admin in bot.iter_participants(
                event.chat_id, filter=ChannelParticipantsAdmins
            ):
                if admin.id == adder:
                    ignore = True
                    break
            if ignore:
                return
            if spamwatch:
                ban = spamwatch.get_ban(user.id)
                if ban:
                    hmm = await event.reply(
                        f"[{user.first_name}](tg://user?id={user.id}) was banned by spamwatch For the reason `{ban.reason}`"
                    )
                    try:
                        await bot.edit_permissions(chat, user.id, view_messages=False)
                        catbanned = True
                    except Exception as e:
                        LOGS.info(e)
                if not catbanned:
                    try:
                        casurl = "https://api.cas.chat/check?user_id={}".format(user.id)
                        data = get(casurl).json()
                    except Exception as e:
                        LOGS.info(e)
                        data = None
                    if data and data["ok"]:
                        reason = f"[Banned by Combot Anti Spam](https://cas.chat/query?u={user.id})"
                        hmm = await event.reply(
                            f"[{user.first_name}](tg://user?id={user.id}) was banned by Combat anti-spam service(CAS) For the reason check {reason}"
                        )
                        try:
                            await bot.edit_permissions(
                                chat, user.id, view_messages=False
                            )
                            catbanned = True
                        except Exception as e:
                            LOGS.info(e)
                if BOTLOG and catbanned:
                    await bot.send_message(
                        BOTLOG_CHATID,
                        "#ANTISPAMBOT\n"
                        f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                        f"**Chat :** {event.chat.title} (`{event.chat_id}`)\n"
                        f"**Reason :** {hmm.text}",
                    )

    # Admin checker by uniborg
    async def is_admin(client, chat_id, user_id):
        if not str(chat_id).startswith("-100"):
            return False
        try:
            req_jo = await client(
                GetParticipantRequest(channel=chat_id, user_id=user_id)
            )
            chat_participant = req_jo.participant
            if isinstance(
                chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
            ):
                return True
        except Exception:
            return False
        else:
            return False
