# for sledeci in ["Marija", "Katarina", "Vladimir", "Petar"]:
#     print("Zdravo", sledeci)

# print("Zdravo svima!!!")

# for broj in range(5):
#     print(broj)

# start_date=2010
# end_date=2023

# for date in range(start_date,end_date+1):
#     print("Dozvoljen godina je:",date)

# print("Ovo je kurs \"Python\" ")

# print("1\t2\t3\t4\t5")
# print("**********************************")

# for brojac in range(1,6):
#     for brojac2 in range(1,6):
#         print(brojac*brojac2, end=("\t"))
#     print("\n")

# for i in range(5):
#     for j in range(5):
#         print("#", end=" ")
#     print("\n")

# for i in range(5):
#     if (i==0 or i==4):
#         for y in range(6):
#             print("*", end=" ")
#         print()
#     else:
#         for y in range(6):
#             if (y==0 or y==5):
#                 print("*",end=" ")
#             else:
#                 print(" ", end=" ")
#         print()

for i in range(10):
    for j in range(10):
        if i==0 or i==9 or j==0 or j==9:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()







