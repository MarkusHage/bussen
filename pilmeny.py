import os
from getkey import getkey, keys
from array import *
import random

Alternativ = ["Lägg till passagerare", "Skriv ut array", "Skriv ut sammanlagd ålder på passagerare", "Avsluta"]

Passagerare = array('i',[])
#AntalPassagerare = 0

def LäggTillPassagerare():
    if len(Passagerare) < 25:
        RandomÅlder = random.randint(5,99)
        Passagerare.append(RandomÅlder)
        print(f"En passagerare som är {RandomÅlder} år gammal hoppade på bussen. Totalt {len(Passagerare)} passagerare på bussen.")
    else:
        print("Tyvärr grabbar, inga slots lediga. Bussen är full.")   
        
def SkrivUtArray():
    if len(Passagerare) > 0:
        print(Passagerare[1,-1])
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
                if Menyval < 3:
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
                        SammanlagdÅlder()
                    case 3:
                        os.system('clear')
                        Avsluta()


        if Menyval == 0:
            print(f"{Alternativ[0]} <--")
            print(f"{Alternativ[1]}")
            print(f"{Alternativ[2]}")
            print(f"{Alternativ[3]}")
        elif Menyval == 1:
            print(f"{Alternativ[0]}")
            print(f"{Alternativ[1]} <--")
            print(f"{Alternativ[2]}")
            print(f"{Alternativ[3]}")
        elif Menyval == 2:
            print(f"{Alternativ[0]}")
            print(f"{Alternativ[1]}")
            print(f"{Alternativ[2]} <--")
            print(f"{Alternativ[3]}")
        elif Menyval == 3:
            print(f"{Alternativ[0]}")
            print(f"{Alternativ[1]}")
            print(f"{Alternativ[2]}")
            print(f"{Alternativ[3]} <--")
          
meny()       