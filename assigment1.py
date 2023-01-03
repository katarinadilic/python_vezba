string="3,9,13,4,42"
lista=string.split(",")
konacno_resenje=""
for broj in lista:
    broj=int(broj)**2
    konacno_resenje+=(str(broj))+','
    duzina=len(konacno_resenje)
print(duzina)
print("Konacno resenje je:",konacno_resenje[0:duzina-1])


print("Hello World"[::2])