sloth=1
size = int(input('SIZE:'))
for c in range(size):
    for r in range(c):
        print(sloth, end=" ")
        sloth +=1
    print()
