import os
from getkey import getkey, keys
import numpy as np
import random

Alternativ = ["Lägg till passagerare", "Skriv ut array", "Skriv ut sammanlagd ålder på passagerare", "Avsluta"]

Passagerare = np.array([])

def LäggTillPassagerare():
    if len(Passagerare) < 25:
        RandomÅlder = random.randint(5,99)
        np.append(Passagerare, RandomÅlder)
        print(f"En passagerare som är {RandomÅlder} år gammal hoppade på bussen. Totalt {len(Passagerare)} på bussen.")
    else:
        print("Tyvärr grabbar, inga slots lediga. Bussen är full.")
    

def SkrivUtArray():
    if len(Passagerare) > 0:
        print(Passagerare)
    else:
        print("Bussen är tom!")

def SammanlagdÅlder():
    if len(Passagerare) > 0:
        print(sum(Passagerare))
    else:
        print("Bussen är tom!")  

def Avsluta():
    print("Avlutar programmet...")
    exit()


def meny():

    Menyval = 0

    while True:
        
        key = getkey()
        
        match key:
            case keys.UP:
                if Menyval > 0:
                    Menyval -= 1
                    os.system('clear')
                else:
                    os.system('clear')
            case keys.DOWN:
                if Menyval < 2:
                    Menyval += 1
                    os.system('clear')
                else:
                    os.system('clear')
            case keys.ENTER:
                match Menyval:
                    case 0:
                        os.system('clear')
                        LäggTillPassagerare()
                    case 1:
                        os.system('clear')
                        SkrivUtArray()
                    case 2:
                        os.system('clear')
                        Avsluta()


        if Menyval == 0:
            print("Första valet <--")
            print("Andra valet")
            print("Avsluta")
        elif Menyval == 1:
            #os.system('clear')
            print("Första valet")
            print("Andra valet <--")
            print("Avsluta")
        elif Menyval == 2:
            #os.system('clear')
            print("Första valet")
            print("Andra valet")
            print("Avsluta <--")
          
meny()       