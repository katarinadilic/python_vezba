# brojevi=[9,1,6,2,5,19,34,22]

# # brojevi.sort()
# # brojevi.reverse()

# # print(brojevi)

# # sortirani_brojevi = [9,1,6,2,5,19,34,22]

# while True:
#     izvrsena_zamena=False
#     for i in range(1, len(brojevi)):
#         if brojevi[i]<brojevi[i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsena_zamena=True
#     if izvrsena_zamena==False:
#         break

# print(brojevi)

# product=["Phone", "Tv", "Computer"]
# price=[155.95, 180.35, 199.9]

# for i in range(len(product)):
#     print(product[i], price[i])

automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peugeot"]

for i in range(len(automobili)):
    print("Automobil:", automobili[i], end=" ")
    if i==3:
        print("Aleksandra vozi automobil:",automobili[i],end="")
    print()