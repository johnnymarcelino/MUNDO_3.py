'''def fizzBuzz(n):
    if(n % 3 == 0):            # Write your code here
        print()

# if __name__ == '__main__':
fizzBuzz(int(input("Number: ")))
'''

'''def fizzBuzz(n):
    if (n % 3 == 0):  # Write your code heres
        print("Fizz")
    elif (n % 5 == 0):
        print("Buzz")
    elif (n % 3 == 0 and n % 5 == 0):
        print("FizzBuzz")
    else:
        print(n)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)'''

import math
import random
import os
import re
import sys


# coleção de filmes -> quantidade não informada
# duração dos filmes -> duracoes[n] / 'n' = number of movie
# each movie take between 1.01 to 3.00 hours
# per day 3.00 hours in the max
# [2.4, 1.04, 2.49, 3.0, 1.75]
# [2.4, 1.5, 2.49, 3.0, 2.2]

def acharMinimoDeDias(duracoes):
    # Write your code here
    count = 0
    sum = 0
    print(duracoes)
    for each in duracoes:
        for each2 in range(0, len(duracoes)):
            if((each + duracoes[each2]) <= 3.00):
                sum += each
                print(f"This is the each! {sum:.2f}")
            else:
                sum += 1
    sum = sum / 3
    if(sum < 1):
        print(f"This is the each 2! {1:.2f}")
    else:
        print(f"This is the each 2! {sum:.2f}")
    # for key, value in enumerate(duracoes):
    #     if(value == 3.00):
    #         count += 1
    #     elif(value < 3.00):
    #         count += 1
    #         if(value + duracoes[key] <= 3.00):
    #             count += 1
    #         elif()


if __name__ == '__main__':
    fptr = sys.stdout
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # print(fptr, "FPTR")

    duracoes_count = int(input("Type a something: ").strip())
    # print(duracoes_count, "The first duracoes count")

    duracoes = []
    # print(duracoes, "The first duracoes list")

    for _ in range(duracoes_count):
        duracoes_item = float(input().strip())
        duracoes.append(duracoes_item)
        # print("duracoes_item", duracoes_item)
        # print("duracoes.apppend(duracoes)", duracoes_item)

    result = acharMinimoDeDias(duracoes)

    fptr.write(str(result) + '\n')
    # print(fptr, "This is the first")

    fptr.close()


# print(result)