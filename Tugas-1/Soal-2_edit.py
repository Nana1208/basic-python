r=float(input("Berapa jari-jari lingkaran? "))
pi=22/7

x=(pi*r**2)

y="Luas lingkaran dengan jari-jari {} cm adalah {} cm².".format(r,x)

print(y)


a="Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm².".format(r,x)

print(a)