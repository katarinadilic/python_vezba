# # kurs = "Python Fundamentals"
# # print(kurs)

# # a = 10
# # b = 3
# # rezultat_sabiranja=a+b
# # print("Sabiranje:",rezultat_sabiranja)
# # print("Oduzimanje:",a-b)
# # print("Mnozenje:",a*b)
# # print("Deljenje:",int(a/b))

# # stepen=a**3
# # print(stepen)
# # print(a//b)
# # print(a%b)

# godine = 25
# #godine+1

# godine=godine+1

# godine+=2
# godine-=10
# godine/=2
# godine//=2


# print(int(godine))


# broj1=15
# broj2=20

# print("Zbir:",broj1+broj2)

# broj1=int(input("Unesite prvi broj: "))

# broj2=int(input("Unesite drugi broj: "))


# print("Zbir:",broj1+broj2)

# #poluprecnik=float(input("Unesite poluprecnik kruga: "))
# pi=3.14
# povrsina_kruga=poluprecnik**2*pi

# print("Povrsina kruga je: %.3f" %povrsina_kruga)

# unos=input("Unesi nesto...")

# print(unos.isnumeric())

# username="katarina"
# password="Katarina1109"

# korisnicko_ime=input("Unesite korisnicko ime: ")
# lozinka=input("Unesite lozinku: ")

# print("Korisnicko ime ispravno: " ,username==korisnicko_ime)
# print("Lozinka ispravna: ", password==lozinka)

# godine=20
# print(godine >= 16)

# broj=int(input("Unesite broj: "))

# ostatak=broj%2

# print("Paran broj? ",ostatak==0)

# import random
# korisnik=int(input("Unesite broj: "))
# racunar=random.randint(1,10)

# pogodjen_broj=korisnik==racunar

# print("Pogodili ste broj: ",pogodjen_broj," Racunar je izabrao: ", racunar)

# automobil=0
# cilj=50

# print(automobil>=cilj)
# automobil+=10
# print(automobil>=cilj)
# automobil+=10
# print(automobil>=cilj)
# automobil+=10
# print(automobil>=cilj)
# automobil+=10
# print(automobil>=cilj)
# automobil+=10
# print(automobil>=cilj)

# provera_imena=True #ime==sacuvano_ime
# provera_lozinke=False #lozinka==sacuvana_lozinka

# print(provera_imena or provera_lozinke)

smer="python"
godina=2022

unos_smera=input("Unesi kurs:")
unos_godine=int(input("Unesi godinu:"))

provera_kurs=smer==unos_smera
provera_godine=godina==unos_godine

print("Odobreno:",provera_kurs and provera_godine)
