from telethon import events
import io
from userbot.utils import admin_cmd
import asyncio

@borg.on(admin_cmd(pattern="mkc (.*)"))
async def monu(mkc):
	name = mkc.pattern_match.group(1)
	A = (f"**{name} madharchod h uski maa ki choot uski maa ko ulta taang ke pelangai tab usko pata chalega.\n\n\n**"
	    f"{name} ki maa ka bhosra\n"
	    "Sale randi ke aulad\n"
	    f"{name} Madharjatt \n"
	    "Tere khandan ko kutta chode \n"
	    f"Randi Jatt {name} ki MKC \n")
	await mkc.edit(A)
	
# ©VaibhavRaj jo edit kiya uski maa chod deni h
#© @dead_yt - Telegram

