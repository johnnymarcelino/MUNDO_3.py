# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.'''


# Press the green button in the gutter to run the script.
import math
import random

import emoji

'''if __name__ == '__main__':
    print_hi('PyCharm')'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Coding: UTF-8

# exercicio 001 print o nome holla mundo

'''holla_mundo = "Hello World!"
print(holla_mundo)'''

# Testes de pycharm

'''def print_hi(name):
    if(johhny == "gabriel"):
        print("Hello World!")'''
# print_hi("Johnny") # test of function print_hi()

# Exercício Python 2: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
'''
nome = str(input("What is your name: "))
print("Seja bem-vindo, {}!" .format(nome))'''

'''start = print("Write down your name below! ")
name = input()
b = input("In case you write down your name, type 'y' for Yes and 'n' for No.")
saudacao = ("It's a pleasure to meet you, ")

if (b == "y"):
    print(saudacao, name, "Program finished!")
else:
    while(b != "n" or "y"):
            start = print("Write down your name below, cause the letter", b, "it's not a variable avalible!")
            name = input()
            b = input("In case you write down your name, type 'y' for Yes and 'n' for No.")
            saudacao = ("It's a pleasure to meet you, ")
'''
# I stopped on class number 06

'''n1 = int(input("Type a number: "))
n2 = int(input("Type a number: "))
s = n1 + n2
print("The sum between {} e {} é: {}".format(n1, n2, s))
print(type(n1))
# n3 = n1.isnumeric() # Dec
print(n3.isalpha())'''

'''numstr = '100' #numeric digits
print(numstr.isnumeric())

numstr = "j" #'\u0034' # \u0034 is 4
print(numstr.isnumeric())

numstr = '\u00BD' # \u0024 is ½
print(str.isnumeric())

numstr = '¾'
print(numstr.isnumeric())'''

'''a = input("Type anything: ")

if(a.isnumeric()):
    print(a, "Is numeric")
    if(a.isalnum()):
        print(a, "is alphanumeric!")
else:
    if(a.islower()):
        print(a, "Is lower")
    else:
        if(a.isupper()):
            print(a, "is upper")
        else:
            if(a.isspace()):
                print(a, "is space")
            else:
                print(a, "Is str")'''

# Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.

'''n1 = int(input("Type a number: "))
n2 = int(input("Type a number: "))
s = n1 + n2
print("The sum between {} e {} é: {}".format(n1, n2, s))'''
# print(type(n1))

# Exercício Python 4: Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

'''a = input("Type anything: ")
print(type(a))
print("It is alphanumeric: {}" .format(a.isalnum()))
print("It is upper: {}" .format(a.isupper()))
print("It is lower: {}" .format(a.islower()))
print("It is space: {}" .format(a.isspace()))
# print("It is al: ", a.isalnum())
print("It is alpha: {}" .format(a.isalpha()))
print("It is captalizaded: {}" .format(a.istitle()))'''


'''if(a.isnumeric()):
    print(a, "Is numeric")
    if(a.isalnum()):
        print(a, "is alphanumeric!")
else:
    if(a.islower()):
        print(a, "Is lower")
    else:
        if(a.isupper()):
            print(a, "is upper")
        else:
            if(a.isspace()):
                print(a, "is space")
            else:
                print(a, "Is str")'''

# Aula 07
# coding: utf-8

'''nome = str(input("What is your name: "))
print("Seja bem-vindo, {:=<50}!" .format(nome))'''
'''div = float(input("typw any number for divisor: "))
numr = float(input("Type any number for number"))
total = div / numr
print("The divisions between {} \ne {} \nis: {:.2f}\n".format(div, numr, total ), end=" >>> ")
print("This calculation is simple, \nis not it")
'''

'''num = float(input("Type here any number: "))
num2 = float(input("Type here another number wished: "))
ant = float(input("Type here any number: "))
suc = float(input("Type here any number: "))'''

'''print()
print("Your number chosen is {} and its predecessor is {} and successor is {}".format(num, num-1, num+1))
print()
print("Your number chosen is {} and its double is {} and its triple is {} and finally"
      " its square root is "
      "{}".format(num, num*2, num*3, num**(1/2)))
print()
print("Your first grade is {} and your second grade is {} then the media grade is {}".format(num, num2, (num+num2)/2))
print()'''
'''cal_conv = float(input("Choose any number in metres to convert in centimeters and minimitres: "))
print("You chose the number {:.2f}m and converted in centimeters is {:.2f}cm and in "
      "minimeters is {:.2f}mm".format(cal_conv, cal_conv*100, cal_conv*1000))'''

'''tabuada = int(input("Type here any number for calculate its multiplication table: "))
# tabuada1 = int(input("Type here any number for calculate its multiplication table: "))
# tabuada2 = int(input("Type here any number for calculate its multiplication table: "))
# tabuada3 = int(input("Type here any number for calculate its multiplication table: "))
# tabuada4 = int(input("Type here any number for calculate its multiplication table: "))
# tabuada5 = int(input("Type here any number for calculate its multiplication table: "))
c1 = tabuada/1
c2 = tabuada/2
c3 = tabuada/3
c4 = tabuada/4
c5 = tabuada/5
c6 = tabuada/6
c7 = tabuada/7
c8 = tabuada/8
c9 = tabuada/9
c10 = tabuada/10

print("The multiplication table of the number have chosen for you is:")
print("---"*5)
print(tabuada,"/ 1 = {:2}".format(c1))
print(tabuada,"/ 2 = {:2}".format(c2))
print(tabuada,"/ 3 = {:2}".format(c3))
print(tabuada,"/ 4 = {:2}".format(c4))
print(tabuada,"/ 5 = {:2}".format(c5))
print(tabuada,"/ 6 = {:2}".format(c6))
print(tabuada,"/ 7 = {:2}".format(c7))
print(tabuada,"/ 8 = {:2}".format(c8))
print(tabuada,"/ 9 = {:2}".format(c9))
print(tabuada,"/ 10 = {:2}".format(c10))
print("---"*5)'''

# how much money have in the wallet and how much dollars can buy
# value of dollar is 3.27

'''have_wallet = float(input("Type here how much money do you have in your wallet in reais: "))
val_dor = 4.74

canBuy = have_wallet/val_dor
print("You've just R$ {:.2f} and you can just buy in dollars a few of $ {:.2f} ".format(have_wallet, canBuy))'''

# how many it is necessary of wall paint to paint the wall

'''length = float(input("Type here a length of your wall: "))
height = float(input("Type here a height of your wall: "))
one_litre_paint = 2
areWall = length * height
paintNecessary = areWall / one_litre_paint
print("Are total of your wall is {:.2f}m² so you have to {:.2f}lt "
      "of wall paint to paint all your wall!".format(areWall, paintNecessary))'''


# Product price and its new price late of discont

'''product_price = float(input("Type here a price of the product you have encountered on the shelf: "))
percentage = (5/100) * product_price
discount = product_price - percentage
print("The price of the product is {:.2f} and with the discount of 5% (R$ {:.2f}), "
      "the new price is R$ {:.2f}".format(product_price, percentage, discount))'''

# New salary/wage of the functionary increse of 15%

'''salary = float(input("Type here a price of the product you have encountered on the shelf: "))
percentage_increase = (15/100) * salary
new_salary = salary + percentage_increase
print("Your current wage is {:.2f} and with the increase of 15% (R$ {:.2f}), "
      "your new salary is R$ {:.2f}".format(salary, percentage_increase, new_salary))'''


# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.


'''num_int = int(input("Type a number: "))
print("The number typing is {}, so its predecessor is {} and its successor is {}".format(num_int, num_int-1, num_int+1))'''

# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

'''sr = pow(64, (1/2))
print(sr)'''

# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

'''dc = float(input("How many degrees Celsius is it now: "))
converted = (dc*9)/5 + 32
print("Temperature in Celsius of {:.1f}ºC converted to fahrenheit is {:.1f}ºF.".format(dc, converted))'''

# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

'''km_traveled = float(input("What is the distance travel (in Km) for your car ?\n"))
rented_day = float(input("How many day do you have rented your car for ?\n"))
rent_value = (km_traveled * 0.15) + (rented_day * 60)
print("You have traveled for {:.2f} Km, during a period of {} day, "
      "so the value total of your rent was R$ {:.2f}.".format(km_traveled, rented_day, rent_value))'''

# AULA 08

'''import math
num = float(input("Type a number: "))
sqrt = math.sqrt(num)'''

'''if(num == float(2)):
    ceil = math.ceil(num)
    sqrt = math.sqrt(num)
    print(ceil, "e", sqrt)
else:
    print("Square root is {}".format(math.sqrt(num)))'''

'''if(sqrt % 2 == 0 or sqrt % 2 == 1):
    print("The square root of {:.0f} is {:.0f}.".format(num, sqrt))
else:
    print("The square root of {:.2f} is {:.2f}.".format(num, sqrt))'''

'''from math import lcm, floor
aa = float(input("Type here a number: "))
bb = pow(aa, (1/2))
# a = lcm(bb)
b = floor(bb)
print(bb)
print("e", b)
# c = pow(aa, (1/2))
# print("e", b, "e", "{:.2f}.".format(c))
# print(c)
# print("the value is {:.2f}.".format(c))'''

'''import random
num = random.randint(0, 25)
print(num)'''

'''import emoji
print(emoji.emojize("Olá mundo :sungglasses: ", use_aliases=True))'''

# Coding: UTF-8

# challenge 16


'''radius = float(input("Type here a number for radius of the circle: "))
pi = math.pi
print("The value of π is {}.".format(pi))
c = radius*2*pi
print("So the value of circumference is {} ".format(c))
numInt = c/(2*radius)
# numInt = int(numFlo)
# ardPi = int(numInt)
# ardPi = math.trunc(numInt)
ardPi = numInt
print("The float number made by a calculation and converted to an entire number is {}.".format(int(ardPi)))'''

# challenge 17

# from math import hypot

'''catOp = float(input("Type here the opposite side of hypotenuse: "))
catAd = float(input("Type here the adjacent side of hypotenuse: "))
cal = catAd**2 + catOp**2
# hip = pow(cal, (1/2))
hip = math.hypot(catOp, catAd)
# hip = hypot(catOp, catAd)
print("The value of hypotenuse from {} (in opposite side) and {} (in adjacent side) is {:.2f}.".format(catOp, catAd, hip))'''

# challenge 18 -

'''catOp = float(input("Type here the opposite side of hypotenuse: "))
catAd = float(input("Type here the adjacent side of hypotenuse: "))
cal = catAd**2 + catOp**2
hip = pow(cal, (1/2))
print("The value of hypotenuse from {} (in opposite side) and {} (in adjacent side) is {}.".format(catOp, catAd, hip))
deg = float(input("Enter with a degree to calculate its sin, cos and tangent: "))
print("The value of sin of the degree {} is {}".format(deg, math.sin(deg)))
sin = catOp / hip
resultSin= math.sin(sin)
print("The value of sin is {}.".format(resultSin))
cos = catAd / hip
resultCos = math.cos(cos)
print("The value of cos is {}.".format(resultCos))
tang = catOp / catAd
resultTang = math.tan(tang)
print("The value of tangent is {}".format(resultTang))'''
# import math

# from math import cos, radians, sin, tan

'''degree2 = int(input("Enter with a degree to calculate its sin, cos and tangent:"))
# degree = math.radians(degree2)
a = math.sin(math.radians(degree2))
b = math.cos(math.radians(degree2))
c = math.tan(math.radians(degree2))
print("The value of sin is {:.2f}, cos is {:.2f} and tangent is {:.2f}".format(a, b, c))'''

# students = list[input("Enter here with the names of students: ")]
'''from random import choice

student1 = str((input("Enter with the name of the first student (number 1): ")))
student2 = str((input("Enter with the name of the second student (number 2): ")))
student3 = str((input("Enter with the name of the third student (number 3): ")))
student4 = str((input("Enter with the name of the fourth student (number 4): ")))

lista = [student4, student3, student2, student1]
chosen = choice(lista)
print("The student chosen was: {}".format(chosen))'''

'''student1 = 1
student2 = 2
student3 = 3
student4 = 4

lucky = random.randint(student1, student4)  # input("Enter here with the names of students: "))
print("Lucky student was: {}".format(lucky))'''

# challenge 19

'''from random import shuffle
a = input("Enter here with the name of the fist group: ")
b = input("Enter here with the name of the second group: ")
c = input("Enter here with the name of the third group: ")
d = input("Enter here with the name of the fourth group: ")

list = [a, b, c, d]
shuffle(list)
print("The group chosen was: {}".format(list))'''


'''aa = random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)
bb = random.randint(1, 4)
cc = random.randint(1, 4)
dd = random.randint(1, 4)
print(aa)'''
'''a = int(1)
b = int(2)
c = int(3)
d = int(4)'''

'''for e in random.randrange(aa, dd, 1):
    print("The first group to presentation is: {}.".format(e))
    print("The second group to presentation is: {}.".format(e))
    print("The third group to presentation is: {}.".format(e))
    print("The fourth group to presentation is: {}.".format(e))'''

# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


'''import pygame
import os
pygame.init()
if(os.path.exists("Track 06.mp3")):
    # pygame.mixer.init()
    pygame.mixer.music.load("Track 06.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while(pygame.mixer.music.get_busy()):
        pygame.event.poll()
        clock.tick(10)
else:
    print("File is not encountered in the paste!")'''

'''import playsound
playsound.playsound("Track01")'''

# Aula 09

# name = "johnny gabriel pereira marcelino"
# dict(name)
# print(name, 0)
'''name = "Johnny gabriel pereira marcelino"
print(name)
print(len(name))
print(len(name[4:15]))
print(name.count("p"))
print(name.count("o", 0, 31))
print(name.find("mar"))
print(name.find("hello"))  # Not encountered return -1

a = "johnny" in name
print(a)

b = name.replace("pereira", "style")
print(b)

all_upper = name.upper()
print(all_upper)
all_lower = name.lower()
print(all_lower)

cap = name.capitalize()
print(cap)
titl = name.title()
print(titl)

name1 = "   maria de fatima  "
print(name1)
c = name1.strip()
print(c)
d = c.title()
print(d)
print(name1)
print(name1.rstrip())
print(name1.lstrip())

nameMy = "Johnny gabriel pereira marcelino"
print(nameMy.split())
print("".join(nameMy))'''

'''n = "Johnny gabriel pereira marcelino   "
print(n.upper().count("P"))
print(len(n.strip("o")))
print(n.strip("Johnny "))
print(n.replace("e", "o"))

print(n[n.count("o")])
print(n.count("o"))
an = n.replace("Johnny", "jorge")
print(an)
print("johnny" in n)
print(n.lower().find("johnny"))
cut = n.rstrip()
list = cut.split()
print(list[2][4])'''

# challenges

# Challenge 22

'''name = str(input("Enter here with your full name: "))
print(name)
print("Your name in uppercase is {}".format(name.upper()))
print("Your name in lowercase is {}".format(name.lower()))
print("Your name have {} lyrics".format(len(name.replace(" ", ""))))
name1 = name.split()
print(len(name1[0]))
print(len(list(name)))'''

# Challenge 23

# Mathmaticsy

'''number = int(input("Enter with a number between 0 and 99999: "))
rn = number.split()
print(rn[1])

u = number // 1 % 10
t = number // 10 % 10
h = number // 100 % 10
th = number // 1000 % 10

print("Your unit is {}".format(u))
print("Your tens is {}".format(t))
print("Your hundreds is {}".format(h))
print("Your thousands is {}".format(th))'''

'''split_number = number.__str__()
number_list = split_number.split()
# print(number_list[0][1])
print("Number represented as unit is {}, as tens is {}, as hundreds is {}, "
      "as thousands is {} and unit of thousands is {}"
      .format(number_list[0][4], number_list[0][3], number_list[0][2], number_list[0][1], number_list[0][0]))'''


'''total = split_number.replace("","-")
total1 = total.rstrip("-")
total2 = total1.lstrip("-")
# total2 = int()
print("Number represented as unit is {}, as tens is {}, as hundreds is {}, as thousands is {} "
      "and unit of thousands is {}".format(total2[5], total2[4], total2[3],total2[2], total2[1]))'''
# print(total2[0])

# Challenge 24

'''cidade = input("What city do you live? :")
# cidade1 = input("What was your last city did you live?")
upper = cidade.upper()
inSant = upper.split()
sant = inSant[0]
haveSant = "SANTO" in sant
print("Whether 'Santo' was into in your first city name, the value 'False' = 'Not', "
      "and 'True' = 'Yes', then this answered: \n{}!".format(haveSant))'''


# temSanto = "Santo" in cidade
# print("If 'Santo' was into in your city, the value 'False' = 'Not', and 'True' = 'Yes', then this answered: {}".format(temSanto))

# Challenge 25

'''name = input("Enter here with your name: ").strip().upper()
in_silva = "SILVA" in name
print("Have your name has 'Silva': {}!".format(in_silva))'''

# Challenge 26

'''enter = str(input("Enter here with any phrase: ")).strip().upper()
print("Total of letters is: {}".format(len(enter)))
print("Letter 'a' was written in the phrase ?: {}".format("A" in enter))
print("What is the first position of the letter 'a' in the phrase: {}".format(enter.find("A")+1))
print("What is the last position of the letter 'a' in the phrase: {}".format(enter.rfind("A")+1))
print("How many times the letter 'a' appears in the phrase: {}".format(enter.count("A")))'''
'''lista = enter.split()
b = lista[-1]
count = b.count("A")
print(count)'''

# print(lista[-1])

# a = len(enter)

# a = enter.count("a")

'''splitA = enter.split()
print(splitA)
print(len(splitA))'''
# print("The last position of the letter 'A' is", len(splitA)])

# countA =
# print(countA)
# a = countA
# print(a)
# print(countA)
# lastA =
# print(enter.find(enter.count("a")))

# Challenge 27

'''fullname = str(input("Enter with your full name: ")).strip().upper()
a = fullname.split()
print("Your first name is {}, and the last name is {}".format(a[0], a[-1]))
print(a[0], a[-1])
# print(a[-1])'''

# AULA 10

'''name = str(input("Enter with your first name: ")).strip().upper()

if(name == "JOHNNY"):
      print("What a beafully name you have! ")

print("Good Morning {}.".format(name))'''

# Challenge 28

'''from  random import randint
from time import sleep
random_number = randint(0, 5)
print("I am going to draw in a number!\nGuess up!")

chosen_number = int(input("Choice a number between 0 to 5, to guess up the number chosen by the program: "))
print("PROCESSING...")
sleep(3)
if(chosen_number == random_number):
    print()
    print("WELL DONE!")
    print()
    print("The number chosen by you was {} and the program number was {}".format(chosen_number, random_number))
    print()
    print("Congrats! You have just guessed up the number chosen by the program!")
else:
    print()
    print("GAME OVER")
    print()
    print("The number chosen by you was {} and the program number was {}".format(chosen_number, random_number))
    print()
    print("I'm sorry! You do not guessed the number up!")
    print()
    print("Try the next time!")'''

# Coding: UTF-8

# Challenge 29

'''car_speed = int(input("Whats is the speed of your car in Km: "))
limit_speed = 79
if(car_speed >= 80):
    traffic_value = (7 * (car_speed - 79))
    print("You were penalized!")
    print("The speed of your car is {} Km/h and the speed limit in this highway is {} Km/h!".format(car_speed, limit_speed))
    print("So you committed a traffic violation!")
    print("The value of your traffic violation exceeded is {:.2f} R$!".format(traffic_value))
else:
    print("You were not penalized!\nHave a good day!")
    print("The speed limit in this highway is {} Km/h and you were in a speed of {} Km/h!".format(limit_speed, car_speed))'''

# Challenge 30

'''num = int(input("Choice a number: "))
if(num % 2 == 1):
    print("The number chosen is odd")
else:
    print("The number chosen is even!")'''

# Challenge 31

'''travel = float(input("What is the distance of your trip in Km ? "))
limit_trip = 200
if(travel <= limit_trip):
    ticket_trip = 0.50
    print("The value of your trip is {:.2f} R$".format(ticket_trip*travel))
else:
    ticket1_trip = 0.45
    print("The value of your trip is {:.2f} R$".format(ticket1_trip*travel))'''

# Challenge 32
'''from datetime import date

year = int(input("Witch are your year? Choice the number 0 to choose the current year: "))
# year // 4
if(year == 0):
    year = date.today().year
if(year % 4 == 0 and year % 100 != 0 and year % 400 != 0):
    print("This is a leap year {}!".format(year))
else:
    print("This in not a leap year {}!".format(year))'''

# Challenge 33

'''num1 = float(input("Choice the first number: "))
num2 = float(input("Choice the second number: "))
num3 = float(input("Choice the third number: "))

if(num1 > num2 and num1 > num3):
    print("The number {} is upper than {} and {}".format(num1, num2, num3))
else:
    if (num2 > num1 and num2 > num3):
        print("The number {} is upper than {} and {}".format(num2, num1, num3))
    else:
        if (num3 > num1 and num3 > num2):
            print("The number {} is upper than {} and {}".format(num3, num1, num2))
if(num1 == num2 and num1 == num3):
    print("Both numbers are igual!")'''

# Challenge 34

'''current_salary = float(input("How much do you make: "))
limit = 1250
percentage1 = 10/100
percentage2 = 15/100
if(current_salary > limit):
    future_salary = (current_salary * percentage1) + current_salary
    increase = percentage1 * current_salary
    print("You have an increased in your salary of {:.2f} R$, then your new salary is {:.2f} R$".format(increase, future_salary))
else:
    if(current_salary <= limit):
        future_salary = (current_salary * percentage2) + current_salary
        increase = percentage2 * current_salary
        print("You have an increased in your salary of {:.2f} R$, "
              "then your new salary is {:.2f} R$".format(increase, future_salary))'''

# Challenge 35

# precisa-se ser menor do que a soma de todos os outros

'''tr1 = float(input("Enter with your first length of the triangle: "))
tr2 = float(input("Enter with your second length of the triangle: "))
tr3 = float(input("Enter with your third length of the triangle: "))

if(((tr2) + (tr3)) > tr1):
    print("YES!\nThese measures can form a triangle!")
else:
    if (((tr1) + (tr3)) > tr2):
        print("YES!\nThese measures can form a triangle!")
    else:
        if (((tr1) + (tr2)) > tr3):
            print("YES!\nThese measures can form a triangle!")
        else:
            print("NO!\nThese measures can not form a triangle!")'''

# AULA 11

'''colors = input("\033[7;30;44m Enter with your name: \033[m")
print("\033[4;33;47m", colors, "\033[m")
a = 10
b = 20

print("The values are \033[35m{} and  \033[30;44m{}\033[30;44m".format(a, b),"\033[m")

name = input("Type your name: ")
print("It's a pleasure to meet you, {}{}{}!".format("\033[4;34m", name, "\033[m"))'''

# AULA 12

'''if():
elif():
else:'''

# CHALLENGE 36

'''house_price = float(input("How much is it the house ? "))
salary_wisher = float(input("How much do you make for month ? "))
years_payment = int(input("How many years will you pay the house for ? "))
payment_request = (house_price / years_payment) / 12
# print(payment_request)
total = (payment_request * (30 / 100)) + payment_request
# month_payment = salary_wisher * 30/100

if(salary_wisher > total):
    print("I am sorry! Your request was recused!")
    print("Your salary is lower than requested!", end=" ")
    print("The value of the times is {:.2f}".format(payment_request))
else:
    if(salary_wisher <= total):
        print("Congrats!!!")
        print("Your request was allowed!!!", end=" ")
        print("The value of the times is {:.2f}".format(payment_request))'''

# CHALLENGE 37

'''chosen = int(input("Enter with any number would you like to convert: "))
convert = int(input(''' '''What system would you like to convert the number {} ?
Type: '1' for binary system
Type: '2' for octal system
Type: '3' for hexadecimal system: ''' #.format(chosen)))

'''if(convert == 1):
    print("The number {} converted to binary system is {}!".format(chosen, bin(chosen)[2:]))
elif(convert == 2):
    print("The number {} converted to octal system is {}!".format(chosen, oct(chosen)[2:]))
elif(convert == 3):
    print("The number {} converted to hexadecimal system is {}!".format(chosen, hex(chosen)[2:]))
else:
    print("Option does not available!")'''

# ascii(4)
# print(ascii())
# print(bin(7))

# CHALLENGE 38

'''chosen = int(input("Enter with the first number: "))
chosen1 = int(input("Enter with the second number: "))

if(chosen > chosen1):
    print("The first value {} is greater than the second value {}!".format(chosen, chosen1))
elif(chosen1 > chosen):
    print("The second value {} is greater than the first value {}!".format(chosen1, chosen))
else:
    print("Both values {} and {}, are equals!".format(chosen, chosen1))'''

# CHALLENGE 39

'''from datetime import date

current = date.today().year
birth_age = int(input("Which year did you birth ? "))
enlist = current - birth_age

if(birth_age < enlist):
    print("You are not already to enlist for while!")
    print("It's left {} years for you enlist".format((current - birth_age) - 18))
elif(birth_age == enlist):
    print("This age mean you are already to enlist!")
elif(birth_age > enlist):
    print("This age overcome the ideal age to enlist!")
    print("It's already passed {} years to enlist!".format((current - birth_age) - 18))'''

# CHALLENGE 40

'''name = str(input("What is your name ? "))
grade = float(input("Whats is your first grade in this semester {} ? ".format(name)))
grade1 = float(input("Whats is your second grade in this semester {} ? ".format(name)))
media = (grade + grade1) / 2
reproved = 5
recovery = 6.9
approved = 7

if(media >= approved):
    print("CONGRATS!")
    print("You have been approved {} !!".format(name))
    print("Your media final in this semester was {}!".format(media))
elif(media >= reproved and media <= recovery):
    print("{}, I hope you study more!".format(name))
    print("You are in recovery!!")
    print("Your media final in this semester was {}!".format(media))
elif(media < reproved):
    print("I AM SORRY {}!!!".format(name))
    print("You have not passed!!!")
    print("Your media final in this semester was {}!".format(media))'''

# CHALLENGE 41
'''from datetime import date

name = str(input("What is your name ? "))
birth_year = int(input("Which year did you birth ? "))
current_year = date.today().year
mirim = 9
infantil = 14
junior = 19
senior = 20
# master = 21
if(current_year - birth_year <= mirim):
    print("You are in the category of 'MIRIM'!!")
    print("You are {} years old!".format(current_year - birth_year))
elif(current_year - birth_year > mirim and current_year - birth_year <= infantil):
    print("You are in the category of 'INFANTIL'!!")
    print("You are {} years old!".format(current_year - birth_year))
elif(current_year - birth_year > infantil and current_year - birth_year <= junior):
    print("You are in the category of 'JUNIOR'!!")
    print("You are {} years old!".format(current_year - birth_year))
elif(current_year - birth_year > junior and current_year - birth_year <= senior):
    print("You are in the category of 'SENIOR'!!")
    print("You are {} years old!".format(current_year - birth_year))
elif(current_year - birth_year > senior):
    print("You are in the category of 'MASTER'!!")
    print("You are {} years old!".format(current_year - birth_year))'''

# CHALLENGE 42

# Coding: UTF-8

'''tr1 = float(input("Enter with your first length of the triangle: "))
tr2 = float(input("Enter with your second length of the triangle: "))
tr3 = float(input("Enter with your third length of the triangle: "))

if((tr2) + (tr3) > tr1 and (tr1) + (tr3) > tr2 and (tr1) + (tr2) > tr3 and tr1 == tr2 == tr3):
    print("YES!\nThese measures can form a triangle!")
    print("This is a equilateral triangle!")
elif((tr2) + (tr3) > tr1 and (tr1) + (tr3) > tr2 and (tr1) + (tr2) > tr3 and tr1 == tr2 or tr3 == tr1 or tr3 == tr2):
    print("YES!\nThese measures can form a triangle!")
    print("This is a isosceles triangle!")
elif((tr2) + (tr3) > tr1 and (tr1) + (tr3) > tr2 and (tr1) + (tr2) > tr3 and tr1 != tr2 != tr3 != tr1):
    print("YES!\nThese measures can form a triangle!")
    print("This is a scalene triangle!")
else:
    print("NO!\nThese measures can not form a triangle!")
'''
# CHALLENGE 43

# massa corpórea

'''weight = float(input("how much do you weight ? \n"))
height = float(input("how tall are you ? \n"))
imc = (weight / (height**2))
print("The MCI of this person is {:.2f}".format(imc))
if((imc) < 18.5):
    print("You are on under weight of {:.2f}!".format(imc))
elif((imc) >= 18.5 and imc <= 25):
    print("You are on ideal weight of {:.2f}!".format(imc))
elif((imc) > 25 and imc <= 30):
    print("You are on overweight of {:.2f}!".format(imc))
elif((imc) > 30 and imc <= 40):
    print("You are on obesity of {:.2f}!".format(imc))
elif((imc) > 40):
    print("You are on morbid obesity of {:.2f}!".format(imc))'''

# CHALLENGE 44

'''print("{:*^40}".format(" lojas johnny!! "))
print("How will you pay this product ? ")
product_price = int(input("How much was your things ? "))
# question_condition = float(input("How will you pay this product ? "))
pay_condition = str(input("For cash payment type: 'CT', for check payment type: 'CA', for credit card type: 'CC', "
                    "for on credit card 2X type: 'C2' and for on credit card 3X type: 'C3'! ")).strip().upper()
ct = product_price - (product_price * 10/100)
ca = product_price
cc = product_price + (product_price * 5/100)
c2 = product_price + (product_price * 10/100)
c3 = product_price + (product_price * 20/100)'''

'''while(pay_condition != "CT" and pay_condition != "CA" and pay_condition != "CC" and pay_condition != "C2" and pay_condition != "C3"):
    pay_condition = str(input("For cash payment type: 'CT', for check payment type: 'CA', for credit card type: 'CC', "
                              "for on credit card 2X type: 'C2' and for on credit card 3X type: 'C3'! ")).strip().upper()
    ct = product_price - (product_price * 10 / 100)
    ca = product_price
    cc = product_price + (product_price * 5 / 100)
    c2 = product_price + (product_price * 10 / 100)
    c3 = product_price + (product_price * 15 / 100)
    print("The price of product is {} reais".format(product_price))'''
'''if(pay_condition == "CT"):
    print("You have a discount of {:.2f} R$, so you have to pay by this product {:.2f}!".format(product_price * 10/100, ct))
elif(pay_condition == "CA"):
    print("You don't have a discount on this product, so you have to pay by this product {:.2f}!".format(ca))
elif(pay_condition == "CC"):
    print("You have a increased of {:.2f} R$ on the price product, so you have to pay by "
          "this product {:.2f}!".format(product_price * 5/100, cc))
elif(pay_condition == "C2"):
    print("You have a increased of {:.2f} R$ on the price product, so you have to pay by "
          "this product {:.2f}!".format(product_price * 10/100, c2))
elif(pay_condition == "C3"):
    print("You have a increased of {:.2f} R$ on the price product, so you have to pay by "
          "this product {:.2f}!".format(product_price * 15/100, c3))
else:
    # print(pay_condition != ("CT" or "CA" or "CC" or "C2" or "C3"))
    print("I am a legend")'''


# CHALLENGE 45

'''from random import randint
from time import sleep

itens = ("STONE", "PAPER", "SCISSOR")
machine = randint(0, 2)
print(''' '''Your choices are:
[ 0 ] STONE
[ 1 ] PAPER
[ 2 ] SCISSOR)'''
'''user = int(input("What is your choice to play with the machine!\n"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print("="*30)
print("You have chosen {}".format(itens[user]))
print("Computer have chosen {}".format(itens[machine]))
print("="*30)'''




'''choice = str(input("Choose '0' for stone, '1' for paper or '2' for scissor to play with the machine! "))
machine = random.randint(0, 2)
# print(machine)
computer = str(machine)
# print(computer)

stone = '0'
paper = '1'
scissor = '2'''

'''if(user == machine):
    print("Computer have chosen {}".format(machine))
    print("You have chosen {}".format(user))
    print("The game tied!")
elif(user == "0" and machine == '1' and user == "1" and machine == '2' and user == "1" and machine == '0'):
    print("Computer have chosen {}".format(machine))
    print("You have chosen {}".format(user))
    print("YOU DEFEATED!\nTHE COMPUTER WIN!")
elif(machine == "1" and user == '0' and machine == "2" and user == '1' and machine == "0" and user == '1'):
    print("Computer have chosen {}".format(machine))
    print("You have chosen{}".format(user))
    print("CONGRATS!!\nYOU WIN!")'''

# AULA 13

# CHALLENGE 46
# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

'''from emoji import emojize
from time import sleep

print()
print("="*10, " COUNTDOWN FOR NEW YEAR!!! ", "="*10)
print(emojize('👍'*12 + '👍'*12))
print()
for c in range(10, 0-1, -1):
    print("="*5, c, "="*5)
    sleep(1)
print()
sleep(1)
print(emojize("\U0001f386"*35))
sleep(1)
print("="*20, "HAPPY NEW YEAR!!!", "="*20)
sleep(1)
print(emojize("\U0001f386"*35))
sleep(1)'''


# CHALLENGE 47
# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

'''for par in range(2, 50+1, 2):
    print(".", end="")
    if(par % 2 == 0):
        print(par, end='')'''

# CHALLENGE 48
# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

'''tm = 0
count = 0
countAll = 0
# so = 0
for so in range(1, 500+1, 2):
    if(so % 3 == 0):
        print(so, end=" ")
        # print(so)
        # tm = so + so
        tm = so + tm
        count += 1
    countAll += 1
        # tm = so + so
print()
print(count, "E", countAll)
print("The sum total of all numbers was:", tm)'''

# print(so)
# tm = so
# else:
# if(so % 2 == 0):
# print("This is what we not want!")
# print(so)
# print("The sum total of numbers multiple 3 is {:.0f}!".format(tm))



'''print("== new codes =="*5)
print("This is 'SO'!", so)
if(so % 2 == 0):
    print(so)
else:
    if(so % 2 == 1):
        # print("Excellent!!")
        print("="*5, so)
        so += so
        print(so)
        tm = so
print("The sum total of odd numbers multiples is {}".format(tm))'''

'''for si in range(so, so, 2):
    print("="*5, "This is 'SI'!", si)
    # print("="*5, si)
    tm = si + si
print("The sum total of odd numbers multiples is {}".format(tm))'''
'''    if(so % 2 == 0):
        so += so
        ts = so
        print(ts)
print("The sum total of odd numbers multiples is {}".format(to))'''

# CHALLENGE 49
# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

'''from time import sleep

numberMult = int(input("Which number would you like to make a multiplication table: "))
untill = int(input("Enter with a number to break the multiplication: "))
print("Multiplication Table of {}".format(numberMult))
for mul in range(0, untill+1, 1):
    sleep(1)
    print(numberMult, "X", mul,  "=", mul*numberMult)'''

# CHALLENGE 50
# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

'''n1 = int(input("Enter with the first number: "))
n2 = int(input("Enter with the second number: "))
n3 = int(input("Enter with the third number: "))
n4 = int(input("Enter with the fourth number: "))
n5 = int(input("Enter with the fifth number: "))
n6 = int(input("Enter with the sixth number: "))'''
# even = 0
'''n2 = 0
count = 0
for even in range(0, 6+1, 1):
    n1 = int(input("Enter with the first number: "))
    if(n1 % 2 == 0):
        n2 = n1 + n2
        count += 1
        print(n2)
print('sum is', n2, 'and the total is', count)'''

# CHALLENGE 51
# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

'''term = int(input("Enter with the first term: "))
r = int(input("Enter with the reason: "))

for pa in range(term, term + (r*10), r):
    print(pa)'''

# CHALLENGE 52
# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

'''a = int(input("Type any integer number: "))
c = 0
count = 0
for b in range(1, a+1, 1):
    print("{}".format(b), end=" ")
    if(a % b == 0):
        c = c + 1
        count = count + 1
        # print("\033[35m")
    else:
        if(a % b == 0):
            count = count + 1
            # print("\033[31m")
if(c == 2):
    # print("\n")
    print(f"\n{a}! YES!!\nIt is a prim number!\n{a} is divided for {count} times")
else:
    print(f"\n{a}! NOT!\nIt is not a prim number!\n{a} is divided for {count} times\nAnd they are {c}")'''


# CHALLENGE 53
# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA,| A SACADA DA CASA,| A TORRE DA DERROTA,| O LOBO AMA O BOLO,| ANOTARAM A DATA DA MARATONA.

'''a = str(input("Type any phrase: ")).strip().upper()
b = a.replace(" ", "")  # or we can use the class ''.JOIN(xyz)
c = len(b)
print(b[::-1])
print(b)
# print(c)
# print(b)

if(b == b[::-1]):
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")'''

# for letra in range(len(variable), -1, -1):

# ////////////////////////////////////////////

# wrongs made

'''for e in range(0, c+1, 1):
    print(d)
    if(d == c):

        print("They are the same!")
'''
# for b in range(a):


# criar uma lista para representar até qual vai a ultima letra!!

# CHALLENGE 54
# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''from datetime import date

notAdult = 0
adult = 0
for age in range(1, 7+1, 1):
    name = int(input("You are the {}º\nWhich year did you born ? ".format(age)))
    if(date.today().year - name >= 21):
        # print("You're an adult!")
        adult = adult + 1
        print("IS ADULT!", adult)
    else:
        # print("You're not an adult!")
        notAdult += 1
        print("NOT ADULT!", notAdult)

print("The amount of adult is {:.0f}!".format(adult))
print("The amount of not adult is {:.0f}!".format(notAdult))'''

# CHALLENGE 55
# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

'''major = 0
c = 0
# d1 = 100000
d = 0
for a in range(0, 5):
    b = float(input("How many pounds do you weight ? "))
    if(b > c):
        c = b
        d = b
    else:
        if(b < d):
            c = b
        if(b > c):
            d = b
        # if(c > b+1):
        #     d = c

print("The bigger weight was {}Kg!".format(c))
print("The less weight was {}Kg!".format(d))'''


# CHALLENGE 56
# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

'''b = 0
d = 20
e = 0
f = 0
peaple = 4
for a in range(0, peaple):
    name = str(input("What is your name ? ")).strip().upper()
    age = int(input("How old are you ? "))
    sex = str(input("What is your sex ? Type 'm' for male or 'f' for female: ")).strip().upper()
    print("="*20)
    print("NAME: {}".format(name))
    print("AGE: {}".format(age))
    print("SEX: {}".format(sex))
    print("="*20)
    f = age + f
    if(age > b):  # and sex == "male")  # if('M' in 'Mm' and sex blablabla):
        if(sex == "M"):
            b = age
            n = name
    else:
        if(age < d):  # if('F' in 'Ff' and sex blablabla):
            if(sex == "F"):
                e += 1
ma = f / peaple
print("The age media of this group is {}!".format(ma))
print("The older man name is {} with {}!".format(n, b))
print("The amount of women in this group with age less than 20 years old is {}!".format(e))'''