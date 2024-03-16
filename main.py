import os

def menyval():
    meny_alternativ = (0, 1, 2)

    while True:
        print("[1] Option 1")
        print("[2] Option 2")
        print("[0] Exit")

        print()
        användare_input = int(input("Välj ett alternativ: "))

        if användare_input in meny_alternativ:
            return användare_input
        else:
            os.system('clear')
            print("Ogiltigt val")
            print()



while True:
    användare_input = menyval()
    if användare_input == 1:
        os.system('clear')
        print("Val 1")
        print()
    elif användare_input == 2:
        os.system('clear')
        print("Val 2")
        print()
    elif användare_input == 0:
        os.system('clear')
        print("Avslutar programmet")
        exit()




















