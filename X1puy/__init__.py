import asyncio
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
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    STRING_SESSION6,
    STRING_SESSION7,
    STRING_SESSION8,
    STRING_SESSION9,
    STRING_SESSION10,
)

# Waktu mulai dan beberapa variabel global lainnya
StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []  # Menyimpan semua Client session yang akan dijalankan
ids = []
SUDO_USERS.append(OWNER_ID)

# Jangan inisialisasi ClientSession() secara global!
aiosession = None

# Fungsi async untuk inisialisasi aiohttp ClientSession
async def init_aiohttp():
    global aiosession
    if aiosession is None:
        aiosession = ClientSession()

# Fungsi async utama untuk memulai semua client dan bot
async def main():
    # Pastikan event loop sudah aktif, lalu inisialisasi ClientSession
    await init_aiohttp()

    # Validasi API_ID dan API_HASH
    if API_ID:
        api_id = API_ID
    else:
        print("WARNING: API ID NOT FOUND, USING DEFAULT VALUE ⚡")
        api_id = "6435225"

    if API_HASH:
        api_hash = API_HASH
    else:
        print("WARNING: API HASH NOT FOUND, USING DEFAULT VALUE ⚡")
        api_hash = "4e984ea35f854762dcde906dce426c2d"

    # Jika BOT_TOKEN ada, kita buat bot client
    bot_app = None
    if BOT_TOKEN:
        bot_app = Client(
            name="app",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=BOT_TOKEN,
            plugins=dict(root="X1puy/modules/bot"),
            in_memory=True,
        )
    else:
        print("WARNING: BOT TOKEN NOT FOUND, PLZ ADD ⚡")

    # Membuat client untuk masing-masing STRING_SESSION jika tersedia
    if STRING_SESSION1:
        print("Client1: Found.. Starting.. 📳")
        client1 = Client(name="one", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION1, plugins=dict(root="X1puy/modules"))
        clients.append(client1)
    if STRING_SESSION2:
        print("Client2: Found.. Starting.. 📳")
        client2 = Client(name="two", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION2, plugins=dict(root="X1puy/modules"))
        clients.append(client2)
    if STRING_SESSION3:
        print("Client3: Found.. Starting.. 📳")
        client3 = Client(name="three", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION3, plugins=dict(root="X1puy/modules"))
        clients.append(client3)
    if STRING_SESSION4:
        print("Client4: Found.. Starting.. 📳")
        client4 = Client(name="four", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION4, plugins=dict(root="X1puy/modules"))
        clients.append(client4)
    if STRING_SESSION5:
        print("Client5: Found.. Starting.. 📳")
        client5 = Client(name="five", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION5, plugins=dict(root="X1puy/modules"))
        clients.append(client5)
    if STRING_SESSION6:
        print("Client6: Found.. Starting.. 📳")
        client6 = Client(name="six", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION6, plugins=dict(root="X1puy/modules"))
        clients.append(client6)
    if STRING_SESSION7:
        print("Client7: Found.. Starting.. 📳")
        client7 = Client(name="seven", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION7, plugins=dict(root="X1puy/modules"))
        clients.append(client7)
    if STRING_SESSION8:
        print("Client8: Found.. Starting.. 📳")
        client8 = Client(name="eight", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION8, plugins=dict(root="X1puy/modules"))
        clients.append(client8)
    if STRING_SESSION9:
        print("Client9: Found.. Starting.. 📳")
        client9 = Client(name="nine", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION9, plugins=dict(root="X1puy/modules"))
        clients.append(client9)
    if STRING_SESSION10:
        print("Client10: Found.. Starting.. 📳")
        client10 = Client(name="ten", api_id=api_id, api_hash=api_hash, session_string=STRING_SESSION10, plugins=dict(root="X1puy/modules"))
        clients.append(client10)

    # Jalankan bot jika ada
    if bot_app is not None:
        await bot_app.start()
        print("Bot is running...")

    # Mulai setiap client session (jika ada)
    for client in clients:
        await client.start()
        print(f"{client.name} started.")

    # Biasanya, Anda mungkin ingin menunggu sampai aplikasi dihentikan secara manual.
    # Misalnya dengan method idle() dari Pyrogram untuk bot:
    if bot_app is not None:
        await bot_app.idle()
    else:
        # Jika hanya client, biarkan aplikasi berjalan (Anda bisa menambahkan mekanisme penghentian sendiri)
        while True:
            await asyncio.sleep(1)

    # Setelah aplikasi selesai, pastikan untuk menutup sesi aiohttp
    await aiosession.close()

# Jalankan main() dengan event loop
if name == 'main':
    asyncio.run(main())
