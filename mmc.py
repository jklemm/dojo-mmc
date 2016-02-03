# coding: utf-8


def mmc(valor):
    if valor <= 1:
        raise Exception('O valor {0} não é aceito! Tente um valor maior que 1!'.format(valor)) 
  
    divisor = 2
    retorno = []
    
    while valor != 1:
        if valor % divisor == 0:
            retorno.append(divisor)
            valor = valor / divisor
        else:
            divisor += 1
    return retorno


def escreve_o_mmc(valor):
    resultado = mmc(valor)
    multiplicacoes = ' x '.join(map(str, resultado))
    texto = '{0} = {1}'.format(valor, multiplicacoes)
    return texto
