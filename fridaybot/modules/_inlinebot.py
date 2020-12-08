import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import SearchVideos

from fridaybot import ALIVE_NAME, CMD_HELP, CMD_LIST
from fridaybot.Configs import Config
from fridaybot.modules import inlinestats

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/53aed76a90e38779161b1.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Friday"


@tgbot.on(events.InlineQuery)
async def inline_handler(event):
    builder = event.builder
    result = None
    query = event.text
    if event.query.user_id == bot.uid and query.startswith("Userbot"):
        rev_text = query[::-1]
        buttons = paginate_help(0, CMD_HELP, "helpme")
        result = builder.article(
            "© Userbot Help",
            text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await event.answer([result])
    elif event.query.user_id == bot.uid and query == "stats":
        result = builder.article(
            title="Stats",
            text=f"**Showing Stats For {DEFAULTUSER}'s Friday** \nNote --> Only Owner Can Check This \n(C) @FridayOT",
            buttons=[
                [custom.Button.inline("Show Stats ?", data="terminator")],
                [Button.url("Repo 🇮🇳", "https://github.com/StarkGang/FridayUserbot")],
                [Button.url("Join Channel ❤️", "t.me/Fridayot")],
            ],
        )
        await event.answer([result])
    elif event.query.user_id == bot.uid and query.startswith("**Hello"):
        result = builder.photo(
            file=WARN_PIC,
            text=query,
            buttons=[
                [custom.Button.inline("Spamming", data="dontspamnigga")],
                [
                    custom.Button.inline(
                        "Casual Talk",
                        data="whattalk",
                    )
                ],
                [custom.Button.inline("Requesting", data="askme")],
            ],
        )
        await event.answer([result])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == bot.uid:
        fci = custom.Button.inline("Open Main Menu Again", data="open")
        await event.edit("`Help Menu Closed...!`", buttons=fci)
    else:
        reply_pop_up_alert = "Please get your own fridaybot ,and don't use mine."
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == bot.uid:
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
        # https://t.me/TelethonChat/115200
        await event.edit(buttons=buttons)
    else:
        reply_popp_up_alert = "Please get your own Userbot, and don't use mine!"
        await event.answer(reply_popp_up_alert, cache_time=0, alert=True)


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == bot.uid:  # pylint:disable=E0602
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(
            current_page_number - 1, CMD_HELP, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await event.edit(buttons=buttons)
    else:
        reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
async def rip(event):
    if event.query.user_id == bot.uid:
        text = inlinestats
        await event.answer(text, alert=True)
    else:
        txt = "You Can't View My Masters Stats"
        await event.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
async def rip(event):
    if event.query.user_id == bot.uid:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    text1 = "BC You have Chosen A Prohibited Option. Therefore, Nigga You Have Been Blocked By UserBot. 🇮🇳"
    await event.edit("Choice Not Accepted ❌")
    await borg.send_message(event.query.user_id, text1)
    await borg(functions.contacts.BlockRequest(event.query.user_id))
    await tgbot.send_message(
        LOG_CHAT,
        f"Hello, A Noob [Nibba](tg://user?id={him_id}) Selected Probhited Option, Therefore Blocked.",
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"whattalk")))
async def rip(event):
    if event.query.user_id == bot.uid:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Choice Accepted ✔️")
    text2 = "Ok. Please Wait Until My Master Approves. Don't Spam Or Try Anything Stupid. \nThank You For Contacting Me."
    await borg.send_message(event.query.user_id, text2)
    await tgbot.send_message(
        LOG_CHAT,
        message=f"Hello, A [New User](tg://user?id={him_id}). Wants To Talk With You.",
        buttons=[Button.url("Contact Him", f"tg://user?id={him_id}")],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
async def rip(event):
    if event.query.user_id == bot.uid:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Choice Accepted ✔️")
    text3 = "Ok, Wait. You can Ask After Master Approves You. Kindly, Wait."
    await borg.send_message(event.query.user_id, text3)
    await tgbot.send_message(
        LOG_CHAT,
        message=f"Hello, A [New User](tg://user?id={him_id}). Wants To Ask You Something.",
        buttons=[Button.url("Contact Him", f"tg://user?id={him_id}")],
    )


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"us_plugin_(.*)")
    )
)
async def on_plug_in_callback_query_handler(event):
    if not event.query.user_id == bot.uid:
        sedok = "Who The Fuck Are You? Get Your Own Friday."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    plugin_name = event.data_match.group(1).decode("UTF-8")
    help_string = "Commands found in {}:\n".format(plugin_name)
    k = "💠🔮💎"
    u = 0
    for i in CMD_LIST[plugin_name]:
        u += 1
        help_string += str(k[u % 3]) + " " + i + "\n\n"
    if plugin_name in CMD_HELP:
        help_string += (
            f"**📤 PLUGIN NAME 📤 :** `{plugin_name}` \n\n{CMD_HELP[plugin_name]}"
        )
    else:
        help_string += " CMD_HELP not set yet 😅😅 try\n .help {}".format(plugin_name)

    reply_pop_up_alert = help_string
    reply_pop_up_alert += (
        "\n\n Use .unload {} to remove this plugin\n ©FRIDAY Userbot".format(
            plugin_name
        )
    )
    try:
        if event.query.user_id == bot.uid:
            fci = [
                custom.Button.inline("◤✞ 𝕲𝖔 𝕭𝖆𝖈𝖐 ✞◥", data="backme({})".format(shivam)),
                custom.Button.inline("◤✞ 𝕮𝖑𝖔𝖘𝖊 ✞◥", data="close"),
            ]
            await event.edit(reply_pop_up_alert, buttons=fci)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine for more info visit @DARK_COBRA_SUPPORT!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    except:
        halps = "Do .help {} to get the list of commands.".format(plugin_name)
        await event.edit(halps)
    if len(reply_pop_up_alert) >= 4096:
        crackexy = "`Pasting Your Help Menu.`"
        await event.answer(crackexy, cache_time=0, alert=True)
        out_file = reply_pop_up_alert
        url = "https://del.dog/documents"
        r = requests.post(url, data=out_file.encode("UTF-8")).json()
        url = f"https://del.dog/{r['key']}"

        await event.edit(
            f"Pasted {plugin_name} to {url}", link_preview=False, buttons=fci
        )
    else:
        await event.edit(message=reply_pop_up_alert, buttons=fci)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backme\((.+?)\)")))
async def on_plug_in_callback_query_handler(event):

    if event.query.user_id == bot.uid:
        try:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number, CMD_HELP, "helpme")
            await event.edit(
                f"""Friday Userbot Modules Are Listed Here !\n
For More Help or Support Visit @FridayOT \nCurrently Loaded Plugins: {len(CMD_LIST)}""",
                buttons=buttons,
            )
        except:
            buttons = paginate_help(0, CMD_HELP, "helpme")
            await event.edit(
                f"""Friday Userbot Modules Are Listed Here !\n
For More Help or Support Visit @FridayOT \nCurrently Loaded Plugins: {len(CMD_LIST)}""",
                buttons=buttons,
            )
    else:
        reply_pop_up_alert = (
            "Please get your own Userbot,for more info visit @FRIDAYOT !"
        )
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"open")))
async def opner(event):
    if event.query.user_id == bot.uid:
        current_page_number = 0
        buttons = paginate_help(current_page_number, CMD_LIST, "helpme")
        await event.edit("`>>>\nReopened The Main Menu of \n©FRIDAY` ", buttons=buttons)
    else:
        reply_pop_up_alert = (
            "Please get your own Userbot,for more info visit @FRIDAY_SUPPORT!"
        )
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = Config.NO_OF_ROWS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLUMNS_DISPLAYED_IN_H_ME_CMD
    helpable_modules = []
    for p in loaded_modules:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format("📌", x, "🔥"), data="us_plugin_{}".format(x)
        )
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
            modules[2::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    global shivam
    modulo_page = page_number % max_num_pages
    shivam = modulo_page
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⏪Previous", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("⚡Close⚡", data="close"),
                custom.Button.inline(
                    "Next⏩", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


@tgbot.on(events.InlineQuery(pattern=r"torrent (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    sedlyf = "https://api.sumanjay.cf/torrent/?query=" + starkisnub
    try:
        okpro = requests.get(url=sedlyf, timeout=10).json()
    except:
        pass
    sed = len(okpro)
    if sed == 0:
        resultm = builder.article(
            title="No Results Found.",
            description="Check Your Spelling / Keyword",
            text="**Please, Search Again With Correct Keyword, Thank you !**",
            buttons=[
                [
                    Button.switch_inline(
                        "Search Again", query="torrent ", same_peer=True
                    )
                ],
            ],
        )
        await event.answer([resultm])
        return
    if sed > 30:
        for i in range(30):
            seds = okpro[i]["age"]
            okpros = okpro[i]["leecher"]
            sadstark = okpro[i]["magnet"]
            okiknow = okpro[i]["name"]
            starksize = okpro[i]["size"]
            starky = okpro[i]["type"]
            seeders = okpro[i]["seeder"]
            okayz = f"**Title :** `{okiknow}` \n**Size :** `{starksize}` \n**Type :** `{starky}` \n**Seeder :** `{seeders}` \n**Leecher :** `{okpros}` \n**Magnet :** `{sadstark}` "
            sedme = f"Size : {starksize} Type : {starky} Age : {seds}"
            results.append(
                await event.builder.article(
                    title=okiknow,
                    description=sedme,
                    text=okayz,
                    buttons=Button.switch_inline(
                        "Search Again", query="torrent ", same_peer=True
                    ),
                )
            )
    else:
        for sedz in okpro:
            seds = sedz["age"]
            okpros = sedz["leecher"]
            sadstark = sedz["magnet"]
            okiknow = sedz["name"]
            starksize = sedz["size"]
            starky = sedz["type"]
            seeders = sedz["seeder"]
            okayz = f"**Title :** `{okiknow}` \n**Size :** `{starksize}` \n**Type :** `{starky}` \n**Seeder :** `{seeders}` \n**Leecher :** `{okpros}` \n**Magnet :** `{sadstark}` "
            sedme = f"Size : {starksize} Type : {starky} Age : {seds}"
            results.append(
                await event.builder.article(
                    title=okiknow,
                    description=sedme,
                    text=okayz,
                    buttons=[
                        Button.switch_inline(
                            "Search Again", query="torrent ", same_peer=True
                        )
                    ],
                )
            )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    urllib.parse.quote_plus(testinput)
    results = []
    search = SearchVideos(f"{testinput}", offset=1, mode="dict", max_results=20)
    mi = search.result()
    moi = mi["search_result"]
    if search == None:
        resultm = builder.article(
            title="No Results Found.",
            description="Check Your Spelling / Keyword",
            text="**Please, Search Again With Correct Keyword, Thank you !**",
            buttons=[
                [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
            ],
        )
        await event.answer([resultm])
        return
    for mio in moi:
        mo = mio["link"]
        thum = mio["title"]
        fridayz = mio["id"]
        thums = mio["channel"]
        td = mio["duration"]
        tw = mio["views"]
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
        okayz = f"**Title :** `{thum}` \n**Link :** `{mo}` \n**Channel :** `{thums}` \n**Views :** `{tw}` \n**Duration :** `{td}`"
        hmmkek = f"Channel : {thums} \nDuration : {td} \nViews : {tw}"
        results.append(
            await event.builder.article(
                title=thum,
                description=hmmkek,
                text=okayz,
                buttons=Button.switch_inline(
                    "Search Again", query="yt ", same_peer=True
                ),
            )
        )
    await event.answer(results)


@tgbot.on(events.InlineQuery(pattern=r"jm (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    search = f"http://starkmusic.herokuapp.com/result/?query={starkisnub}"
    seds = requests.get(url=search).json()
    for okz in seds:
        okz["album"]
        okmusic = okz["music"]
        hmmstar = okz["perma_url"]
        singer = okz["singers"]
        hmm = okz["duration"]
        langs = okz["language"]
        hidden_url = okz["media_url"]
        okayz = (
            f"**Song Name :** `{okmusic}` \n**Singer :** `{singer}` \n**Song Url :** `{hmmstar}`"
            f"\n**Language :** `{langs}` \n**Download Able Url :** `{hidden_url}`"
            f"\n**Duration :** `{hmm}`"
        )
        hmmkek = (
            f"Song : {okmusic} Singer : {singer} Duration : {hmm} \nLanguage : {langs}"
        )
        results.append(
            await event.builder.article(
                title=okmusic,
                description=hmmkek,
                text=okayz,
                buttons=Button.switch_inline(
                    "Search Again", query="jm ", same_peer=True
                ),
            )
        )
    await event.answer(results)


@tgbot.on(events.InlineQuery)  # pylint:disable=E0602
async def inline_handler(event):
    builder = event.builder
    query = event.text
    replied_user = await tgbot.get_me()
    firstname = replied_user.username
    if query == None:
        resulte = builder.article(
            title="Usage Guide.",
            description="(C) @FridayOT",
            text=f"**How To Use Me?** \n**Youtube :** `@{firstname} yt <query>` \n**Example :** `@{firstname} yt why we lose song` \n\n**Torrent :** `@{firstname} torrent <query>` \n**Example :** `@{firstname} torrent avengers endgame ` \n\n**JioSaavan :** `@{firstname} jm <query>` \n**Example :** `@{firstname} jm dilbaar`",
            buttons=[
                [Button.url("Contact Me", f"t.me/{firstname}")],
                [Button.switch_inline("Search Youtube", query="yt ", same_peer=True)],
                [
                    Button.switch_inline(
                        "Search Torrent", query="torrent ", same_peer=True
                    )
                ],
                [Button.switch_inline("Search JioSaavn", query="jm ", same_peer=True)],
            ],
        )
        await event.answer([resulte])
