import random

izbor_racunara=random.randint(1,100)
izbor_korisnika=int(input("Unesite broj od 1 o 100:"))

if(izbor_korisnika>100 or izbor_korisnika<0):
    print("Uneli ste broj koji nije dozvoljen")
elif izbor_racunara>izbor_korisnika:
    print("Racunar je pobedio brojem",izbor_racunara)  
elif izbor_racunara<izbor_korisnika:
    print("Pobedili ste, racunar je odabrao broj",izbor_racunara)
else:
    print("Rezultat je neresen, i racunar je izabrao broj", izbor_racunara)


