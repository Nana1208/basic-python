# x adalah nilai syarat kelulusan 
x=float(input("Standar nilai kelulusan: "))

# a adalah hasil ujian teori
a=float(input("Nilai ujian teori: "))

# b adalah ujian praktek
b=float(input("Nilai ujian praktek: "))


if a >= x and b >= x:
    print("Selamat, anda lulus!")

if a >= x and b < x:
    print("Anda harus mengulang ujian praktek.")

if b >= x and a<x:
    print("Anda harus mengulang ujian teori")

if a < x and b < x:
    print("Anda harus mengulang ujian teori dan praktek")
