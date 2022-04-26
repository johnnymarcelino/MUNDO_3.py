# ENCODING: UTF-8

# TUPLAS SÃO IMUTÁVEIS

lanche = ('hambuger', 'suco', 'pizza', 'pudim', "Batata Frita")
# print(lanche[-2::-1])

'''for count in range(0, len(lanche)):
    print(f"Vou comer {lanche[count]} na posição {count}")
print("Comi pra caramba")
'''
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
numeral = int(input("Enter any number between '0' and '20': "))
if(numeral > 20):
    while(numeral > 20):
        numeral = int(input("Enter any number between '0' and '20': "))

print(f"You have choose {numeral} in numeral and this number in extensive is {numExtenso[numeral]}")'''

# CHALLENGE 73

times = ("São Paulo", "Vasco", "Botafogo", "Cruzeiro", "Flamengo", "Coritiba", "Juventude", "Arsenal", "Man Unt", "Milan", "Liverpool",
              "Inter Milão", "Real Madrid", "Barcelona", "Bayer Muniq", "Chelsea", "PSG", "Palmeiras", "Corinthians", "Zenit", "Man City")
rank = 0
print(f"These are the rankings of the top 5 on the soccer table:\n{times[0:5]}")
print(f"These are the rankings of the last 4 on the soccer table:\n{times[-4:len(times):1]}")
print(f"This is the list of the club's classification in sort {sorted(times)}")
for pos in times:
    if(pos != "Barcelona"):
        rank += 1
    if(pos == "Barcelona"):
        break
print(f"Barcelona club it is in the position {times.index(pos)}ª of the classification!")
