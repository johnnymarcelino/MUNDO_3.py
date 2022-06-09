# AULA 14

'''for b in range(1, 10+1):
    # print("I'm in {}".format(b))
    c = float(input("Enter with a number: "))
print("FIM")'''


# print()

'''a = 1
while(a != 10+1):
    print("I'm in {}".format(a))
    a = float(input("Enter with a number: "))
    a += 1
print("FIM!")'''

'''r = "S"
while(r == "S"):
    a = int(input("Enter with a number: "))
    r = str(input("Do you want continue, [S/N] ? ")).upper()
print("FIM")'''

'''n = 1
even = odd = 0
while(n != 0):
    n = int(input("Enter with a number: "))
    if(n != 0):
        if(n % 2 == 0):
            # n += 1
            even += 1
        else:
            odd += 1
print("The amount of even numbers were {}, and the amount of odd numbers were {}!".format(even, odd))'''


# CHALLENGE 57

# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''system = str(input("What is your sex ?\nType 'M' for male or 'F' for female: ")).upper()[0]
if(system == "M"):
    m = "Male"
    print("Your sex is {}!".format(m))
else:
    if(system == "F"):
        f = "Female"
        print("Your sex is {}!".format(f))
while(system != "F" and system != "M"):
    system = str(input("What is your sex ?\nType 'M' for male or 'F' for female: ")).upper()[0]
    if(system == "M"):
        m = "Male"
        print("Your sex is {}!".format(m))
    else:
        f = "Female"
        print("Your sex is {}!".format(f))'''


# CHALLENGE 58

# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

'''machine = randint(0, 10)
# print(machine)
user = int(input("Choose a number between 0 and 10: "))
attempts = 1
if(machine == user):
    print("VERY GOOD!!\nYou're amazing, you guessed up the number!")
    print("The number have chosen by you was {}!".format(user))
    print("The number have chosen by the machine was {}!".format(machine))
    print("You needed just {} attempts to guessed up".format(attempts))
else:
    print("TRY AGAIN!!\nYou not guessed up the number")
    print("The number have chosen by the machine was {}!".format(machine))
    print("The number have chosen by you was {}!".format(user))
    attempts += 1
while(user != machine):
    user = int(input("Choose a number between 0 and 10: "))
    machine = randint(0, 10)
    if (machine == user):
        print("VERY GOOD!!\nYou're amazing, you guessed up the number!")
        print("The number have chosen by you was {}!".format(user))
        print("The number have chosen by the machine was {}!".format(machine))
        attempts += 1
        print("You needed just {} attempts to guessed up".format(attempts))
    else:
        print("TRY AGAIN!!\nYou not have guessed up the number")
        print("The number have chosen by the machine was {}!".format(machine))
        print("The number have chosen by you was {}!".format(user))
        attempts += 1'''

# ////////////////////////////////////////////////////////

'''machine = randint(0, 10)
print(machine)
print("Try any number!")
hit = False
while(hit == False):
    user = int(input("number ? "))
    if(user == machine):
        hit = True
print("Congrats!")'''

# Coding: UTF-8
# CHALLENGE 59

# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior
# [ 4 ] novos números [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

# val1 = int(input("Enter with the first value: "))
# val2 = int(input("Enter with the second value: "))
# menu = int(input("Choose:\n[ 1 ] to sum\n[ 2 ] to multiply\n[ 3 ] to show the greatest number\n[ 4 ] to new numbers or\n[ 5 ] to exit the program\n"))

'''menu = 0
while(menu != 5):
    val1 = int(input("Enter with the first value: "))
    val2 = int(input("Enter with the second value: "))
    menu = int(input("Choose:\n[ 1 ] to sum\n[ 2 ] to multiply\n[ 3 ] to show the greatest number\n[ 4 ] to new numbers or\n[ 5 ] to exit the program\n"))
    if(menu == 1):
        sum = val1 + val2
        print("The sum between {} and {} is {}".format(val1, val2, sum))
    if(menu == 2):
        mult = val1 * val2
        print("The multiplication between {} and {} is {}".format(val1, val2, mult))
    if(menu == 3):
        if(val1 > val2):
            print("The greatest number between {} and {} was {}".format(val1, val2, val1))
        elif(val1 < val2):
            print("The greatest number between {} and {} was {}".format(val1, val2, val2))
        else:
            print("There are not the greatest number between {} and {}, cause they are the same {}".format(val1, val2, val2))
    if(menu == 4):
        # while(menu == 4):
        val1 = int(input("Enter with the first value: "))
        val2 = int(input("Enter with the second value: "))
        menu = int(input("Choose:\n[ 1 ] to sum\n[ 2 ] to multiply\n[ 3 ] to show the greatest number or\n[ 4 ] to new numbers\n[ 5 ] to exit the program\n"))
        if (menu == 1):
            sum = val1 + val2
            print("The sum between {} and {} is {}".format(val1, val2, sum))
        if (menu == 2):
            mult = val1 * val2
            print("The multiplication between {} and {} is {}".format(val1, val2, mult))
        if (menu == 3):
            if (val1 > val2):
                print("The greatest number between {} and {} was {}".format(val1, val2, val1))
            elif (val1 < val2):
                print("The greatest number between {} and {} was {}".format(val1, val2, val2))
            else:
                print("There are not the greatest number between {} and {}, cause they are the same {}".format(val1, val2, val2))
    if(menu <= 0 or menu > 5):
        print("Entered not accepted!")
        menu = int(input("Choose:\n[ 1 ] to sum\n[ 2 ] to multiply\n[ 3 ] to show the greatest number\n[ 4 ] to new numbers or\n[ 5 ] to exit the program\n"))
if(menu == 5):
    print("You have opted to exit from the program!")'''

# CHALLENGE 60

# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# a = int(input("Enter with any number: "))
# b = 1
'''if(a < 0):
    print("there are not factorial for negative numbers!")
else:'''
# for d in range(a, 0, -1):
#     print(d, end=" x ")
#     b = b * (d-1) + b
# print("=", b)
# print("\nFactorial of {} is {}".format(a, b))

# /////////////////////////////////////////////////
'''# print("This is", torial)
result = torial * (torial - 1)
print(torial)
resul = torial + torial
resulFinal = resul + resul
print(resul)
# print(torial)
print("The factorial of {} is {}".format(facto, resulFinal))
# resul = torial
# print(resul)'''

# //////////////////////////////////////////////////////////

'''facto1 = int(input("Enter with any number: "))
facto = facto1
total = 1
# result = 0
# if(facto >= 0):
print("Calculating {}!.... {}!".format(facto, facto), end=" x ")
while(facto > 0):
    # total = total * (facto)
    total *= facto
    facto = facto -1
    print("{}!".format(facto), end="")
    if(facto > 0):
        print(" x ", end=" ")
    else:
        print(" = ", end=" ")
print(total)
print("Factorial of {}! is {}".format(facto1, total))'''

# ////////////////////////////////////////////
# result = facto * (facto - 1)
# print("The result is {}".format(result))
# else:
#     result = facto * (facto) + 1
# facto = facto -1
# total = result * (facto) + total
# print("The facto is {}".format(facto))
# facto = facto -1
# print(result)

# CHALLENGE 61

# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''term = int(input("Enter with the first term: "))
r = int(input("Enter with the reason: "))
a = term
b = 1
# while(b <= 10):
while(term <= a + (9*r)):
    print(term, end=" ")
    term = term + r
    b += 1
print("END")'''

# /////////////////////////////////////////////////////////

'''for pa in range(term, term + (r*10), r):
    print(pa)

else:
    if(r % 2 == 1):
        while(term <= (10 * r)):
            print(term, end=" ")
            term = term + r'''

'''for pa in range(term, term + (r*10), r):
    print(pa)'''

'''term = int(input("Enter with the first term: "))
r = int(input("Enter with the reason: "))
# a = 10
b = 0
# print(term)
# if(r % 2 == 0):
while(term < (term + (r * 10)+1)):
        term = term + r + term
        print(term, end=" ")
# else:
while(term < (10 * r)+1):
    print(term, end=" ")
    term = term + r'''

# CHALLENGE 62

# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

'''term = int(input("Enter with the first term: "))
r = int(input("Enter with the reason: "))
a = term
b = 0
while(term <= a + (9 * r)):
    print(term, end=" ")
    term = term + r
print()
# print("Would you like to show off more terms ?")
# c = str(input("Enter 'Y' for yes and 'N' for no\nOtherwise, type '0' for exit from program: ")).strip().upper()
# term = int(input("Enter with the amount of term to show up or with '0' to exit from program: "))
# term = c
# r1 = r
c = int(input("Enter with the amount of term to show up or with '0' to exit from program: "))
while(c > 0):
    print("\nWould you like to show off more terms ?")
    c = int(input("Enter with the amount of term to show up or with '0' to exit from program: "))
    while(c <= a + (9 * r)):
        print(c, end=" ")
        c = c + r
    else:
        if(c == 0):
            print("You prefer to exit from the program!")
else:
    if(c == 0):
        print("You have chosen to exit from the program!")'''

# tests

'''a = int(input("enter number: "))
while(a > 0):
    a = int(input("enter number: "))
    print("ola", a + a)'''

# //////////////////////////////////

# On works

'''term = int(input("Enter with the first term: "))
r = int(input("Enter with the reason: "))
a = term
count = 0
while(term <= a + (9 * r)):
    print(term, end=" ")
    term = term + r
    count += 1
print("PAUSE")
z = term
count1 = count
# c = int(input("Enter with the amount of term to show up or with '0' to exit from program: "))
while(term != 0):
    print("\nWould you like to show off more terms ?")
    term = int(input("Enter with the amount of term to show up or with '0' to exit from program: "))
    a = term
    while(term <= a-1 + (a * r)):
        print(z, end=" ")
        term = term + r
        z = z + r
        count1 += 1
    if(term > 0):
        print("PAUSE")
    elif(term < 0 ):
        print("TYPING INVALID!!!")
else:
    if(term == 0):
        print("You have chosen to exit from the program!")
        print("Progression have finished with {} term show off!".format(count1))'''

# CHALLENGE 63

# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

# REFAZER COM N TERMOS REQUISITADOS

'''print("="*30)
print("SEQUENCE OF FIBONACCI!!")
print("="*30)

n = int(input("Enter with any number to initiate the count: "))
c = int(input("How many terms would you like to show ? "))
a = n
b = n
# d = 0
# e = 1
if(n == 0):
    print(n, end=" -> ")
    n = 1
    a = n
    b = n
    while(n <= c*c):
        print(n, "->", b, end=" -> ")
        n = n + b
        b = n + b
else:
    while(n <= c*c*c):
        print(n, "->", b, end=" -> ")
        n = n + b
        b = n + b'''

# CHALLENGE 64

# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

'''a = int(input("Type any number [999 TO STOP]: "))
b = 0
c = 1
while(a != 999):
    b += a
    c = a - a + c + 1
    a = int(input("Type any number [999 TO STOP]: "))
print("The sum of numbers typing was {}!".format(b))
print("The total of numbers entered were {}!".format(c-1))'''


# CHALLENGE 65

# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

'''b = str("Y").upper().strip()
c = 0
d = 0
e = 0
f = 0
while(b == "Y" or b != "N"):
    a = int(input("Enter any number: "))
    c = a + c
    d = 1 + d
    if(a > e):
        e = a
        f = a
    else:
        if(a < f):
            f = a
    b = str(input("Do you want continue?\nType 'Y' for Yes or 'N' for No: ")).upper().strip()[0]
print("The media between the numbers typing is {:.2f}!".format(c/d))
print("The greater number entered was {} and the lower was {}!".format(e, f))
print("The amount of numbers entered was {}!".format(d))'''

# //////////////////////////////////////////////////////

'''resp = 's'
média = soma = quant = maior = menor = 0
while(resp in 'Ss'):
    núm = int(input("Digite um número: "))
    soma += núm
    quant += 1
    if(quant == 1):
        maior = menor = núm
    else:
        if(núm > maior):
            maior = núm
        if(núm < menor):
            menor = núm
    resp = str(input("Quer continuar ? [ S / N ]")).upper().strip()[0]
média = soma / quant
print("você digitou {} números e a média foi {}".format(quant, média))
print("o maior valor foi {} e o menor foi {}".format(maior, menor))'''

# AULA 15

'''count = 1
while True:
    print(count, "->", end=" ")
    count += 1
print("ACABOU!")'''

'''n = s = 0
while(n != 999):
    n = int(input("Type a number: "))
    if(n == 999):
        break
    s += n
print("The value of the sum is {}".format(s))'''

# f' STRINGS

'''system = "Johnny"
age = 26
salary = 987.35
# print(f"The system of him is {system} and his is {age}")
print(f"The {system:->20} is {age} and make R$ {salary:.2f} for month!")'''

# CHALLENGE 66

'''s = count = 0
# while(n != 999):
while True:
    n = int(input("Type a number [999 to stop]: "))
    # print(n)
    if(n == 999):
        break
    s += n
    count += 1
print(f"The sum of number typing is {s} and the amount is {count}")'''

# CHALLENGE 67

# multiply = float(input("Would you like to do which multiplication table: "))
# multiply = 0
# while(multiply >= 0):
'''while True:
    # print("--"*30)
    multiply = float(input("Would you like to do which multiplication table: "))
    if(multiply < 0):
        break
    print("--"*30)
    numer = 1
    while(numer <= 10):
        total = multiply * numer
        print(f"{multiply:.0f} * {numer} = {total:.0f}")
        numer += 1
    print("--"*30)
print("--"*30)
print("Multiplication table finished")'''

# CHALLENGE 68

'''from random import randint

print("Let's play Even or Odd!")
player = int(input("Choose a number: "))
machine = randint(0, 10)
# print(machine)
evenOrodd = str(input("Even or Odd ?\nType 'E' for EVEN or 'O' for ODD: ")).upper()
gain = 0
keep = 1
# print("Enter with just 'E' (even) or 'O' (odd)!\nTry again!")
if(evenOrodd[0] == "E"):
    if(machine % 2 == 1 and player % 2 == 1 or machine % 2 == 0 and player % 2 == 0):
        print("You have gained!")
        print(f"The machine choose {machine}")
        gain += 1
    else:
        if(machine % 2 == 0 and player % 2 == 1 or machine % 2 == 1 and player % 2 == 0):
            print("GAME OVER!")
            print(f"The machine choose {machine}")
            keep = 0
elif(evenOrodd[0] == "O"):
    if(machine % 2 == 0 and player % 2 == 1 or machine % 2 == 1 and player % 2 == 0):
        print("You have gained!")
        print(f"The machine choose {machine}")
        gain += 1
    else:
        if (machine % 2 == 0 and player % 2 == 0 or machine % 2 == 1 and player % 2 == 1):
            print("GAME OVER!")
            print(f"The machine choose {machine}")
            keep = 0
elif(evenOrodd != "E" or evenOrodd != "O"):
    while(evenOrodd != "E" or evenOrodd != "O"):
        print("Enter with just the letter 'E' or 'O' to play")
        player = int(input("Choose a number: "))
        evenOrodd = str(input("Even or Odd ?\nType 'E' for EVEN or 'O' for ODD: ")).upper()
        machine = randint(0, 10)
        if (evenOrodd[0] == "E"):
            if (machine % 2 == 1 and player % 2 == 1 or machine % 2 == 0 and player % 2 == 0):
                print("You have gained!")
                print(f"The machine choose {machine}")
                gain += 1
            else:
                if (machine % 2 == 0 and player % 2 == 1 or machine % 2 == 1 and player % 2 == 0):
                    print("GAME OVER!")
                    print(f"The machine choose {machine}")
                    keep = 0
        elif (evenOrodd[0] == "O"):
            if (machine % 2 == 0 and player % 2 == 1 or machine % 2 == 1 and player % 2 == 0):
                print("You have gained!")
                print(f"The machine choose {machine}")
                gain += 1
            else:
                if (machine % 2 == 0 and player % 2 == 0 or machine % 2 == 1 and player % 2 == 1):
                    print("GAME OVER!")
                    print(f"The machine choose {machine}")
                    keep = 0
while(keep != 0):
    player = int(input("Choose a number: "))
    machine = randint(0, 10)
    # print(machine)
    evenOrodd = str(input("Even or Odd ?\nType 'E' for EVEN or 'O' for ODD: ")).upper()
    if (evenOrodd[0] == "E"):
        if (machine % 2 == 1 and player % 2 == 1 or machine % 2 == 0 and player % 2 == 0):
            print("You have gained!")
            print(f"The machine choose {machine}")
            gain += 1
        else:
            if (machine % 2 == 0 and player % 2 == 1 or machine % 2 == 1 and player % 2 == 0):
                print("GAME OVER!")
                print(f"The machine choose {machine}")
                keep = 0
    elif (evenOrodd[0] == "O"):
        if (machine % 2 == 0 and player % 2 == 1 or machine % 2 == 1 and player % 2 == 0):
            print("You have gained!")
            print(f"The machine choose {machine}")
            gain += 1
        else:
            if (machine % 2 == 0 and player % 2 == 0 or machine % 2 == 1 and player % 2 == 1):
                print("GAME OVER!")
                print(f"The machine choose {machine}")
                keep = 0
    # elif (evenOrodd != "E" or evenOrodd != "O"):
    #     print("This is not accepted!!\nYou have loosen!")
    #     break
    elif (evenOrodd != "E" or evenOrodd != "O"):
        while (evenOrodd != "E" or evenOrodd != "O" and keep != 0):
            print("Enter with just the letter 'E' or 'O' to play")
            player = int(input("Choose a number: "))
            machine = randint(0, 10)
            # print(machine)
            evenOrodd = str(input("Even or Odd ?\nType 'E' for EVEN or 'O' for ODD: ")).upper()
            if (evenOrodd[0] == "E"):
                if (machine % 2 == 1 and player % 2 == 1 or machine % 2 == 0 and player % 2 == 0):
                    print("You have gained!")
                    print(f"The machine choose {machine}")
                    gain += 1
                else:
                    if (machine % 2 == 0 and player % 2 == 1 or machine % 2 == 1 and player % 2 == 0):
                        print("GAME OVER!")
                        print(f"The machine choose {machine}")
                        keep = 0
            elif (evenOrodd[0] == "O"):
                if (machine % 2 == 0 and player % 2 == 1 or machine % 2 == 1 and player % 2 == 0):
                    print("You have gained!")
                    print(f"The machine choose {machine}")
                    gain += 1
                else:
                    if (machine % 2 == 0 and player % 2 == 0 or machine % 2 == 1 and player % 2 == 1):
                        print("GAME OVER!")
                        print(f"The machine choose {machine}")
                        keep = 0
print(f"You have gained {gain} matches")'''

# ///////////////////////////////////////////////////////////////////

# SOLUTION FROM GUANABARA

'''from random import randint
g = 0
while True:
    user = int(input("Enter with a number: "))
    machine = randint(0, 10)
    total = machine + user
    type = " "
    while(type not in "OE"):
        type = str(input("Do you want even or odd ? [E/O] ")).strip().upper()[0]
    print(f"You choose {user} and the machine choose {machine}. The total is {total} ", end="")
    print("It's EVEN" if total % 2 == 0 else "It's ODD")
    if(type == "E"):
        if(total % 2 == 0):
            print("You Gained!")
            g += 1
        else:
            if(total % 2 == 1):
                print("You Loose!!")
                break
    elif(type == "O"):
        if(total % 2 == 1):
            print("You Gained!")
            g += 1
        else:
            if(total % 2 == 0):
                print("You Loose")
                break
    print("Let's play again!")
print(f"You have gained {g} times")'''

# CHALLENGE 69

'''a = "REGISTER A PERSON!"
print("---"*10)
print(" "*5 + "REGISTER A PERSON!" + " "*5)
# print(f"{a:^30}")
print("---"*10)'''

'''# keep = str("Y").upper()
peopleMajor18 = 0
womenMinor20 = 0
amountMen = 0
# while(keep[0] == "Y"):
while True:
    print("---" * 10)
    print(" " * 5 + "REGISTER A PERSON!" + " " * 5)
    # print(f"{a:^30}")
    print("---" * 10)
    age = int(input("How old are you ? "))
    sex = str(input("What is your sex ? ")).upper().strip()
    while (sex[0] != "F" and sex[0] != "M"):
        print("Just [ Y / N ]", end=" ")
        sex = str(input("What is your sex ? ")).upper().strip()
    if (age > 18):
        peopleMajor18 += 1
    if (sex[0] == "F" and age < 20):
        womenMinor20 += 1
    if (sex[0] == "M"):
        amountMen += 1
    keep = str(input("Do you want to continue [Y/N] ? ")).upper().strip()
    while(keep[0] != "Y" and keep[0] != "N"):
        keep = str(input("Do you want to continue [Y/N] ? ")).upper().strip()
    if(keep[0] == "N"):
        break
print(f"The amount of men is {amountMen}")
print(f"The amount of women with the age below 20's is {womenMinor20}")
print(f"The amount of people with the age above 18's is {peopleMajor18}")'''

# CHALLENGE 70 #  APRIMORAR COM LISTA DINÂMICA DOS PRODUTOS ACIMA DE $ 100

'''print("--"*20)
print(" "*10 + "STORE VERY CHEAP" + " "*10)
print("--"*20)
# user = "Y"
valueTotal = 0
one_hundred = 0
cheaper = 0
expensive = 0
lista = list()
lista1 = list()
lista2 = list()
# product1 = str()
# while(user[0] == "Y" or user[0] != "N"):
while True:
    product = str(input("What is the system of this product ? ")).strip().upper()
    price = float(input("What is your price ? "))
    valueTotal += price
    lista.append(product)
    if(price > 1000):
        one_hundred += 1
        product1 = product
        lista1.append(product)
    if(price < 1000):
        lista2.append(product)
    if(cheaper == 0 and expensive == 0):
        expensive = price
        cheaper = price
        expensive_product = product
        cheaper_product = product
    else:
        if(price > expensive):
            expensive = price
            expensive_product = product
            # lista1.append(product)
        if(price < cheaper):
            cheaper = price
            cheaper_product = product
    user = str(input("Do want continue ? [Y/N] ")).strip().upper()
    while(user[0] != "Y" and user[0] != "N"):
        user = str(input("Do want continue ? ")).strip().upper()
    if(user[0] == "N"):
        break
    # else:
    #     if(user[0] == "N"):
    #         break
print(f"The total value spent was {valueTotal:.2f} and they are: {lista}")
print(f"The amount of product with the value up to $ 1000.00 is {one_hundred}, and they are: {lista1}")
print(f"The system of the product cheaper is {cheaper_product}, its value is {cheaper} and they are: {lista2}")
print(f"The system of the product more expensive is {expensive_product} and its value is {expensive}")'''

# CHALLENGE 71

# print("=="*25)
# print(" "*2 + "ATM (AUTOMATIC TELLER MACHINE) SIMULATION" + " "*2)
# print("=="*25)
# withdraw = 1
# cells1 = 1
# cells10 = 10
# cells20 = 20
# cells50 = 50
# delivery = 0
# total = 0
# while(withdraw > 0):
#     withdraw = int(input("How much would you like to withdraw ? "))
#     if(withdraw >= cells1 and withdraw < cells10):
#         while(withdraw >= cells1):
#             delivery = withdraw
#             cells1 += 1
#             total = cells1 - 1
#         print(f'''The Automatic Teller Machine will delivery you ${delivery} dollars"
# Total of money cells in $1 dollar is {total}''')
#     elif(withdraw >= 10 and withdraw < cells20):
#         delivery = withdraw
#         while(withdraw < cells20 and withdraw > cells10 and total):
#             cells1 += 1
#             while(cells1 < withdraw - 10):
#                 cells1 += 1
#             while(cells10 < withdraw - cells1):
#                 cells10 += 1
#             total = cells10 + cells1
#         print(f'''The Automatic Teller Machine will delivery you ${delivery} dollars
# Total of money cells in $1 dollar is {cells1}
# Total of money cells in $10 dollar is {cells10 - 9}''')
#     elif(withdraw >= 20 and withdraw < 50):
#         delivery = withdraw
#         cells1 = 0
#         cells10 = 0
#         cells20 = 0
#         total = 0
#         while(total != withdraw):
#             delivery = withdraw
#             while(cells1 < withdraw - 20):
#                 cells1 += 1
#                 if(cells1 == 9):
#                     break
#             while(cells10 < withdraw - cells1 - 20):
#                 cells10 += 1
#                 if(cells10 == 1):
#                     break
#             while(cells20 < withdraw - cells10 - cells1):
#                 cells20 += 1
#                 if(cells20 == 1):
#                     break
#             total = cells20 + cells10 + cells1
#         print(f'''The Automatic Teller Machine will delivery you ${delivery} dollars
# Total of money cells in $1 dollar is {cells1}
# Total of money cells in $10 dollar is {cells10}
# Total of money cells in $20 dollar is {cells20 - 18}''')
#     elif(withdraw >= 50):
#         delivery = withdraw
#         cells1 = 0
#         cells10 = 0
#         cells20 = 0
#         cells50 = 50
#         total = 0
#         while(cells50 != withdraw):
#             delivery = withdraw
#             total = cells50 + cells20 + cells10 + cells1
#             while(cells1 < withdraw - 50):
#                 cells1 += 1
#                 if(cells1 == 9):
#                     break
#             while(cells10 < withdraw - cells1):
#                 cells10 += 1
#                 if(cells10 == 1):
#                     break
#             while(cells20 < withdraw - cells10 - cells1):
#                 cells20 += 1
#                 if(cells20 == 1):
#                     break
#             while(cells50 < withdraw - 50 - cells1):
#                 cells50 += 1
#             total = cells50 + cells20 + cells10 + cells1
#             print(f'''The Automatic Teller Machine will delivery you ${delivery} dollars
# Total of money cells in $1 dollar is {cells1}
# Total of money cells in $10 dollar is {cells10}
# Total of money cells in $20 dollar is {cells20}
# Total of money cells in $50 dollar is {cells50}''')
#     print("==" * 25)
# print("Come Back Always!!!")

# /////////////////////////////////////////////////////////////////////////////

# SOLUTION COME FROM PROF. GUANABARA

'''print("=="*25)
print(" "*2 + "ATM (AUTOMATIC TELLER MACHINE) SIMULATION" + " "*2)
print("=="*25)

cells1 = 0
cells10 = 10
cells20 = 20
cells50 = 50
total = 0
entrada = 1

while True:
    valorSacado = int(input("Quanto voce quer sacar ? "))
    if(valorSacado == entrada):
        print(f"Total de cédulas de R$ 1 é {valorSacado}")
    else:
        if(valorSacado > entrada):
            if(valorSacado > 1 and valorSacado < 10):
                um = valorSacado * 1
                print(f"Total de cédulas de R$ 1 é {um}")
            if(valorSacado >= 10 and valorSacado < 20):
                dez = 1
                um = (valorSacado - 10)
                print(f"Total de cédulas de R$ 1 é {um}")
                print(f"Total de cédulas de R$ 10 é {dez}")
            if(valorSacado >= 20 and valorSacado < 50):
                vinte = 
    while(entrada != valorSacado):
        if(valorSacado == 10):
            print()
'''

# ///////////////////////////

'''print("=="*25)
print(" "*2 + "ATM (AUTOMATIC TELLER MACHINE) SIMULATION" + " "*2)
print("=="*25)

valor = int(input("Quanto você quer sacar ? R$ "))
céd = 50
totalcéd = 0
# valor = 1
while True:
    if(valor >= céd):
        valor = valor - céd
        totalcéd += 1
    else:
        if(totalcéd > 0):
            print(f"O total de cédulas a receber de R$ {céd} é igual a {totalcéd}")
        if(céd == 50):
            céd = 20
        elif(céd == 20):
            céd = 10
        elif(céd == 10):
            céd = 1
        totalcéd = 0
        if(valor == 0):
            break'''


# ////////////////////////////

'''valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor = valor % 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota5 = valor // 5
valor %= 5
nota1 = valor // 1
print(f"notas de 50 = {nota50:.0f}")
print(f"notas de 20 = {nota20:.0f}")
print(f"notas de 10 = {nota10:.0f}")
print(f"notas de 5 = {nota5:.0f}")
print(f"notas de 1 = {nota1:.0f}")'''


# ///////////////////////////////////////////

'''valor = int(input('Quanto você quer sacar? R= '))
lista1 = [valor // 50, (valor%50)//20, ((valor%50)%20)//10, ((valor%50)%20)%10]
lista2 = ['R$50','R$20','R$10','R$1']
for i in range(4):
    if (lista1[i] > 0):
        print('Total de {} cédulas de {}'.format(lista1[i], lista2[i]))'''
