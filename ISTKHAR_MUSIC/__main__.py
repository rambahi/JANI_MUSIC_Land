import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ISTKHAR_MUSIC import LOGGER, app, userbot
from ISTKHAR_MUSIC.core.call import noor
from ISTKHAR_MUSIC.misc import sudo
from ISTKHAR_MUSIC.plugins import ALL_MODULES
from ISTKHAR_MUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ISTKHAR_MUSIC.plugins" + all_module)
    LOGGER("ISTKHAR_MUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await noor.start()
    try:
        await noor.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("ISTKHAR_MUSIC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await noor.decorators()
    LOGGER("ISTKHAR_MUSIC").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @Jani_RP ᴊᴏɪɴ @Jani_RP , @Jani_Music_robot ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ISTKHAR_MUSIC").info("Stopping istkhar Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
