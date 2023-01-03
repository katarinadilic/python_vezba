biblioteka=[]

while True:
    print("Odaberi komendu: 1-unos, 2-prikaz, 3-brisanje, >3-izlaz")
    komanda=int(input("Unesite komandu: "))

    if komanda == 1:
        naslov=input("Unesite naslov: ")
        autor=input("Unesite autora: ")
        isbn=int(input("Unesite isbn: "))
        biblioteka.append([naslov,autor,isbn])
        print("Dodata knjiga")
    if komanda==2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda==3:
        kljucna_rec=input("Unesite naziv knjige:")
        for knjiga in biblioteka:
            for detalj in knjiga:
                if detalj==kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")
    if komanda>3:
        print("Izlaz iz programa")
        break    
