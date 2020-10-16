def Menu():
    kontak1= {
        "nama":"Nana",
        "telepon": 1406543100
    }

    kontak2= {
        "nama":"Zidan",
        "telepon": 1606828021
    }

    daftar_kontak=[]
    daftar_kontak.append(kontak1)
    daftar_kontak.append(kontak2)
    repeater = "y"
    while (repeater=="y"):
        print("Selamat Datang!")
        print("""
                ---Menu---
            
            1.Daftar Kontak
            2.Tambah Kontak
            3.Keluar
            """)
        
        pilihan=int(input("Pilihan menu: "))

        if pilihan==1:
            print("Daftar kontak:")
            for kontak in daftar_kontak:
                print ("Nama: {}". format (kontak["nama"]))
                print ("No Telepon: {}". format (kontak["telepon"]))

        elif pilihan==2:
            count=int(input("Berapa kontak: "))

            for i in range (count):
                print("Kontak ke {}".format(i+1))
                Nama=input("Nama:  ")
                Telepon=int(input("No Telepon: "))
                kontak3= {
                    "nama":Nama, 
                    "telepon": Telepon
                }
                daftar_kontak.append(kontak3)

            print("Kontak berhasil ditambahkan")
            
        elif pilihan==3:
            print("Program selesai, sampai jumpa!")
            return daftar_kontak
        else:
            print("Menu tidak tersedia")
        repeater = input("Apakah anda ingin kembali ke menu?(y/n): ")
    return daftar_kontak

Menu()