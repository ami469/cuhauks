import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "X1puy"])

async def join(client):
    try:
        await client.join_chat("TheUpdatesChannel")
    except BaseException:
        pass
