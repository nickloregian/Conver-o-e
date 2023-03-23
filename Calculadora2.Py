valorpadrão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def gbparamb(valorASerConvertido):
    print('Valor convertido de gb para mb')
    gbCalculado = valorASerConvertido / valorpadrão
    return bytesCalculado

def mbparagb(valorASerConvertido):
    print('Valor convertido de mb para gb')
    bitsCalculado = valorASerConvertido * valorpadrão
    return bitsCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)