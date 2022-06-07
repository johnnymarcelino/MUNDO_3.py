def metade(charge, formato=False):
    '''
    -> Calcula o preço de um determinado preço
    retornando o resultado com ou sem formatoção
    :param charge: O preço que se quer reajustar
    :param formato: Quer a saída formatada ou não?
    :param taxa: Qual é a porcentagem de aumento
    :return: O valor reajustado com ou sem formatação
    '''
    # print("="*30)
    # if(troco == "sim"):
    # print("="*30)
    half = charge / 2
    return half if formato is False else moeda(half)


def diminuir(charge, tax, formato=False):
    # global totalDec
    # global ta
    decrease = charge - charge * (tax/100)
    # def totalDim(charge):
    #     totalDec = charge - decrease
    #     return totalDec, decrease
    # # totalDec = charge - decrease
    return decrease if formato is False else moeda(decrease)


def dobro(charge, formato=False):
    double = charge * 2
    return double if (formato) is False else moeda(double)


def aumentar(charge, tax, formato=False):
    # global totalInc
    increase = charge + charge * (tax/100)
    # totalInc = charge + increase
    return increase if formato is False else moeda(charge)


def moeda(price=0, moeda="R$"):
    # if(moeda == True):
    #     moeda = "R$"
    return f"{moeda}{price:.2f}".replace(".", ",")
    # else:
    #     if (moeda == False):
    #         return moeda


def resumo(price=0, taxaA=10, taxaR=5):
    print("="*30)
    print("RESUMO DO VALOR".center(30))
    print("="*30)
    print(f"Preço analisado: \t{moeda(price)}")
    print(f"Dobro do analisado: {dobro(price):.2f}")
    print(f"Metade do analisado: {metade(price):.2f}")
    print(f"{taxaA}% de aumento: \t{aumentar(price, taxaA, True)}")
    print(f"{taxaR}% de redução: \t{diminuir(price, taxaR, True)}")
    print("="*30)
