# x adalah nilai syarat kelulusan 
x=70

# a adalah hasil ujian teori
a=90

# b adalah ujian praktek
b=40


if a >= x and b >= x:
    print("Selamat, anda lulus!")

if a >= x and b < x:
    print("Anda harus mengulang ujian praktek.")

if b >= x and a<x:
    print("Anda harus mengulang ujian teori")

if a < x and b < x:
    print("Anda harus mengulang ujian teori dan praktek")
