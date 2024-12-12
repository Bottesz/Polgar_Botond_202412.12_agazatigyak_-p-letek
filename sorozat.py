import random



def fej_iras():
    lista_dobasok = []
    i:int = 0
    fejek:int = 0

    for i in range(7):
        lista_dobasok.append(random.randint(0,1))


    for i in range(len(lista_dobasok)):
        if lista_dobasok[i] == 1:
            print("FEJ", end=" ")
        else:
            print("ÍRÁS", end=" ")
        if i < len(lista_dobasok) - 1:
            print("-", end=" ")


    for dobas in lista_dobasok:
        if dobas == 1:
            fejek +=1
    return fejek



def konzolra_kiir(fejek):
    print("\n II/E,F:\n\t Fejek száma: ",fejek) 


def fileba_kiir(fejek):
    fajlom = open("fejek.txt", "w", encoding="UTF-8")
    fajlom.write("II/F\n")
    fajlom.write(f"A fejek száma: {fejek}.")
    fajlom.close()

