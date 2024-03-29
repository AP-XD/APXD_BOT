from datetime import datetime

from fridaybot import *
from fridaybot.events import *

DELETE_TIMEOUT = 5
import asyncio

from fridaybot import CMD_HELP
from fridaybot.utils import *


@borg.on(admin_cmd(pattern="sqlsend (?P<shortname>\w+)$"))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./fridaybot/helper//{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("Uploaded {} in {} seconds".format(input_str, time_taken_in_ms))
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


CMD_HELP.update(
    {
        "helpersender": ".hlpsend <sql_helpername>\
\nUsage: send the l helper\
\n\n``\
\n****\
"
    }
)
