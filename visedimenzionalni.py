proizvodi=[
             ["iphone 11","samsung s22","xiaomi x3"],
             ["acer", "macbook","dell"],
             ["ipad", "samsung galaxy tab", "xiaomi tablet"]
           ]

# telefoni=["iphone 11","samsung s22","xiaomi x3"]
# laptopovi=["acer", "macbook","dell"]
# tableti=["ipad", "samsung galaxy tab", "xiaomi tablet"]

# # proizvodi=[telefoni, laptopovi, tableti]

# print(proizvodi[0][1])

# for kategorija in proizvodi:
#     for stavka in kategorija:
#         print(stavka)

for i in range(len(proizvodi)):
    for j in range(len(proizvodi[i])):
        print(proizvodi[i][j])
    
     
