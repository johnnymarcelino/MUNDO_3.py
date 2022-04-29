# ENCODING: UTF-8

# TUPLAS SÃO IMUTÁVEIS

# lanche = ('hambuger', 'suco', 'pizza', 'pudim', "Batata Frita")
# print(lanche[-2::-1])

'''for count in range(0, len(lanche)):
    print(f"Vou comer {lanche[count]} na posição {count}")
print("Comi pra caramba")'''


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

'''valNum = []
count = max = min = rankMax = rankMin = a = 0
for pos, read in enumerate(range(0, 5)):
    valNum.append(int(input("Enter with the number for the position {}: ".format(count))))
    count += 1
    if(count == 1):
        rankMax = rankMin = pos
        min = max = valNum
    if(valNum > max):
        max = valNum
        rankMax = pos
    if(valNum < min):
        min = valNum
        rankMin = pos
print(f"You entered with the values: {valNum}")
print(f"O biggest value entered was {max}, in the positions {rankMax}")
print(f"O lowest value entered was {min}, in the positions {rankMin}")'''
# ////////////////////////////////////////////////////////
'''valNum = []
# count = max = min = rankMax = rankMin = a = 0
count = 0
for pos, read in enumerate(range(0, 5)):
    valNum.append(int(input("Enter with the number for the position {}: ".format(pos))))
    a = valNum
    del(valNum)
    if(max(valNum) > (a)):
        a = pos
    if(min(valNum) < (a)):
        b = pos
print(f"You entered with the values: {valNum}")
print(f"The biggest value entered was {max(valNum)}, in the positions {a}")
print(f"The lowest value entered was {min(valNum)}, in the positions {b}")'''

# CHALLENGE 79

list = []
while True:
