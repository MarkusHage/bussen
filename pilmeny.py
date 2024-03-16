import os
from getkey import getkey, keys


def meny():
    
    Menyval = 0
    
    print("Första valet <--")
    print("Andra valet")
    print("Avsluta")
    print()
    print("Välj alternativ med piltangenterna")
    

    while True:
        key = getkey()

        if key == keys.UP and Menyval > 0:
            Menyval -= 1
        elif key == keys.DOWN and Menyval < 2:
            Menyval += 1
        elif key == keys.ENTER:
            if Menyval == 0:
                print("Första valet")
                #Första valet
            elif Menyval == 1:
                print("Andra valet")
                #Andra valet
            else:
                exit()
                #Avsluta
        else:
            buffer += key
            print(buffer)

        if Menyval == 0:
            print("Första valet <--")
            print("Andra valet")
            print("Avsluta")
        elif Menyval == 1:
            print("Första valet")
            print("Andra valet <--")
            print("Avsluta")
        elif Menyval == 2:
            print("Första valet")
            print("Andra valet")
            print("Avsluta <--")

          
meny()       

"""
if användare_input in meny_alternativ:
    return användare_input
else:
    os.system('clear')
    print("Ogiltigt val")
    print()
"""