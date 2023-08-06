#!/usr/bin/env python3

import subprocess
import os
import sys

print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Program : Konversi Video Menjadi Audio  @
@ Pembuat : Rofi [FII14]                  @
@ GitHub  : https://github.com/FII14/KVMA @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")

nama_file_video = input("Masukkan nama file video (format MP4): ")

if not os.path.exists(nama_file_video):
    print(f"Kesalahan: File video '{nama_file_video}' tidak ditemukan.\n")
    sys.exit(1)

nama_file_audio = input("Masukkan nama file audio (format MP3): ")

if os.path.exists(nama_file_audio):
    pilihan = input(f"File audio '{nama_file_audio}' sudah ada. Apakah Anda ingin menimpa file yang ada? (iya/tidak): ")
    
    if pilihan.lower() != 'iya':
        print("Konversi dibatalkan.\n")
        sys.exit(1)

try:
    print("\n[*] Sedang melakukan konversi.")
    devnull = open(os.devnull, 'w')
    subprocess.run(['ffmpeg', '-i', nama_file_video, '-vn', '-acodec', 'libmp3lame', '-q:a', '4', nama_file_audio], stdout=devnull, stderr=devnull)
    devnull.close()
    print(f"[*] Konversi selesai.")
    
    folder_hasil = "hasil"
    
    if not os.path.exists(folder_hasil):
        os.makedirs(folder_hasil)
    
    os.rename(nama_file_audio, os.path.join(folder_hasil, nama_file_audio))
    
    print(f"[*] Hasil konversi disimpan dalam folder '{folder_hasil}'.\n")
    sys.exit(0)
    
except Exception as e:
    print(f"Terjadi kesalahan: {e}\n")
    sys.exit(1)
