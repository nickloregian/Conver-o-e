valorpadrão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bytesparakb(valorASerConvertido):
    print('Valor convertido de byte para kb')
    bytesCalculado = valorASerConvertido / valorpadrão
    return bytesCalculado

def kbparamb(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido / valorpadrão
    return bitsCalculado

def mbparagb(valorASerConvertido):
    print('Valor convertido de mb para gb')
    bitsCalculado = valorASerConvertido / valorpadrão
    return bitsCalculado

def gbparatb(valorASerConvertido):
    print('Valor convertido de gb para tb')
    bitsCalculado = valorASerConvertido / valorpadrão
    return bitsCalculado

def tbparapb(valorASerConvertido):
    print('Valor convertido de tb para pb')
    bitsCalculado = valorASerConvertido / valorpadrão
    return bitsCalculado


