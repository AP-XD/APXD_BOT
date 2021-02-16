"""
UserBot Module to search the internet
All-in-one by @its_xditya
(c)TeleBot

Available commands:
.ggl - howtogoogle
.duckduckgo - search on duckduckgo
.go - search on google
"""

from re import findall

import requests
from search_engine_parser import GoogleSearch
from googlesearch import search 

from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(outgoing=True, pattern=r"go (.*)"))
async def gsearch(q_event):
    """ For .google command, do a Google search from @borgHelp. """
    match = q_event.pattern_match.group(1)
    query = match
    s = ""
    for j in search(query, num=10, stop=10, pause=2): 
        s = s + j + "\n"
    await q_event.edit(
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + s, link_preview=False
    )


@borg.on(admin_cmd("duckduckgo (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ", "+"))
    if sample_url:
        link = sample_url.rstrip()
        await event.edit(
            "Let me 🦆 DuckDuckGo that for you:\n🔎 [{}]({})".format(input_str, link)
        )
    else:
        await event.edit("something is wrong. please try again later.")


@borg.on(admin_cmd(pattern="ggl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit(
            "[{}]({})\n`Thank me Later 🙃` ".format(input_str, response_api.rstrip())
        )
    else:
        await event.edit("something is wrong. please try again later.")
