a=10
b=10

if True:
    # do something, blok kayak ini berarti ini di dalamnya if
    print("True")

if a > b:
    print("True")
    print("True -- 2")

if a> b:
    print("a lebih besar dari b")

elif a==b:
    print("a sama dengan b")


else:
    print("a lebih kecil dari b")

# Kondisi di atas berlaku hanya jika diakomodasi. Bila tidak ada kondisi yang sesuai maka tidak akan keluar hasilnya.

print (True and True)
print (True and False)
print(True or False)
print(not False)
print(not True)
