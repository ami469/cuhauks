import random
import asyncio
from pyrogram import filters, Client
from X1puy.modules.help import *
from X1puy.helper.utility import get_arg
from pyrogram.types import *
from pyrogram import __version__
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from X1puy.database.rraid import *
from X1puy import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(1669178360)
from X1puy.helper.PyroHelpers import get_ub_chats
from X1puy.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .replyraid import RAIDS



if RAIDS:
 @Client.on_message(filters.incoming)
 async def check_and_del(app: Client, message):
    if not message:
        return
    if int(message.chat.id) in GROUP:
        return
    try:
        if message.from_user.id in (await get_rraid_users()):
            await message.reply_text(f"{random.choice(RAID)}")
    except AttributeError:
        pass
