popularan_proizvod=""
jesen=input("Da li je trenutno godisnje doba jesen?")

if jesen!="da" and jesen!="ne":
    print("Uneli ste pogresnu informaciju")
elif jesen=="da":
    popularan_proizvod="ajvar"
    print(popularan_proizvod)
else:
    popularan_proizvod="jabuka"
    print(popularan_proizvod)


