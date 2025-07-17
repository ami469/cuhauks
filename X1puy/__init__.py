import time
from datetime import datetime
from aiohttp import ClientSession
from pyrogram import Client
from config import (
    API_ID,
    API_HASH,
    SUDO_USERS,
    OWNER_ID,
    BOT_TOKEN,
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5,
    STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
)

# Global variabel
StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
clients = []
ids = []
SUDO_USERS.append(OWNER_ID)
aiosession = None  # Akan dibuat saat loop aktif


# Fungsi async utama
async def main(return_objects=False):
    global aiosession, clients, ids

    # Buat aiohttp ClientSession setelah loop aktif
    if aiosession is None:
        aiosession = ClientSession()

    print("LOG: Initializing Clients...")

    # Validasi API ID dan HASH
    api_id = API_ID if API_ID else "6435225"
    api_hash = API_HASH if API_HASH else "4e984ea35f854762dcde906dce426c2d"

    # Bot client
    app = None
    if BOT_TOKEN:
        app = Client(
            name="app",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=BOT_TOKEN,
            plugins=dict(root="X1puy/modules/bot"),
            in_memory=True
        )
    else:
        print("WARNING: BOT TOKEN NOT FOUND ⚡")

    # USER Clients
    def create_client(name, session_string):
        return Client(
            name=name,
            api_id=api_id,
            api_hash=api_hash,
            session_string=session_string,
            plugins=dict(root="X1puy/modules")
        )

    # Tambahkan semua user session jika tersedia
    session_list = [
        STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5,
        STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
    ]

    for i, session in enumerate(session_list, start=1):
        if session:
            name = f"client{i}"
            print(f"{name}: Found.. Starting.. 📳")
            client = create_client(name, session)
            clients.append(client)

    # Return ke main.py jika diminta
    if return_objects:
        return clients, app, ids
