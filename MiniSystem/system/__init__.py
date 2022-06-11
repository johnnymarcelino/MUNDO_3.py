# def lists():
'''from MiniSystem.system import *
from MiniSystem.arquivo import *
people = {"Johnny Gabriel": 26, "Jorge Marcelino": 30, "Maria de Fatima": 67, "Clelia Pereira": 61, "Almir Aguiar": 34,
          "Cleiton Aguiar": 36, "Jéssica Lira": 29, "Lucas Cauan": 9, "Daniel Caique": 8}
    # return people
#  "Marcelo da Costa": 35
arq = "FileSystem.txt"



def menu(msg = "PRINCIPAL MENU"):
    a = "=" * 50
    # msg = "MENU PRINCIPAL"
    # c = a.count("=")  # conta quantas vezes aparece sinal '='
    print(a)
    # c = c / 2
    # d = c // 1.5
    # d = int(d)
    # print(' ' * (d), f'{msg.center()}', ' ' * (d))
    print(f'{msg.center(50)}')
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
        except:
                print("=" * 50)
                print("\033[0;31mERROR!\033[m")
                print("\033[0;34mType only:\033[m")
                continue
        else:
            if(choice > 3 or choice < 0):
                while(choice > 3 or choice < 0):
                    print("=" * 50)
                    print("\033[0;31mERROR!\033[m")
                    print("\033[0;34mType only:\n1 - See people's list\n2 - Registry new person or\n3 - Quit of the system\033[m")
                    choice = int(input("Your option: "))
                break
        if (choice == 1):
            readFile(arq)
            break
        elif (choice == 2):
            newReg("NEW REGISTRY")
        else:
            if(choice == 3):
                from time import sleep
                sleep(2)
                print("Logging out of the System so far!")
                break
            break
        break


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
    a = open(arq, "at")
    a.write(f"{name};{age}\n")
    # arq[name] = age
    print(f"New registry noted of {name} added")
    a.close()
    menu("PRINCIPAL MENU")


def filExist(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def creatFile(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("There is some problem with the create the file")
    else:
        print(f"File {nome}, created with success!")
    readFile(arq)


def readFile(name):
    try:
        a = open(name, "rt")
    except:
        print("There is a problem with the program")
    else:
        # menu("List of People")
        print("List of People")
        for linhas in a:
            dado = linhas.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
        print(a.read())
    finally:
        option()
'''