# ENCODING: UTF-8

# TUPLAS SÃO IMUTÁVEIS

# lanche = ('hambuger', 'suco', 'pizza', 'pudim', "Batata Frita")
# print(lanche[-2::-1])

'''for count in range(0, len(lanche)):
    print(f"Vou comer {lanche[count]} na posição {count}")
print("Comi pra caramba")'''
import afxres

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

