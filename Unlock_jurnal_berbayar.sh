#!/bin/bash

# Fungsi untuk menampilkan teks berwarna
color_text() {
    echo -e "\033[38;5;$1m$2\033[0m"
}

# Fungsi untuk animasi loading
loading_animation() {
    spin='|/-\'
    while true; do
        for i in `seq 0 3`; do
            echo -ne "\r$(color_text 196 'Sedang memproses') ${spin:$i:1}"
            sleep 0.1
        done
    done
}

# Clear screen
clear

# Menampilkan header dengan warna
color_text 9 "========================================================"
color_text 10 "      LIBRARY JURNAL BERBAYAR DOWNLOAD LINK UNIVERSAL"
color_text 9 "========================================================"
color_text 15 " Powered by Fandy * Script Bash"
color_text 9 "--------------------------------------------------------"
color_text 14 " Masukkan URL jurnal atau DOI untuk mengambil jurnal"
color_text 9 "--------------------------------------------------------"

# Meminta input URL dari user
read -p "$(color_text 33 'Masukkan URL jurnal yang ingin diambil (misalnya dari DOI atau URL jurnal berbayar): ')" url_jurnal

# Validasi input
if [[ -z "$url_jurnal" ]]; then
    color_text 1 "URL tidak boleh kosong! Silakan coba lagi."
    exit 1
fi

# Menjalankan animasi loading di background
loading_animation &

# Menunggu sebentar sebelum melanjutkan
sleep 1

# Stop animasi loading
kill $!

# Memodifikasi URL menjadi format yang sesuai dengan Sci-Hub
url_scihub="https://sci-hub.se/$url_jurnal"

# Menampilkan URL Sci-Hub yang telah dimodifikasi
color_text 10 "Link Sci-Hub untuk jurnal ini adalah:"
color_text 5 "$url_scihub"

# Menggunakan perintah 'xdg-open' untuk membuka link di browser (untuk Termux dengan GUI, atau bisa menggunakan browser lain)
color_text 33 "Membuka link di browser..."
xdg-open $url_scihub

# Akhir script
color_text 2 "Proses selesai! Link dapat diakses melalui browser."

