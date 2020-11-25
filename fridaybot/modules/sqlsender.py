from fridaybot import *
from fridaybot import CMD_HELP
from fridaybot.events import *
from fridaybot.utils import *


@borg.on(admin_cmd(pattern="sqlsend (?P<shortname>\w+)$"))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./fridaybot/modules/sql_helper/{}.py".format(input_str)

    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )

    await event.edit("Uploaded {} ".format(input_str))
    await event.delete()


CMD_HELP.update(
    {
        "sqlsender": "`.sqlsend <sql_helpername>`\
\n**Usage:** send the sql helper\
\n\n``\
\n****\
"
    }
)
