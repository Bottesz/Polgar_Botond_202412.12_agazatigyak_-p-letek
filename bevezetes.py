def elso_feladat():
    print("I/A: ")
    jatekos_neve:str = str(input("Játékos neve: "))
    szerepkor:str = str(input("szerepkör: "))
    
    print("I/B: ")
    if szerepkor == "varázsló":
        print(f"Üdvözlünk {jatekos_neve} 2 életed van!")
    elif szerepkor == "harcos":
        print(f"Üdvözlünk {jatekos_neve} 10 életed van!")
    else:
        print(f"Üdvözlünk {jatekos_neve} 8 életerőd van!")
        
