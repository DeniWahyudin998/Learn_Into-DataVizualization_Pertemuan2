# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:46:15 2022

@author: 081796
"""

HargaBuku = int(input("Masukkan Harga Buku : "))
JumlahBeli = int(input("Masukkan Jumlah Beli Buku : "))
Uang = int(input("Masukkan Jumlah Uang : "))
TotalHarga = HargaBuku * JumlahBeli

if Uang > TotalHarga :
    print("Mendapatkan Membeli Buku", "& Kembalian sebesar", (Uang - TotalHarga))
elif Uang == TotalHarga :
    print("Mendapatkan Membeli Buku", "& Jumlah Uang Sesuai")
elif Uang == HargaBuku :
    print("Hanya Mendapatkan 1 Buku")
else :
    print("Uang Anda Tidak Mencukupi")
    

bobot_absen = int(input("Masukkan Bobot Jumlah Absensi : "))
bobot_tugas = int(input("Masukkan Bobot Nilai Tugas : "))
bobot_uts   = int(input("Masukkan Bobot Nilai UTS : ")) 
bobot_uas   = int(input("Masukkan Bobot Nilai UAS : "))

nilai_absen = int(input("Masukkan Jumlah Absensi : "))
nilai_tugas = int(input("Masukkan Nilai Tugas : "))
nilai_uts   = int(input("Masukkan Nilai UTS : ")) 
nilai_uas   = int(input("Masukkan Nilai UAS : "))
total_nilai = (nilai_absen*0.1) + (nilai_tugas*0.2) + (nilai_uts*0.3) + (nilai_uas*0.4)
print(int(total_nilai))

if total_nilai >= 80 < 100:
    print("Anda Mendapatkan Nilai A")
elif total_nilai >= 70 < 80:
    print("Anda Mendapatkan Nilai B")
elif total_nilai >= 60 < 70:
    print("Anda Mendapatkan Nilai C")
elif total_nilai >= 50 < 60:
    print("Anda Mendapatkan Nilai D")
else:
    print("Anda Mendapatkan Nilai E")