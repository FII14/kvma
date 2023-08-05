import subprocess
import os

nama_file_video = input("Masukkan nama file video (format MP4): ")

if not os.path.exists(nama_file_video):
    print(f"Kesalahan: File video '{nama_file_video}' tidak ditemukan.")
    sys.exit(1)

nama_file_audio = input("Masukkan nama file audio (format MP3): ")

if os.path.exists(nama_file_audio):
    pilihan = input("File audio '{nama_file_audio}' sudah ada. Apakah Anda ingin menimpa file yang ada? (iya/tidak): ")
    
    if pilihan.lower() != 'iya':
        print("Konversi dibatalkan.")
        exit()

try:
    subprocess.run(['ffmpeg', '-i', nama_file_video, '-vn', '-acodec', 'libmp3lame', '-q:a', '4', nama_file_audio])
    print(f"Konversi selesai: {nama_file_video} menjadi {nama_file_audio}")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
