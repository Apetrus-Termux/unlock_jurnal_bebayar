import time
import webbrowser
import sys
import threading

# Fungsi untuk membuat teks berwarna di terminal
def color_text(color_code, text):
    return f"\033[38;5;{color_code}m{text}\033[0m"

# Fungsi animasi loading
def loading_animation():
    spin = ['|', '/', '-', '\\']
    while True:
        for symbol in spin:
            sys.stdout.write(f"\r{color_text(196, 'Sedang memproses')} {color_text(46, symbol)}")
            sys.stdout.flush()
            time.sleep(0.2)

# Tampilan awal
print("\033c")  # Clear screen
print(color_text(9, "========================================================"))
print(color_text(10, "      LIBRARY JURNAL BERBAYAR DOWNLOAD LINK UNIVERSAL"))
print(color_text(9, "========================================================"))
print(color_text(15, " Powered by Fandy * Language Python"))
print(color_text(9, "--------------------------------------------------------"))
print(color_text(14, " Enter keyword to search jurnal or type 'exit' to quit"))
print(color_text(9, "--------------------------------------------------------"))

# Meminta input dari pengguna
keyword = input(color_text(33, "Masukkan link jurnal yang mau di eksekusi: "))

# Validasi input
if keyword.lower() == 'exit':
    print(color_text(1, "Terima kasih telah menggunakan program ini."))
    sys.exit(0)
elif not keyword:
    print(color_text(1, "Kata kunci tidak boleh kosong! Silakan coba lagi."))
    sys.exit(1)

# Menjalankan animasi loading di background
loading_thread = threading.Thread(target=loading_animation)
loading_thread.daemon = True
loading_thread.start()

# Simulasi pencarian data
time.sleep(4)

# Hasil pencarian
print("\033c")  # Clear screen
print(color_text(9, "========================================================"))
print(color_text(10, "                 HASIL PENCARIAN"))
print(color_text(9, "========================================================"))
print(color_text(14, f" Link download untuk kata kunci '{keyword}':"))
print(color_text(5, f"https://example.com/search?q={keyword.replace(' ', '+')}"))
print(color_text(9, "========================================================"))

# Menyediakan opsi untuk membuka link di browser
print(color_text(33, "Membuka link di browser..."))
webbrowser.open(f"https://example.com/search?q={keyword.replace(' ', '+')}")

# Akhir script
print(color_text(2, "Proses selesai! Link dapat diakses melalui browser."))
