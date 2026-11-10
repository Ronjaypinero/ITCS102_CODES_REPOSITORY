num = 0
come = True 

while come == True:
    n=int(input('input a number:'))

    if n == 0:
        print("LOOP TERMINATED")
        print("TOTAL OF ALL NUMBERS IS ",num)
        break
    else:
        print("LOOP CONTINUE")
        num+=n
        print("CURRENT TOTAL IS", num)
        continue