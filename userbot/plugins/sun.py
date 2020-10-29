from telethon import events
import asyncio
from collections import deque
from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"sun"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("😎🌤🌥☀️⛅️🌦🌞"))
	for _ in range(32):
		await asyncio.sleep(0.3)
		await event.edit("".join(deq))
		deq.rotate(1)