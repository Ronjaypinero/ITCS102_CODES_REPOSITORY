size = int(input('size:'))
for r in range(size):
    for x in range(size):
        if r==0 or r==size - 1 \
        or x==0 or x==size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()