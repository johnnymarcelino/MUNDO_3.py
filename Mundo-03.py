# ENCODING: UTF-8

# TUPLAS SÃO IMUTÁVEIS

# lanche = ('hambuger', 'suco', 'pizza', 'pudim', "Batata Frita")
# print(lanche[-2::-1])

'''for count in range(0, len(lanche)):
    print(f"Vou comer {lanche[count]} na posição {count}")
print("Comi pra caramba")'''
import random

'''for comida in lanche:
    print(f"Vou comer {comida}")
print("Comi pra caramba")
'''

'''for pos, count in enumerate(lanche):
    print(f"Vou comer {count}, na posição {pos}")
print("Comi pra caramba")'''

# print(sorted(lanche))

'''a = (1, 4, 7, 2)
b = (7, 9, 0, 1)
c = a + b
d = sorted(c)'''
# print(sorted(c))

# print(c.count(1))
'''print(d)
print(d[2])
print(f"temos {c.count(7)} número 7")
print(f"A sua primeira posição do 7 é {c.index(7)}")
print(f"A sua segunda posição do 7 é {c.index(7, 2+1)}")'''

'''pessoa = ("Johnny", 27, 1.70, 1,68, "M")
del(pessoa)
print(pessoa)'''

# CHALLENGE 72
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, do zero até vinte.
# Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso

'''numExtenso = ("Zero", "One", "Two", "Tree", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
              "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")
# numeral = int(input("Enter any number between '0' and '20': "))
# if(numeral > 20):
#     while(numeral > 20):
while True:
    numeral = int(input("Enter any number between '0' and '20': "))
    if(numeral <= 20):
        print(f"You have chose {numeral} in numeral and this number in extensive is {numExtenso[numeral]}")
    else:
        continue
    c = str(input("Would you like keeping ? [Y / N]: ")).strip()
    if(c in "Nn"):
        break
print("You have decided to quit of the program!")'''

# CHALLENGE 73
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados.
# c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

'''times = ("São Paulo", "Vasco", "Botafogo", "Cruzeiro", "Flamengo", "Coritiba", "Juventude", "Arsenal", "Man Unt", "Milan", "Liverpool",
              "Inter Milão", "Real Madrid", "Barcelona", "Bayer Muniq", "Chelsea", "PSG", "Palmeiras", "Corinthians", "Zenit", "Man City")
rank = 0
print(("=="*20))
print(f"This is the list of clubs!\n{times}")
print(("=="*20))
print(f"These are the rankings of the top 5 on the soccer table:\n{times[0:5]}")
print(("=="*20))
print(f"These are the rankings of the last 4 on the soccer table:\n{times[-4:len(times):1]}")
print(("=="*20))
print(f"This is the list of the club's classification in sort:\n{sorted(times)}")
print(("=="*20))
print(f"Barcelona club it is in the position {times.index('Barcelona')+1}ª of the classification!")
print(("=="*20))
for pos in times:
    if(pos != "Barcelona"):
        rank += 1
    if(pos == "Barcelona"):
        break
print(f"Barcelona club it is in the position {times.index(pos)+1}ª of the classification!")'''

# CHALLENGE 74
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

'''from random import randint

# for tupla in range(random.randint(0, 10), 5):
#     lista = tupla
#     print(lista)
# tupla1 =
# tupla2 =
# tupla3 =
# tupla4 =
# tupla5 =

c = m = n = tupla = 0
e = f = 0
# tupla1 = tupla2 = tupla3 = tupla4 = 0
while(c != 5):
    # a = randint(0, 10)
    # print("numeros do A", a)
    # b = randint(0, 10)
    # print("numeros do B", b)
    # d = randint(0, 10)
    # print("numeros do D", d)
    # e = randint(0, 10)
    # print("numeros do E", e)
    # f = randint(0, 10)
    # print("numeros do F", f)
    # print()
    # tupla = tupla.split()
    # if(c == 0):
    #     m = n = a = b = d = e = f
    a = randint(0, 10)
    print("numeros do A", a)
    b = randint(0, 10)
    print("numeros do B", b)
    d = randint(0, 10)
    print("numeros do D", d)
    e = randint(0, 10)
    print("numeros do E", e)
    f = randint(0, 10)
    print("numeros do F", f)
    if(c == 0):
        m = n = a
    # else:
    if(a > m):
        m = a
    if(b > m):
        m = b
    if(d > m):
        m = d
    if(e > m):
        m = e
    if(f > m):
        m = f
    if(a < n):
        n = a
    if(b < n):
        n = b
    if(d < n):
        n = d
    if(e < n):
        n = e
    if(f < n):
        n = f
    # tupla = tuple(tupla)
    tupla = ((a), (b), (d), (e), (f))
    c = 5
print(f"The drawn numbers was: {tupla}")
print(f"The bigger number was {m}")
print(f"The lower number was {n}")'''

    # b = str(a)
    # tupla1 = str(a)
    # del(a)
    # d = str(a)
    # tupla2 = b + tupla1
    # del(b)
    # e = str(d)
    # tupla3 = e + tupla1 + tupla2
    # del(d)
    # f = str(e)
    # tupla4 = f + tupla1 + tupla2 + tupla3
    # del(e)
    # g = str(f)
    # tupla5 = g + tupla1 + tupla2 + tupla3 + tupla4
    # del(f)
    # total = list(tupla5)
    # print(d)

# SOLUTION FROM GUANABARA

'''from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# print(f"The numbers draws were:", n)
print("The numbers draws were: ", end="")
for a in n:
    print(a, end=" ")
print()
print(f"The biggest number draw was {max(n)}")
print(f"The lowest number draw was {min(n)}")'''

# CHALLENGE 75
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

'''total = 0
val1 = int(input("Enter with any number: "))
val2 = int(input("Enter with any number: "))
val3 = int(input("Enter with any number: "))
val4 = int(input("Enter with any number: "))
tupla = ((val1), (val2), (val3), (val4))
print(tuple(tupla))
print(f"The total of times that showed the number off '9' is {tupla.count(9)}")
if(3 not in tupla):
    print(f"The number '3' was not enter any time.")
else:
    print(f"The number '3' is in position {tupla.index(3)+1}ª")
count = 0
for pos, a in enumerate(tupla):
    if(a % 2 == 0):
        count += 1
        if(count == 1):
            total = (a)
            total2 = total
            del(a)
        if(count == 2):
            total1 = a
            total2 = (total, total1)
            # del(a)
        if(count == 3):
            total3 = a
            total2 = (total, total1, total3)
            # del(a)
        if(count == 4):
            total4 = a
            total2 = (total, total1, total3, total4)
            # del(a)
# if(val2 % 2 == 0):
#     count += 1
        print(f"We hava till now {count} even numbers and its positions is {pos+1}")
print(f"The total of even numbers is {count} and they are {total2}")'''

# SOLUTION FROM GUANABARA

'''núm = (int(input("Enter with a number: ")), int(input("Enter with one more number: ")),
       int(input("Enter with another number: ")), int(input("Enter with the last number: ")))
print(f"You have entered the numbers: {núm}")
print(f"The value of '9' appeared {núm.count(9)} times")
if(3 in núm):
    print(f"The number '3' is it in {núm.index(3)+1}ª position")
else:
    print(f"The value of '3' is not entered at not of position!")
print(f"The quantity of even number are: ", end="")
for n in núm:
    if(n % 2 == 0):
        print(n, end=" ")'''

# CHALLENGE 76
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''# price = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
count = 0
listing = ("Pencil", 1.75, "Eraser", 2.00, "notebook", 15.90, "Pencil Case", 25.00, "Protractor", 4.20, "Compass", 9.99, "Schoolbag", 120.32, "Pens", 22.30, "Books", 34.90)
# print(listing[2], "R$", listing[3])
for pos, products in enumerate(listing):
    print(products[count], end="..............R$: ")
    count += 1
    print(listing[count])
    # print(price)'''

# SOLUTION FROM GUANABARA

'''listing = ("Pencil", 1.75, "Eraser", 2.00, "notebook", 15.90, "Pencil Case", 25.00,
           "Protractor", 4.20, "Compass", 9.99, "Schoolbag", 120.32, "Pens", 22.30, "Books", 34.90)
# print(len(listing))
print(f"{'='*30}")
print(f"{'LIST OF PRICES':^25}")
print("="*30)
for pos in range(0, len(listing)):
    if(pos % 2 == 0):
        print(f"{listing[pos]:.<30}", end="R$")
    else:
        print(f"{listing[pos]:>7.2f}")'''


# CHALLENGE 77
#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

'''lotWords = ("rice", "mouse", "notebook", "chair", "tv", "light", "sofa", "plate", "screem", "aleloui")
for vogal in lotWords:
    if("a" in vogal and "e" and vogal and "i" in vogal and "o" in vogal and "u" in vogal):
        a = vogal.find("a")
        e = vogal.find("e")
        i = vogal.find("i")
        o = vogal.find("o")
        u = vogal.find("u")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}, {vogal[e]}, {vogal[i]}, {vogal[o]}, {vogal[u]}")
    if ("a" in vogal and "e" in vogal and "i" in vogal and "o" in vogal):
        a = vogal.find("a")
        e = vogal.find("e")
        i = vogal.find("i")
        o = vogal.find("o")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}, {vogal[e]}, {vogal[i]}, {vogal[o]}")
    if ("a" in vogal and "e" in vogal and "i" in vogal):
        a = vogal.find("a")
        e = vogal.find("e")
        i = vogal.find("i")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}, {vogal[e]}, {vogal[i]}")
    if ("a" in vogal and "e" in vogal):
        a = vogal.find("a")
        e = vogal.find("e")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}, {vogal[e]}")
    if ("a" in vogal):
        a = vogal.find("a")
        print(f"In phrase {vogal}, we have the vowels {vogal[a]}")
    if ("e" in vogal):
        e = vogal.find("e")
        print(f"In phrase {vogal}, we have the vowels {vogal[e]}")
    if ("i" in vogal):
        i = vogal.find("i")
        print(f"In phrase {vogal}, we have the vowels {vogal[i]}")
    if ("o" in vogal):
        o = vogal.find("o")
        print(f"In phrase {vogal}, we have the vowels {vogal[o]}")
    if ("u" in vogal):
        u = vogal.find("u")
        print(f"In phrase {vogal}, we have the vowels {vogal[u]}")
    # else:
    #     print("This is not in 'aeiou'")
    # print(vogal)'''

# SOLUTION FROM GUANABARA

'''lotWords = ("rice", "mouse", "notebook", "chair", "tv", "light", "sofa", "plate", "screem", "aleloui")
for vowels in lotWords:
    print(f"\nIn the phrase {vowels.upper()} we have: ", end="")
    for letter in vowels:
        if(letter.lower() in "aeiou"):
            print(letter, end=" ")'''

# CLASS 17

# num = (2, 4, 8, 1, 3)
# num[2] = 4  #  tuplas são imutáveis
# print(num)
'''
num = [2, 4, 8, 1, 3]
num[2] = 0
# num = 5  #  receber total
# print(num)
num.append(6)
num.sort()
num.sort(reverse=True)
num.insert(5, 10)
num.pop(4)
num.insert(4, 4)
if(1 in num):
    num.remove(4)
else:
    print("não encontrei o valore 1!")
print(num)
print(f"Essa lista tem {len(num)} elementos!")'''

'''valores = list()
# valores.append(4)
# valores.append(9)
# valores.append(2)
# print(valores)

for count in range(0, 6):
    valores.append(int(input("Enter with a number: ")))
    for c, v in enumerate(valores):
        print(f"Na posição {c}, encontrei o valor {v}!")
print("Cheguei ao final da lista!")'''

'''a = [1, 7, 5, 3]
# b = a  # Cria uma ligação entre as listas
b = a[:]  # Lista B cria uma cópia de lista A
b[2] = 9
print(f"Lista A: {a}")
print(f"Lista B: {b}")'''

# CHALLENGE 78
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

'''valNum = rankMax = rankMin = []

count = 0
for pos, read in enumerate(range(0, 5)):
    count += 1
    a = int(input("Enter with the number for the position {}: ".format(count)))
    valNum.append(a)
    if(count == 1):
        rankMax.append(pos)
        rankMin.append(pos)
        maior = menor = a
    if(a > maior):
        maior = a
        if(a > )
        rankMax.remove(max(rankMax))
        rankMax.append(pos)
    if(a < menor):
        menor = a
        rankMin.append(pos)
print(f"You entered with the values: {valNum}")
print(f"O biggest value entered was {max(valNum)}, in the positions {rankMax}")
print(f"O lowest value entered was {min(valNum)}, in the positions {rankMin}")'''


# ////////////////////////////////////////////////////////

# Done
'''valNum = []
a = []
b = []
# count = max = min = rankMax = rankMin = a = 0
count = 0
for pos, read in enumerate(range(0, 20)):
    add = int(input("Enter with the number for the position {}: ".format(pos+1)))
    count += 1
    if(count == 1):
        a.append(pos+1)
        b.append(pos+1)
        maior = menor = add
    if(add > maior):
        maior = add
        if(add in valNum):
            if(add > max(valNum)):
                del(a[:])
                a.append(pos+1)
            if(add == max(valNum)):
                a.append(pos+1)
            # else:
            #     continue
        else:
            if(add > max(valNum)):
                del(a[:])
                a.append(pos+1)
            if(add == max(valNum)):
                a.append(pos+1)
            # else:
            #     continue [5, 9, 15, 20, 45, 45, 12, 15, 16, 79, 15, 45, 7, 5, 5, 6, 45, 79, 79, 45, 5]
    if(add < menor):
        menor = add
        if(add in valNum):
            if(add < min(valNum)):
                del(b[:])
                b.append(pos+1)
            if(add == min(valNum)):
                b.append(pos+1)
            # else:
            #     continue
        else:
            if(add < min(valNum)):
                del(b[:])
                b.append(pos+1)
            if(add == min(valNum)):
                b.append(pos+1)
            # else:
            #     continue
    else:
        if(add in valNum):
            if(add == max(valNum)):
                a.append(pos+1)
            else:
                if(add == min(valNum)):
                    b.append(pos+1)
    valNum.append(add)
    # print(f"Max A {max(a)}")
    # print(f"Min B {min(b)}")
print(f"You entered with the values: {valNum}")
print(f"The biggest value entered was {max(valNum)}, in the positions {a}")
print(f"The lowest value entered was {min(valNum)}, in the positions {b}")'''

# //////////////////////////////////////////////////////////////////////////////////

# SOLUTION FROM GUANABARA

'''lista = list()
bigger = lower = 0
# for rank, value in enumerate(range(0, int(input("Enter with a number: ")))):
for value in range(0, 5):
    # print(" First", value)
    lista.append(int(input("Enter with a number: ")))
    # print("Second", value)
    if(value == 0):
        bigger = lower = lista[value]
    else:
        if(lista[value] > bigger):
            bigger = lista[value]
        if(lista[value] < lower):
            lower = lista[value]
    # print(lista[value])
print(lista)
print(f"The biggest numbers was {bigger}, And they are in the posotion ", end=" ")
for pos, valueB in enumerate(lista):
    if(valueB == bigger):
        print(f"{pos}", end="...")
print(f"\nThe lowest number entered was: {lower}, and are in the position: ", end="")
for pos, valueB in enumerate(lista):
    if(valueB == lower):
        print(f"{pos}", end="...")'''


# CHALLENGE 79
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

'''list = []
while True:
    adicionar = int(input("Enter with a number: "))
    if(adicionar in list):
        print("Este número já existe na lista, não vou adicionar!")
    else:
        list.append(adicionar)
        print(f"O número {adicionar} foi adicionado com sucesso!")
    stop = str(input("Do you want keep up ? [Y / N]: "))
    if(stop[0].upper() == "N"):
        break
list.sort()
print(f"Você digitou os números: {list}")'''

# CHALLENGE 80
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

'''lista = []
for b, a in enumerate(range(0, 5)):
    add = int(input("Enter with a number: "))
    if(add not in lista):
        for c in lista:
            if(c < min(lista)):
                lista.append(add)
                print(f"{add} foi adicionado na posição {b}")
            if(c > max(lista)):
                lista.append(add)
                print(f"{add} foi adicionado na posição {b}")
    else:
        
print(f"Você cadastrou os números {lista}")'''

# ////////////////////////////  45 47 44 49 16 50 47 46 49 47

'''lista = list()
count = 0
for b, a in enumerate(range(0, 10)):
    add = int(input("Enter with a number: "))
    # if(add in lista):
    #     for c in lista:
    #         count += 1
    #         if(c == add):
    #             lista.insert(lista.index(c)+count, add)
    #             print(f"{add} foi adicionado na posição {lista.index(c)+count}")
    #             break
    if(add not in lista):
        for c in lista:
            count += 1
            if(add > max(lista)):
                count += 1
                lista.insert((lista.index(max(lista)))+1, add)
                print(f"{add} foi adicionado na última posição ({lista.index(max(lista))})º!")
                break
            elif(add < min(lista)):
                count += 1
                lista.insert((lista.index(min(lista))), add)
                print(f"{add} foi adicionado na primeira posição ({lista.index(min(lista))})º!")
                break
            else:
                if(add == c):
                    count += 1
                    lista.insert(lista.index(c), add)
                    print(f"{add} foi adicionado na posição {lista.index(c)}")
                    break
        if(count <= 0):
            lista.append(add)
            print(f"{add} foi adicionado na última posição!")
        else:
            if(add not in lista):
                # count += 1
                # for c in lista:
                if(add > lista[-1]):
                    lista.insert(lista.index(lista[-1])+1, add)
                    print(f"{add} foi adicionado na posição {lista.index(lista[-1])+1}")
                else:
                    pos = 0
                    while(pos < len(lista)):
                        if(add <= lista[pos]):
                            lista.insert(pos, add)
                            break
                        pos += 1
                    print(f"{add} foi adicionado na posição {lista.index(add)}")
                        # z = lista.count(add)
                        # if(z > 1):
                        #     del(lista[1])
                        #     break
        # if(count <= 0):     #  45 25 16 49 44  /// 16, 47, 47, 44, 45, 47, 46, 47, 49, 50] //// 45 47 44 49 16 50 47 46 49 47
        #     lista.append(add)
        #     print(f"{add} foi adicionado na última posição!")
        #     break
    else:
        if(add in lista):
            # count += 1
            for c in lista:
                if(c == add):
                    lista.insert(lista.index(c), add)
                    print(f"{add} foi adicionado na posição {lista.index(c)+1}")
                    break
    # else:
    #     lista.append(add)
print("="*60)
print(f"Você cadastrou, em ordem, os números: {lista}")
print(len(lista))'''


# CHALLENGE 81
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#  A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

'''cadastro = []
count = 0
while True:
    cadastro.append(int(input("Enter with a number: ")))
    count += 1
    user = str(input("Wolud like to continue ? [S / N]: ")).strip().upper()[0]
    if(user == "N"):
        break
print("="*50)
print(f"The list entered with the numbers is: {cadastro}")
print("="*50)
print(f"The total of elements entered were: {count}")
print("="*50)
if(5 in cadastro):
    print(f"The number '5' is in the list {cadastro}, in the position {cadastro.index(5)}")
    print("The number '5' logically was entered")
else:
    print(f"The number '5' is not in lista: {cadastro}")
print("="*50)
cadastro.sort(reverse=True)
print(f"The numbers inserted in position decreasing is: {cadastro}")'''

# CHALLENGE 82
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

'''lista1 = []
listaEven = []
listaOdd = []
evenCount = 0
oddCount = 0
while True:
    lista1.append(int(input("Enter with a number: ")))
    contiOrBreak = str(input("Would like to continue ? [Y / N]: ")).strip().upper()[0]
    if (contiOrBreak == "N"):
        break
for even in lista1:
    if(even % 2 == 0):
        listaEven.append(even)
        evenCount += 1
    else:
        listaOdd.append(even)
        oddCount += 1
print(f"The numbers entered in the list were: {lista1}")
print(f"The numbers even entered were: {listaEven} and they are at totally: {evenCount}")
print(f"The numbers odd entered were: {listaOdd} and they are at totally: {oddCount}")'''

# CHALLENGE 83
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

'''express = list(str(input("Enter with the express: ")))
# print(express[-1])
# print(express)
# print(len(express))
# print("(" in express)
# print(express.count("("))
# for together in express:
# if(express[0] == ")"):
#     print("Express is not allowed!")
if(express.count("(") == express.count(")") and express[-1] != "(" and express[0] != ")"):
    print("Express is allowed!")
# elif(str(express)):
# if(express[-1] == "("):
#     print("Express is not allowed!")
else:
    if(express[0] == ")" or express[-1] == "(" or express.count("(") != express.count(")")):
        print("Express is not allowed!")
# print(len(express))
# print("".join(express))
# a = []
# for to in express:
#     print(to)
print(f"The Express used was '{''.join(express)}'")'''

'''exp = str(input('Digite a expressão: '))
print('A expressão está correta!' if exp.count('(') == exp.count(')') and exp[0] != ")" and exp[-1] != "(" else 'A expressão está errada!')'''

# SOLUTION FROM GUANABARA

'''express = list(str(input("Enter with the express: ")))
pilha = list()
for sim in express:
    if(sim == "("):
        pilha.append("(")
    elif(sim == ")"):
        if(len(pilha) > 0):
            pilha.pop()
        else:
            pilha.append(")")
            break
if(len(pilha) == 0):
    print("A sua expressão está certa!")
else:
    print("A sua expressão não está certa!")'''

# CLASS 18

'''teste = list()
teste.append("Johnny")
teste.append(26)
print(teste)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = "Jorge"
teste[1] = 30
print(galera)
galera.append(teste[:])
print(galera)'''

'''galera = [["Danilo", 40], ["Alana", 25], ["Jose", 26], ["João", 18]]
# print(galera[3][0])
for p in galera:
    # print(p[0][1])
    print(f"{p[0]}, tem {p[1]} anos de idade")'''

'''galera = list()
dados = list()
totmaoir = totmenor = 0
for c in range(0, 3):
    dados.append(str(input("Digite o nome: ")))
    dados.append(int(input("Digite idade: ")))
    galera.append(dados[:])
    dados.clear()
# print(galera)
for p in galera:
    if(p[1] >= 21):
        print(f"{p[0]}, é maior de idade!")
        totmaoir += 1
    else:
        print(f"{p[0]}, é menor de idade!")
        totmenor += 1
print(f"O total de maiores de idade é {totmaoir} e de menor é {totmenor}")'''

# CHALLENGE 84
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas, B) Uma listagem com as pessoas mais pesadas e C) Uma listagem com as pessoas mais leves.

'''nome = list()
dada = list()
heaviestLi = list()
lightestLi = list()
person = 0
while True:
    nome.append(str(input("What is your name: ")))
    nome.append(float(input("How much weight are you: ")))
    contOrBrk = str(input("Would like to continue [Y / N] ? "))
    dada.append(nome[:])
    nome.clear()
    if(contOrBrk[0].upper().strip() == "N"):
        break
for p in dada:
    if(p[0] == p[0]):
        person += 1
        nome.append(p[0])
heaviest = dada[0][1]
lighter = dada[0][1]
count = 0
for w in dada:
    if(w[1] >= heaviest):
        # print(f"{w[0]} is the most heaviest!")
        if(w[1] == heaviest):
            heaviestLi.append(w[0])
        if(w[1] > heaviest):
            heaviest = w[1]
            heaviestLi.clear()
            heaviestLi.append(w[0])
    if(w[1] <= lighter):
        # print(f"{w[0]} is the most lightest!")
        if(w[1] == lighter):
            lightestLi.append(w[0])
        if(w[1] < lighter):
            lighter = w[1]
            lightestLi.clear()
            lightestLi.append(w[0])
    count += 1
print(f"The list you have entered was: {dada}")
print(f"The total of people register was: {person}")
print(f"They are: {nome}")
print(f"The people who is the most heaviest is {heaviestLi}, with {heaviest}Kg!")
print(f"The people who is the most lightest is {lightestLi}, with {lighter}Kg!")'''

# //////////////////////////////////////////////////////////////////////////////////////

# SOLUTION FROM GUANABARA

'''temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if(len(princ) == 0):
        mai = men = temp[1]
    else:
        if(temp[1] > mai):
            mai = temp[1]
        if(temp[1] < men):
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar? [S / N] "))
    if(resp in "Nn"):
        break
print("-="*50)
# print(f"Os dados foram {princ}")
print(f"Ao todo, você cadastrou {len(princ)} pessoas")
print(f"O menor peso foi de {men}Kg. Peso de ", end="")
for p in princ:
    if(p[1] == men):
        print(f"[{p[0]}]", end=" ")
print()
print(f"O maior peso foi de {mai}Kg. Peso de: ", end=" ")
for p in princ:
    if(p[1] == mai):
        print(f"[{p[0]}]", end=" ")'''

# CHALLENGE 85
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

'''numeros = [[], []]
for c in range(1, 7+1):
    user = int(input(f"Digite o {c}º valor: "))
    if(user % 2 == 0):
        numeros[0].append(user)
    if(user % 2 == 1):
        numeros[1].append(user)
print("-=" * 50)
numeros[0].sort()
numeros[1].sort()
# print(numeros)
print(f"Os valore pare cadastrados são: {numeros[0]}")
print(f"Os valores impares cadastrados são: {numeros[1]}")'''

# ////////////////////////////////////////////////////////
# ANOTHER SOLUTION

'''lista_de_numeros = []
for c in range(1, 8):
    lista_de_numeros.append(int(input(f'Digite o {c}° valor: ')))
lista_de_numeros.sort()
print('-=' * 40)
print(f'Os valores pares digitados foram: ', end='')
for n in lista_de_numeros:
    if n % 2 == 0:
        print(f'{n} ', end='')
print(f'\nOs valores impares digitados foram: ', end='')
for n in lista_de_numeros:
    if n % 2 != 0:
        print(f'{n} ', end='')'''


# for n in numeros:
#     # if(n % 2 == 0):
#     numeros.append([n[numeros]])
#     if(n % 2 == 1):
#         numeros.append([n][numeros])
# print(numeros)

'''val = list()
evenAndOdd = list()
for rank, c in enumerate(range(0, 7)):
    user = int(input(f"Enter with the {rank+1}º. value: "))
    val.append([user][0])
    # print(val)
for d in val:
    if(d % 2 == 0):
        evenAndOdd.append([[1], [0]])
    else:
        if(d % 2 == 1):
            evenAndOdd.append([[0], [1]])
print(evenAndOdd)'''

# print(val)
# for a in val:
#     if(a % 2 == 0):
#         evenAndOdd.append()
#     else:
#         evenAndOdd.append([0][0])
# # j = evenAndOdd[0][1]
# print(evenAndOdd)
# print(j)

# CHALLENGE 86
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

'''a = list()
count = 0
for c in range(0, 3):
    for x in range(0,3):
        if(count < 3):
            a.append(int(input("Digite o primeiro valor para [{}, {}]: ".format(c, x))))
            count += 1
    count = 0
    for y in range(3, 6):
        if(count > 2 and count < 6):
            a.append(int(input("Digite o primeiro valor para [{}, {}]: ".format(count, y))))
            count += 1
    count = 0
    for z in range(7, 9):
        if(count > 5 and count < 10):
            a.append(int(input("Digite o primeiro valor para [{}, {}]: ".format(count+c, z))))
            count += 1
count = 0
for d in a:
    if(count < 3):
        print("[ {} ]".format(d), end="")
    count += 1
print()
count = 0
for d in a:
    if(count > 2 and count < 6):
        print("[ {} ]".format(d) , end="")
    count += 1
print()
count = 0
for d in a:
    if(count > 5):
        print("[ {} ]".format(d) , end="")
    count += 1'''

# SOLUTION FROM GUANABARA

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para: [{l}, {c}]: "))
print(matriz)
for numero in matriz:
    for numero1 in numero:
        print(f"[{numero1:^5}]", end=" ")
    print()'''


# CHALLENGE 87
# Aprimore o desafio anterior, mostrando no final.
# A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

'''a = list()
count = 0
somaPar = 0
tercCol = 0
maior = 0
for c in range(0, 3):
    for x in range(0,3):
        if(count < 3):
            user = int(input("Digite o primeiro valor para [{}, {}]: ".format(c, x)))
            if(user % 2 == 0):
                somaPar += user
            if(count == 2):
                tercCol += user
            if(c == 1):
                maior = user
            if(count > 3):
                if(user > maior):
                    maior = user
            a.append(user)
            count += 1
    count = 0
    # for y in range(3, 6):
    #     if(count > 2 and count < 6):
    #         user = int(input("Digite o primeiro valor para [{}, {}]: ".format(count, y)))
    #         if(user % 2 == 0):
    #             somaPar += user
    #         if(count == 5):
    #             tercCol += user
    #         if(count == 3):
    #             maior = user
    #         if(count > 3):
    #             if(user > maior):
    #                 maior = user
    #         a.append(user)
    #         count += 1
    # count = 0
    # for z in range(7, 9):
    #     if(count > 5 and count < 10):
    #         user = int(input("Digite o primeiro valor para [{}, {}]: ".format(count, y)))
    #         if(user % 2 == 0):
    #             somaPar += user
    #         if (count == 9):
    #             tercCol += user
    #         if (count == 3):
    #             maior = user
    #         if(count > 3):
    #             if(user > maior):
    #                 maior = user
    #         a.append(user)
    #         count += 1
count = 0
for d in a:
    if(count < 3):
        print("[ {:^5} ]".format(d), end="")
    count += 1
print()
count = 0
for d in a:
    if(count > 2 and count < 6):
        print("[ {:^5} ]".format(d) , end="")
    count += 1
print()
count = 0
for d in a:
    if(count > 5):
        print("[ {:^5} ]".format(d) , end="")
    count += 1
print()
print("="*50)
print("A soma de todos os valores pares digitados foram: {}".format(somaPar))
print("A soma de todos os valores da terceira coluna digitados foram: {}".format(tercCol))
print("O maior valor digitado da segunda linha foi: {}".format(maior))'''

# CHALLENGE 88
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

'''from random import randint
from time import sleep

print("="*50)
print("{:^50}".format("Vamos jogar na Mega-Sena"))
print("="*50)
jogos = []
user = int(input("Quantos jogos você quer realizar ? "))
count = 0
gravados = []
if(user == 1):
    print("-="*5, "SORTEANDO {} JOGO".format(user), "-="*5)
else:
    print("-="*5, "SORTEANDO {} JOGOS".format(user), "-="*5)
for jogadas in range(user):
    for vezes in range(0, 6):
        aleat = randint(1, 60)
        while(aleat in jogos):
            aleat = randint(1, 60)
        jogos.insert(vezes, aleat)
    count += 1
    gravados.append(jogos[:])
    sleep(1)
    jogos.sort()
    print(f"Jogo {jogadas+1}: {jogos}")
    jogos.clear()
print(f"{'-=<'*5} {'Boa Sorte!'} {'>-='*5}")
# print(gravados)'''

# CHALLENGE 89
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'''alunos = []
while True:
    a = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    alunos.append((a, n1, n2, media))
    cp = str(input("Quer continuar [S / N] ? ")).strip().upper()
    if(cp == "N"):
        break
print("-="*20)
print(f"{'No'}  {'Nome':<10}{'Média':>10}")
for index, grade in enumerate(alunos):
    print(f'{index}  {alunos[index][0]:<10}{alunos[index][3]:>10.2f}')
print("-"*20)
while True:
    mostrar = int(input("Mostrar a nota de qual alunos ? (999 interrompe): "))
    if(mostrar == 999):
        break
    else:
        if(mostrar == len(alunos)-1):
            print(f"notas de {alunos[mostrar][0]}, são: [{alunos[mostrar][1]}], [{alunos[mostrar][2]}]")
            print("-"*25)
print("Processos finalizados!")
print(alunos)'''

# CLASS 19

# pessoas = {"nomes": "Johnny", "Sexo": "M", "Idade": 26}
# print(pessoas)
# print(pessoas["Idade"])
# print(pessoas["nomes"])
# print(pessoas["Sexo"])
# print(f"O {pessoas['nomes']} é do sexo {pessoas['Sexo']} com idade de {pessoas['Idade']}")
# print(f'O {pessoas["nomes"]} tem {pessoas["Idade"]} anos de idade e é do sexo {pessoas["Sexo"]}')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# print()
# print()
# for k in pessoas.keys():
#     print(k)
# print()
# for v in pessoas.values():
#     print(v)
# print()
# for items in pessoas.items():
#     print(items)
# print()
# print()
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# print()
# print()
# # del(pessoas["Sexo"])
# # print(pessoas)
#
# pessoas["nomes"] = "Gabriel"
# print(pessoas)
#
# pessoas["Peso"] = 68.5
# print(pessoas)
# print(pessoas["Peso"])
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# //////////////////////////////////////////////////////////////////

'''brasil = []
estado1 = {"uf": "Rio de Janeiro", "Sigla": "RJ"}
estado2 = {"uf": "São Paulo", "Sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(estado2)
print(estado1)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]["Sigla"])
print(brasil[0]["uf"])
print(brasil[1]["uf"])'''

'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["Sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)'''
# for k in brasil:
#     print(k)
# for k, v in brasil:
#     print(f'A {k} é {v}')

'''for e in brasil:
    for v in e.values():
        print(f'{v}', end=" ")
    # if(len(brasil) < len(brasil)):
    print("-> ", end="")
    # for k, v in e.items():
    #     print(f'O campo {k} tem valor {v}')'''

# CHALLENGE 90

# notaFinal = {}
# while True:
#     notaFinal['name'] = str(input("What is your name ? "))
#     notaFinal['media'] = float(input("What is your media grade in school ? "))
#     print(f"Name is {notaFinal['name']}")
#     print(f"Media is {notaFinal['media']}")
#     if(notaFinal['media'] >= 7):
#         # print(f"{notaFinal['name']} you were approved in the test, cause your media grade was {notaFinal['media']}!")
#         print(f"Situation is equal APPROVED!")
#     else:
#         # print(f"{notaFinal['name']} you were not approved in the test, cause your media grade was {notaFinal['media']:.1f}!")
#         print(f"Situation is equal FAILED!")
#     break

# phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
# for name, number in phonebook.items():
#     print("Phone number of %s is %d" % (name, number))

# CHALLENGE 91 - UNCOMPLETED

'''from random import randint
from time import sleep

count = 1
# greater = 0
# less = 0
player = {}
# while(count < 4):
print("DRAWN NUMBERS")
for x in range(1, 5):
    # number = int(input(f"Player {count}, enter here with the number '1' to play the data: "))
    data = randint(1, 6)
    player[f'player{count}'] = data
    # while(number != 1):
    #     player = int(input(f"Player {count}, enter here with the number '1' to play the data!: "))
    # if(count == 1):
    #     greater = data
    #     less = data
    # else:
    #     if(data > greater):
    #         greater = data
    #     if(data < less):
    #         less = data
    # player[f"player {count}"] = dict(data)
    print(" "*3, f'player{count} have got {data}')
    sleep(1)
    # print(f'Number of the player {count} was {data}!')
    count += 1
print()
sorted(player.values())
print("PLAYERS RANKING")
# for big in player.values():
#     if(count == 4):
#         player["player1"] = big
#     else:
#         for cmp in player.values():
#             if()
#         if(big > player):

count = 1
# for ply, value in player.items():
#     print(" "*3, f"{count}º position: {ply} with {value}")
#     count += 1
#     sleep(1)

for i, v in sorted(player.items()):
    print(" "*3, f"{i} with {v}")


# print(player)
# print()
# playerList = list(player)
# playerList.sort()
# print(playerList)
# print()
# playerDic = dict(playerList)
# print(playerDic)
# data = randint(1, 6)
# player ='''

# CHALLENGE 92

'''employee = {}
employee["name"] = str(input("What is your name ? "))
employee["age"] = int(input("Which year do you born ? "))
employee["spjc"] = int(input("What is the number of your work card ? [0] In case not have "))
employee["age"] = 2022 - employee["age"]
if(employee["spjc"] == 0):
    print("=-=" * 15)
    print(f"Your name is {employee['name']}!")
    print(f"You are {employee['age']} years old!")
    print(f"The number of your job card is {employee['spjc']}")
else:
    employee["started"] = int(input("Which year do you started in the first company ? "))
    employee["salary"] = float(input("What is your salary currently ? "))
    employee["retire"] = (35 - (2022 - employee["started"])) + employee["age"]
    print("=-=" * 15)
    print(f"Your name is {employee['name']}!")
    print(f"You are {employee['age']} years old!")
    print(f"The number of your job card is {employee['spjc']}")
    print(f"Your currently salary is {employee['salary']}")
    print(f"Your fist work was in {employee['started']}")
    print(f"Therefore you will retire when you are {employee['retire']}")
print("=-="*15)
print(employee)'''

# CHALLENGE 93

'''play_better = {}

play_better["name"] = str(input("Name: "))
match = int(input(f"How many match {play_better['name']} have played: "))
count = 0
lista = []
# play_better["goals"] = {}
for g in range(match):
    lista.append(int(input(f"How many goals did {play_better['name']} score in match {g+1}: ")))
    count += lista[g]
    # play_better["goals"] = list[int(input(f"How many goals did {play_better['name']} score in match {g}: "))]
    # play_better["totalGoals"] = play_better["goals"].copy()
# play_better["goals"] = int(input(f"How many goals did you score in {play_better['match']} match: "))
# play_better["performance"] = play_better["match"] / count
# print("Your performance is {:.2f} per match!".format(play_better["performance"]))
print("=-="*20)
play_better["goals"] = lista
play_better["total"] = count
# print(count)
# print()
print(play_better)
print("=-="*20)
for k, v in play_better.items():
    print(f"The field {k} has the value {v}")
print("=-="*20)
# print(f"Your name is {play_better['name']}")
print(f"Player {play_better['name']} played {match} matches")
# print()
c = 1
for each, goal in play_better.items():
    if(each == "goals"):
        for a in goal:
            print(" "*2, "=> " f'In the match {c}, scored {a}')
            c += 1
print(f"It is a total of {play_better['total']} goals")
# for k, v in play_better.items():'''

