# def lists():
people = {"Johnny Gabriel": 26, "Jorge Marcelino": 30, "Maria de Fatima": 67, "Clelia Pereira": 61, "Almir Aguiar": 34,
          "Cleiton Aguiar": 36, "Jéssica Lira": 29, "Lucas Cauan": 9, "Daniel Caique": 8}
    # return people
#  "Marcelo da Costa": 35

def menu(msg = "PRINCIPAL MENU"):
    a = "=" * 50
    # msg = "MENU PRINCIPAL"
    c = a.count("=")  # conta quantas vezes aparece sinal '='
    print(a)
    c = c / 2
    d = c // 1.5
    d = int(d)
    print(' ' * (d), f'{msg}', ' ' * (d))
    print(a)
    option()


def newReg(msg):
    a = "=" * 50
    # msg = "MENU PRINCIPAL"
    c = a.count("=")  # conta quantas vezes aparece sinal '='
    # print(a)
    c = c / 2
    d = c // 1.5
    d = int(d)
    print(' ' * (d), f'{msg}', ' ' * (d))
    print(a)
    regPeop()


def option():
    while True:
        try:
            print("\033[0;34m1 - See people's list\033[m")
            print("\033[0;34m2 - Registry new person\033[m")
            print("\033[0;34m3 - Quit of the system\033[m")
            print("=" * 50)
            choice = int(input("Your option: "))
            # if(type(choice) != int(choice)):
            #     while(type(choice) != int(choice)):
            #         choice = int(input("Your option: "))
            # if(choice.isnumeric()):
            #     choice = int(choice)
            # else:
                # while(choice is not choice.isdigit()):
                    # print("=" * 50)
                    # print("\033[0;31mERROR!\033[m")
                    # print(
                    #     "\033[0;34mType only:\n1 - See people's list\n2 - Registry new person or\n3 - Quit of the system\033[m")
                    # choice = input("Your option: ")
            # print("=" * 50)
        except:
            print("=" * 50)
            print("\033[0;31mERROR!\033[m")
            print("\033[0;34mType only:\033[m")
            # print(
            #     "\033[0;34mType only:\n1 - See people's list\n2 - Registry new person or\n3 - Quit of the system\033[m")
            # choice = int(input("Your option: "))
            continue
            # choice = input("Your option: ")
        #     while(choice.isnumeric() != int(choice)):
        #         print("=" * 50)
        #         print("\033[0;31mERROR!\033[m")
        #         print("\033[0;34mType only:\n1 - See people's list\n2 - Registry new person or\n3 - Quit of the system\033[m")
        #         choice = int(input("Your option: "))
        else:
            while(choice > 3 or choice < 0):
                print("=" * 50)
                print("\033[0;31mERROR!\033[m")
                print("\033[0;34mType only:\n1 - See people's list\n2 - Registry new person or\n3 - Quit of the system\033[m")
                choice = int(input("Your option: "))
            print("=" * 50)
            # menu("="*30)
            if (choice == 1):
                seePeop()
            elif (choice == 2):
                newReg("NEW REGISTRY")
            else:
                if(choice == 3):
                    from time import sleep
                    sleep(2)
                    print("Logging out of the System so far!")
    # else:
    #     while (choice > 3 or choice < 0):
    #         print("\033[0;31mERROR!\033[m")
    #         print(
    #             "\033[0;33mType only:\n1 - See people's list\n2 - Registry new person or\n3 - Quit of the system\033[m")
    #         choice = int(input("Your option: "))
    # Error Handling


def seePeop():
    for na, ag in people.items():
        if (len(na) > 14):
            print(na, f'\t\t\t{ag} years old')
        else:
            print(na, f'\t\t\t\t{ag} years old')
    menu("PRINCIPAL MENU")


def regPeop():
    name = str(input("Name: ")).strip()
    while(name.isnumeric() or name == ""):
        print("\033[0;31mERROR!\033[m")
        print("\033[0;32mPlease, enter with only the name of person\033[m")
        name = str(input("Name: ")).strip()
    age = input("Age: ")
    while(age.isnumeric() != True):
        age = input("Age: ")
    people[name] = age
    # for last in people.values():
    #     if(last == name)
    print(f"New registry noted of {name} added")
    menu("PRINCIPAL MENU")

# menu("PRINCIPAL MENU")
# option()