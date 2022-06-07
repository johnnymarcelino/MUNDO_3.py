def metade(charge):
    # print("="*30)
    # if(troco == "sim"):
    # print("="*30)
    half = charge / 2
    return half

def diminuir(charge, tax):
    # global totalDec
    # global ta
    decrease = charge - charge * (tax/100)
    # def totalDim(charge):
    #     totalDec = charge - decrease
    #     return totalDec, decrease
    # # totalDec = charge - decrease
    return decrease


def dobro(charge):
    double = charge * 2
    return double


def aumentar(charge, tax):
    # global totalInc
    increase = charge + charge * (tax/100)
    # totalInc = charge + increase
    return increase


def moeda(price=0, moeda=False, ):
    if(moeda == True):
        moeda = "R$"
        return f"{moeda}{price}".replace(".", ",")
    else:
        return moeda
