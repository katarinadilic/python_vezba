# sekunde=10

# while sekunde>0:

#     if sekunde>0:
#         print(sekunde)

#     sekunde -=1

for x in range(10):
    for y in range(10):
        if y>=x:
            print("*", end="")
        else:
            print(" ", end="")
    print()

