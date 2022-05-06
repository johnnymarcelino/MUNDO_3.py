# bandas = list()
#
# while True:
#     op = int(input("0. Para sair do programa\n"
#                    "1. Adicionar outra banda\n"
#                    "2. Exibir bandas favoritas\n"
#                    "3. Tamanho da lista\n"
#                    "4. Mudar valor de item\n"
#                    "Digite Aqui: "))
#     if(op == 0):
#         break
#     if(op == 1):
#         banda = input("\nDigite o nome da banda: ")
#         bandas.append(banda)
#         print()
#     if(op == 2):
#         print(f"\nAs suas bandas favoritas são: {bandas}")
#         print()
#     if(op == 3):
#         print(f"\nO tamanho da lista é {len(bandas)}")
#         print()
#     if(op == 4):
#         print(f"\nVoce tem {len(bandas)} elementos")
#         banda = int(input("Qual índice voce quer mudar: "))
#         if(banda > len(bandas)-1):
#             print("Esse indice não existe")
#             break
#         elemento = input("Qual voce gostaria de adicionar: ")
#         bandas[banda] = elemento
#         print(f"Elemento {elemento} adicionado com suscesso no indece {bandas.index(elemento)}!")

# squares = [x**2 for x in range(10)]
# print(squares)

# squares = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(squares)

# combs = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if(x != y):
#             combs.append((x, y))
#             print(combs)
# print()
# print(combs)

# value ['3.1', '3.14', '3.142', '3.1416', '3.14159']
# from math import pi
# a = [str(round(pi, i)) for i in range(1, 6)]
# a = []
# for i in range(1, 6+1):
#     a.append(str(round(pi, i)))
# print(a)

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# # print(len(matrix[0]))
# for row in matrix:
#     # print(len(row))
#     for i in range(4):
#         matrix.append([row[i]])
# print(matrix)
# matrix = []
# [[row[i] for row in matrix] for i in range(4)]]

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del(a[0])
# print(a)
# del(a[2:5])
# print(a)

# numeros = []
# for n in range(0, 10):
#     numeros += [n]  # concatenação de listas / numeros transformam-se em listas!
# print(numeros)

# numeros = []
# for n in range(0, 10):
#     numeros += [n]
# print(numeros)
# print()
# soma = 0
# for n in numeros:
#     print(n)
#     soma += n
# print(f"A soma de todos é {soma}")

# numeros = []
# for n in range(1, 10+1):
#     numeros += [n]
# print(numeros)
# print()
# for n in numeros:
#     print(f"O dobro do valor do elemento {n} na lista é {n*2}")

# numeros = []
# for n in range(1, 10+1):
#     numeros.append(n)
# for n in range(len(numeros)):
#     numeros[n] = numeros[n]*2
#     # print(numeros[n])
# print(numeros)
# for n in numeros:
#     print(n)

# numeros = []
# for n in range(1, 10+1):
#     numeros.append(n)
#     print(f"Número {n}: {n}")

# materias = int(input("Quantas materiais voce tem na escola ? "))
# disciplinas = []
# for c in range(materias):
#     disciplinas.append(str(input("Quais são as materias: ")))
# print(f"As suas materias são: {disciplinas}")
# print()
# # print("Dig")
# media = 0
# nota = []
# for notas in disciplinas:
#     valor = float(input(f"Qual foi a sua nota em {notas}: "))
#     nota.append(valor)
#     media += valor
# for b in range(len(nota)):
#     print(f"A sua nota em {disciplinas[b]}: {nota[b]}")
# print(f"Portanto a sua média geral é de {media/materias:.2f}")
# for media in nota:
#     print("Portanto, a sua médi {}")


# print("SEQUENCIA DE FIBONACCI")
#
# numero = int(input("Digite aqui um numero: "))
# termos = []
# for c in range(0, numero):
#     if(c == 0 or c == 1):
#         termos.append(c)
#     else:
#         termos.append(termos[c-1]+termos[c-2])
# print(termos)


# semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
# novaLista = semana[1:5]
# print(novaLista)

# if("Domingo" in semana):
#     print("Sim", 'Domingo', "Está em semana!")
# else:
#     print("Não está!")

# if("Domingo" not in semana):
#     print("True")
# else:
#     print("False")


# list1 = [1, 2, 3, 4]
# # list2 = list1
# # list1[1] = 9
# # # print(list2)
# # list2 = []
# # for item in list1:
# #     list2.append(item)
# # print(list2)
# # list2[1] = 2
# list2 = [] + list1
# list1[3] = 5
# print(list1, "E", list2)


# matriz = [[0 for i in range(3)] for j in range(3)]
# count = 0
# # print(matriz)
# for linha in range(3):
#     for coluna in range(3):
#         matriz[linha][coluna] = count
#         count += 1
# print(matriz)
# print()
# for linha in range(3):
#     for coluna in range(3):
#         print("%4d" % matriz[linha][coluna], end='')
#     print()


# board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# board = [[0 for i in range(3)] for j in range(3)]
# continuar = 1
# jogada = 0
# jogador = jogada % 2 + 1
# while continuar:
#     continuar = int(input("Digite 1 para continuar\n"
#                           "Digite 0 para parar: "))
#     print(board)
#     jogada += 1
# ///////////////////////////////////////////////
# JOGO DA VELHA
# ///////////////////////////////////////////////

# def menu():
#     continuar = 1
#     while continuar:
#         continuar = int(input("0. Sair \n" +
#                               "1. Jogar novamente\n"))
#         if continuar:
#             game()
#         else:
#             print("Saindo...")
#
#
# def game():
#     jogada = 0
#
#     while ganhou() == 0:
#         print("\nJogador ", jogada % 2 + 1)
#         exibe()
#         linha = int(input("\nLinha :"))
#         coluna = int(input("Coluna:"))
#
#         if board[linha - 1][coluna - 1] == 0:
#             if (jogada % 2 + 1) == 1:
#                 board[linha - 1][coluna - 1] = 1
#             else:
#                 board[linha - 1][coluna - 1] = -1
#         else:
#             print("Nao esta vazio")
#             jogada -= 1
#
#         if ganhou():
#             print("Jogador ", jogada % 2 + 1, " ganhou apos ", jogada + 1, " rodadas")
#
#         jogada += 1
#
#
# def ganhou():
#     # checando linhas
#     for i in range(3):
#         soma = board[i][0] + board[i][1] + board[i][2]
#         if soma == 3 or soma == -3:
#             return 1
#
#     # checando colunas
#     for i in range(3):
#         soma = board[0][i] + board[1][i] + board[2][i]
#         if soma == 3 or soma == -3:
#             return 1
#
#     # checando diagonais
#     diagonal1 = board[0][0] + board[1][1] + board[2][2]
#     diagonal2 = board[0][2] + board[1][1] + board[2][0]
#     if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
#         return 1
#
#     return 0
#
#
# def exibe():
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == 0:
#                 print(" _ ", end=' ')
#             elif board[i][j] == 1:
#                 print(" X ", end=' ')
#             elif board[i][j] == -1:
#                 print(" O ", end=' ')
#
#         print()
#
#
# board = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]
#
# menu()


# COMBINAÇÕES DE JOGOS DA MEGA SENA

# total=0
# for dez1 in range(1, 60+1):
#     print(dez1, end=" ")
#     for dez2 in range(dez1+1, 60+1):
#         print(dez2, end=" ")
#     #     for dez3 in range(dez2+1,60):
#     #         # print(dez3)
#     #         for dez4 in range(dez3+1,60):
#     #             # print(dez4)
#     #             for dez5 in range(dez4+1,60):
#     #                 # print(dez5)
#     #                 for dez6 in range(dez5+1,60):
#     #                     print(dez6)
#     total += 1
# print(total)

