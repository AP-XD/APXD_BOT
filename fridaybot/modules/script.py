import asyncio
import os
from os import remove
from subprocess import PIPE
from subprocess import run as runapp
from sys import executable

import pybase64

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd

running_processes: dict = {}


@borg.on(admin_cmd(pattern="^\,term(?: |$|\n)([\s\S]*)"))
async def evaluate(event):
    await event.edit(f"**AP_XD**: `Running Terminal.....`")
    message = str(event.chat_id) + ":" + str(event.message.id)
    if running_processes.get(message, False):
        await event.edit("A process for this event is already running!")
        return
    cmd = event.pattern_match.group(1).strip()
    if not cmd:
        await event.edit("``` Give a command or use !help script.```")
        return
    if cmd in ("fridaybot.session", "env", "printenv"):
        return await event.edit(
            f"`AP_XD:` **Privacy Error, This command not permitted**"
        )
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    running_processes.update({message: process})
    stdout, stderr = await process.communicate()
    not_killed = running_processes.get(message, False)
    if not_killed:
        del running_processes[message]
    text = f"**Terminal Command**: `{cmd}`\n**Return code**: `{process.returncode}`\n\n"
    if stdout:
        text += "\n**[stdout]**\n`" + stdout.decode("UTF-8").strip() + "\n`"
    if stderr:
        text += "\n**[stderr]**\n`" + stderr.decode("UTF-8").strip() + "\n`"
    if stdout or stderr:
        if not len(text) > 4096:
            return await event.edit(text)
    output = open("term.txt", "w+")
    output.write(text)
    output.close()
    await event.client.send_file(
        event.chat_id,
        "term.txt",
        reply_to=event.id,
        caption=f"`AP_XD:` **Output too large, sending as file**",
    )
    os.remove("term.txt")
    return


@borg.on(admin_cmd(pattern=r"^\,exec(?: |$)([\s\S]*)"))
async def run(run_q):
    code = run_q.pattern_match.group(1)

    if not code:
        await run_q.edit(
            f"`AP_XD:` **At least a variable is required to \
execute. Use !help script for an example.**"
        )
        return

    if code in ("fridaybot.session", "env", "printenv"):
        await run_q.edit(f"`AP_XD:` **Privacy Error, This command not permitted**")
        return

    if len(code.splitlines()) <= 5:
        codepre = code
    else:
        clines = code.splitlines()
        codepre = (
            clines[0] + "\n" + clines[1] + "\n" + clines[2] + "\n" + clines[3] + "..."
        )

    command = "".join(f"\n {l}" for l in code.split("\n.strip()"))
    process = await asyncio.create_subprocess_exec(
        executable,
        "-c",
        command.strip(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    if result:
        if len(result) > 4096:
            file = open("exec.txt", "w+")
            file.write(result)
            file.close()
            await run_q.client.send_file(
                run_q.chat_id,
                "exec.txt",
                reply_to=run_q.id,
                caption="`Output too large, sending as file`",
            )
            remove("exec.txt")
            return
        await run_q.edit(
            "**Query: **\n`" f"{codepre}" "`\n**Result: **\n`" f"{result}" "`"
        )
    else:
        await run_q.edit(
            "**Query: **\n`" f"{codepre}" "`\n**Result: **\n`No Result Returned/False`"
        )


@borg.on(admin_cmd(pattern="^\,eval(?: |$)(.*)"))
async def evaluate(query):
    if query.pattern_match.group(1):
        expression = query.pattern_match.group(1)
    else:
        await query.edit(
            f"`AP_XD:` **Please give command type !help script for more info**"
        )
        return

    if expression in ("fridaybot.session", "env", "printenv"):
        await query.edit(f"`AP_XD:` **Privacy Error, This command not permitted**")
        return

    try:
        evaluation = str(eval(expression))
        if evaluation:
            if isinstance(evaluation, str):
                if len(evaluation) >= 4096:
                    file = open("eval.txt", "w+")
                    file.write(evaluation)
                    file.close()
                    await query.client.send_file(
                        query.chat_id,
                        "eval.txt",
                        reply_to=query.id,
                        caption="`Output too large, sending as file`",
                    )
                    remove("eval.txt")
                    return
                await query.edit(
                    "**Query: **\n`"
                    f"{expression}"
                    "`\n**Result: **\n`"
                    f"{evaluation}"
                    "`"
                )
        else:
            await query.edit(
                "**Query: **\n`"
                f"{expression}"
                "`\n**Result: **\n`No Result Returned/False`"
            )
    except Exception as err:
        await query.edit(
            "**Query: **\n`" f"{expression}" "`\n**Exception: **\n" f"`{err}`"
        )


@borg.on(admin_cmd(pattern="^\,hash (.*)"))
async def gethash(hash_q):
    hashtxt_ = hash_q.pattern_match.group(1)
    hashtxt = open("hashdis.txt", "w+")
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = (
        "Text: `"
        + hashtxt_
        + "`\nMD5: `"
        + md5
        + "`SHA1: `"
        + sha1
        + "`SHA256: `"
        + sha256
        + "`SHA512: `"
        + sha512[:-1]
        + "`"
    )
    if len(ans) > 4096:
        hashfile = open("hashes.txt", "w+")
        hashfile.write(ans)
        hashfile.close()
        await hash_q.client.send_file(
            hash_q.chat_id,
            "hashes.txt",
            reply_to=hash_q.id,
            caption="`It's too big, sending a text file instead. `",
        )
        runapp(["rm", "hashes.txt"], stdout=PIPE)
    else:
        await hash_q.reply(ans)


@borg.on(admin_cmd(pattern="^\,base64 (en|de) (.*)"))
async def endecrypt(query):
    if query.pattern_match.group(1) == "en":
        lething = str(pybase64.b64encode(bytes(query.pattern_match.group(2), "utf-8")))[
            2:
        ]
        await query.reply("Encoded: `" + lething[:-1] + "`")
    else:
        lething = str(
            pybase64.b64decode(
                bytes(query.pattern_match.group(2), "utf-8"), validate=True
            )
        )[2:]
        await query.reply("Decoded: `" + lething[:-1] + "`")


CMD_HELP.update(
    {
        "script": "!term\
\nUsage: run  shell command in javes, Javes's os is alpine so use apline commands like !term apk add < packges>\
\n\n!exec \
\nUsage: run python command in javes. like !exec print ('hello')\
\n\n!eval\
\nUsage: Evalute mini-expressions. like !eval 1+1\
\n\n!hash\
\nUsage: find the md5, sha1, sha256, sha512 of the string.\
\n\n!base64 en/de\
\nUsage: find the base64 encode/decode  the given string.  like !base64 en hello\
\n\n**Sodo commands ( type !help sudo for more info)**\
\n .term , .exec , .eval, .base64 en/de , .hash\
"
    }
)
