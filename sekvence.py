# osoba=["Sofija",20, "plava", True]
# print(osoba[0])
# print("Godine:", osoba[1])

# automobili=["Opel","Mercede","Ford","Skoda"]
# print(automobili[2])

# for x in range(10):
#     print(x)

# kurs="Python"

# duzina=len(kurs)

# for i in range(duzina):
#     print(kurs[i])

# ime="Katarina Dilic"
# for i in range(len(ime)):
#     print(ime[i])

a=[1,3,2,6,5,33,22,56,45]

parni=[]
neparni=[]

for index in range(len(a)):
    if a[index]%2 == 0:
        parni.append(a[index])
    else:
        neparni.append(a[index])
print("Parni brojevi su: ",parni)
print("Neparni brojevi su: ",neparni)



