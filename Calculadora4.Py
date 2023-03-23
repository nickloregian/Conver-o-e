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
    bitsCalculado = valorASerConvertido * valorpadrão
    return bitsCalculado

def gbparatb(valorASerConvertido):
    print('Valor convertido de gb para tb')
    gbCalculado = valorASerConvertido / valorpadrão
    return bytesCalculado

def tbparagb(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * valopadrão
    return bitsCalculado