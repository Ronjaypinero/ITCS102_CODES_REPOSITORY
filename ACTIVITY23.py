gachiakuta=[]
vinland=[]
onepiece=[]
jujutsu_kaisen=[]
tokyo_ghoul=[]
black_clover=[]
naruto=[]
attack_on_titan=[]

while True:
    ans = input("Do you read or watch anime?yes/no").lower()
    if ans=="yes":
        print("What anime do you like the most in this list?")
        print("1. gachiakuta \n2 vinland \n3 onepiece \n4 jujutsu_kaisen \n5 tokyo_ghoul \n6 black_clover \n7 naruto \n8 attack_on_titan")
    else:
        break
        choice= int(input("Input--> "))

        if choice ==1:
            print("GACHIAKUTA")
            character= input("Who's your favorite character?")
            gachiakuta.append(character)
            print("ohh you like", gachiakuta)
            con= input("Do you wish to continue?yes/no").lower()
            if con== 'yes':
                continue
            else:
                break
        else:
            prirnt("INVALID CHOICE!!!!")