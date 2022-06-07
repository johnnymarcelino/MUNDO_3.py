def leiaDinheiro(b):
    valido = False
    while not valido:
        entrada = str(input(b)).replace(",", ".").strip()
        if(entrada.isalpha() or entrada == ""):
            print(f"\033[0;31mERROR! \"{b}\" é preço inválido!\033[m")
        else:
            valido = True
            return float(entrada)



    # if(b.replace(",", ".").isnumeric()):
    #     b = float(b)
    #     moeda.resumo(b)
    # else:
    #     print(f"\033[0;31mERROR! \"{b}\" é preço inválido!\033[m")
    #     p = input("Digite o preço: R$ ")
    #     dados.leiaDinheiro(p)
    #     p = float(p)
    #     moeda.resumo(p)


# a = float(input("Enter with a value: "))
# leiaDinheiro(a)