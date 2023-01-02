brojevi=[9,1,6,2,5,19,34,22]

# brojevi.sort()
# brojevi.reverse()

# print(brojevi)

# sortirani_brojevi = [9,1,6,2,5,19,34,22]

while True:
    izvrsena_zamena=False
    for i in range(len(brojevi)):
        if brojevi[i]<brojevi[i-1]:
            privremena=brojevi[i]
            brojevi[i]=brojevi[i-1]
            brojevi[i-1]=privremena
            izvrsena_zamena=True
    if izvrsena_zamena==False:
        break
    
print(brojevi)