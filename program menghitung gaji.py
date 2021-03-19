import os

print("PROGRAM MENGHITUNG GAJI KARYAWAN")
print("="*32)
nama = input("masukkan nama : ")
nip = int(input("masukkan NIP karyawan : "))
gol = input("masukkan golongan : ")
jml = int(input("masukkan jumlah anak : "))
anak = jml * 200000
potBPJS = 0.02
if gol == "A" or "a":
    gaji = 2000000
elif gol == "B" or "b":
    gaji = 3000000
elif gol == "C" or "c":
    gaji = 4000000
elif gol == "D" or "d":
    gaji = 5000000
hasil = round(gaji - (gaji + anak) * potBPJS)

os.system("cls")

print("="*20,"STRUK GAJI","="*20)
print("Nama         :",nama)
print("NIP          :",nip)
print("Golongan     :",gol)
print("Gaji Kotor   :",gaji)
print("Gaji Bersih  :",hasil)




