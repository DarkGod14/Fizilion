# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
#
#
#Modified by @PrajjuS
""" Userbot module for other small commands. """

import io
import sys
from os import execl
from random import randint
from time import sleep

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, trgg
from userbot.events import register
from userbot.utils import time_formatter


@register(outgoing=True, pattern="^\{trg}random".format(trg=trgg))
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit(
        "**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" + itemo[index] + "`"
    )


@register(outgoing=True, pattern="^\{trg}sleep ([0-9]+)$".format(trg=trgg))
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    counter = int(time.pattern_match.group(1))
    await time.edit("`Going For Sleep`")
    if BOTLOG:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID,
            f"You put the bot to sleep for {str_counter}.",
        )
    sleep(counter)
    await time.edit("`OK, I'm awake now.`")


@register(outgoing=True, pattern="^\{trg}shutdown$".format(trg=trgg))
async def killbot(shut):
    """For .shutdown command, shut the bot down."""
    await shut.edit("`Shutting The Power Off`")
    if BOTLOG:
        await shut.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down")
    await bot.disconnect()


@register(outgoing=True, pattern="^\{trg}restart$".format(trg=trgg))
async def killdabot(reboot):
    await reboot.edit("`Restarting`")
    if BOTLOG:
        await reboot.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot Restarted")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()


@register(outgoing=True, pattern="^\{trg}readme$".format(trg=trgg))
async def reedme(event):
    await event.edit(
        "Here's something for you to read:\n"
        "\n[Fizilions README.md file](https://github.com/FrosT2k5/ProjectFizilion/blob/demon/README.md)"
)


@register(outgoing=True, pattern="^\{trg}guide$".format(trg=trgg))
async def guidee(event):
    await event.edit(
        "*Guide on Deploying Fizilion*\n"
        "•[Reading Guide](https://elytra8.github.io/ProjectFizilion)\n"
        "•[Yt Guide](https://youtu.be/tJzmrTq09tA)\n"
)


# Copyright (c) Gegham Zakaryan | 2019
@register(outgoing=True, pattern="^\{trg}repeat (.*)".format(trg=trgg))
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(" ", 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^\{trg}repoo$".format(trg=trgg))
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        "[Click here](https://github.com/FrosT2k5/ProjectFizilion) to open Fizilion's GitHub Repo."
    )

@register(outgoing=True, pattern="^\{trg}repo$".format(trg=trgg))
async def repo_is_heree(wannaseee):
    """ For .repo command, just returns the repo URL. """
    await wannaseee.edit(
        "[Click here](https://github.com/DarkGod14/Fizilion) to open my fork of Fizilion's GitHub Repo."
    )

@register(outgoing=True, pattern="^\{trg}deploy$".format(trg=trgg))
async def repo_is_here(wannasee):
    """ For .deploy command, just returns the heroku deploying URL. """
    await wannasee.edit(
        "[Click here](https://heroku.com/deploy?template=https://github.com/DarkGod14/Fizilion/tree/main) to deploy Fizilion Userbot on Heroku."
    )

@register(outgoing=True, pattern="^\{trg}support$".format(trg=trgg))
async def grup(sapot):
    await sapot.edit("**Channel:** @CosmicUserbot\n**Support Group:** @CosmicUserbotChat")
    
@register(outgoing=True, pattern="^\{trg}raw$".format(trg=trgg))
async def raw(rawtext):
    the_real_message = None
    reply_to_id = None
    if rawtext.reply_to_msg_id:
        previous_message = await rawtext.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = rawtext.reply_to_msg_id
    else:
        the_real_message = rawtext.stringify()
        reply_to_id = rawtext.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await rawtext.edit("`Check the userbot log for the decoded message data !!`")
        await rawtext.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`",
        )


CMD_HELP.update(
    {
        "misc": ".random <item1> <item2> ... <itemN>"
"\nUsage: Get a random item from the list of items.\n\n"
".sleep <seconds>"
"\nUsage: hibernate your userbot.\n\n"
".shutdown"
"\nUsage: Shutdowns Your Bot.\n\n"
".repo"
"\nUsage: If you are curious what makes the userbot work, this is what you need.\n\n"
".readme"
"\nUsage: Provide links to setup the userbot and it's modules\nAnd .support for support group\n\n"
".guide"
"\nUsage: Provides Full guide to setup Fizilion Userbot.\n\n"
".repeat <no.> <text>"
"\nUsage: Repeats the text for a number of times. Don't confuse this with spam tho.\n\n"
".restart"
"\nUsage: Restarts the bot !!\n\n"
".raw"
"\nUsage: Get detailed JSON-like formatted data about replied message."
".deploy"
"\nUsage: Get link to deploy Fizilion Userbot on Heroku."
     }
)
