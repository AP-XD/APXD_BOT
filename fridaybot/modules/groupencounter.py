# Imported by @Crackexy File Provided By @StressedGuy
# Dont Know The Real Owner Or Creator So Credits To owner 🤷‍♂️

from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName

from fridaybot import CMD_HELP, bot
from fridaybot.events import admin_cmd

client = bot


async def get_user_from_event(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit(f"* Pass The User's Username, Id or Reply!**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Failed \n **Error**\n", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@borg.on(ChatAction)
async def handler(tele):
    if tele.user_joined or tele.user_added:
        try:
            from fridaybot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await tele.get_user()
            gmuted = is_gmuted(guser.id)
        except:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await tele.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                tele.chat_id, guser.id, view_messages=False
                            )
                            await tele.reply(
                                f"**Gbanned User Joined!!!**\n"
                                f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Action** : **Banned**"
                            )
                        except:
                            return


@borg.on(admin_cmd(pattern="gban(?: |$)(.*)"))
async def gspider(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("**GBANNING THE USER...**")
    else:
        rkp = await lazy.edit("**PROCESSING...**")
    me = await rk.client.get_me()
    await rkp.edit(f"**GBANNING THE USER!!!**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    else:
        rk.chat.title
    try:
        user, reason = await get_user_from_event(rk)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await rkp.edit("**Gban Can't Be Used In Private Chats/Groups**")
    if user:
        if user.id == 1054081968:
            return await rkp.edit(
                "**Lol? Are You Dumb Retard? I Will Never Do Anything Against My Creator**"
            )
        try:
            from fridaybot.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await rk.client(BlockRequest(user))
        except:
            pass
        testrk = [
            d.entity.id
            for d in await rk.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await rkp.edit(
                    f"**USER IS BEING BANNED!!!\nUser Gbanned in {a} chats...**"
                )
            except:
                b += 1
    else:
        await rkp.edit(f"**Reply to a user!! **")
    try:
        if gmute(user.id) is False:
            return await rkp.edit(f"**Error! User Probably Already Gbanned.**")
    except:
        pass
    return await rkp.edit(
        f"**USER GBANNED❗❗❗**\n**Person's Name** : {user.first_name}\n**Victim's Id** :{user.id}\n**GBanned By** : @{me.username}\n**Affected Chats** : {a} \n**User Was Blocked and added to CrackBot Gban List.**"
    )


@borg.on(admin_cmd(pattern="ungban(?: |$)(.*)"))
async def gspider(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("**UnGbanning The User**")
    else:
        rkp = await lazy.edit("**Processing...**")
    me = await rk.client.get_me()
    await rkp.edit(f"**Requesting To UnGban User!!!**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    else:
        rk.chat.title
    try:
        user, reason = await get_user_from_event(rk)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await rkp.edit(f"**Error! Unknown User.**")
    if user:
        if user.id == 1054081968:
            return await rkp.edit(f"**Error! cant ungban this user.**")
        try:
            from fridaybot.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await rk.client(UnblockRequest(user))
        except:
            pass
        testrk = [
            d.entity.id
            for d in await rk.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await rkp.edit(
                    f"**Requesting  to UnGban User!\nUser UnGbanned in {a} chats.....**"
                )
            except:
                b += 1
    else:
        await rkp.edit(f"**Reply To A User!!! **")
    try:
        if ungmute(user.id) is False:
            return await rkp.edit(f"**Error! User probably already ungbanned.**")
    except:
        pass
    return await rkp.edit(
        f"**UnGbanned**\n**USER : [{user.first_name}](tg://user?id={user.id}) **in {a} chat(s) , UnBlocked and Removed User From Gban List**"
    )


CMD_HELP.update(
    {
        "gban": "!gban <username> / <userid> / <reply to a user>\
\n**Usage**: Globel ban the person in all groups, channels , block in pm , add gban watch (use with solution) \
\n\n!ungban <username> / <userid> / <reply to a user>\
\n**Usage**: unban user from all groups, channels , remove user from gban watch.\
"
    }
)
