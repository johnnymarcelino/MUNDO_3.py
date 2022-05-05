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
# print(f"Portanto a sua média geral é de {media/materias}")
# # for media in nota:
# #     print("Portanto, a sua médi {}")
