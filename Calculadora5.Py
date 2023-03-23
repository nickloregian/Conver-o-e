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
    bytessCalculado = valorASerConvertido * valorpadrão
    return bitsCalculado

def tbparapb(valorASerConvertido):
    print('Valor convertido de tb para pb')
    tbCalculado = valorASerConvertido / valorpadrão
    return bytesCalculado

def pbparatb(valorASerConvertido):
    print('Valor convertido de pb para tb')
    bitsCalculado = valorASerConvertido * valorpadrão
    return bitsCalculado