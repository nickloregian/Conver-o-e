
unidades = ['Bit', 'Byte','Kb', 'Mb', 'Gb', 'Tb', 'Pb']
unidadeinicial = input("unidade inicial:")
unidadefinal = input("unidade final:")
valor = int(input())
posiçãoinicial = 0
posiçãofinal = 0
unidadebit = 'bit'

if unidadeinicial == unidadebit:
    valor3 = valor / 8
    unidadeinicial = "byte"
else:
    valor3 = valor

for i in unidades:
    if i == unidadeinicial:
            posiçãoinicial = unidades.index(i)
    if i == unidadefinal: 
            posiçãofinal = unidades.index(i)
variavel = posiçãofinal-posiçãoinicial
valor2= 1024**variavel
valor3= valor3/valor2
    
if unidadefinal == unidadebit:
    if unidadeinicial == "byte":
        valor3 = valor * 8
    else:
        valor3= (valor / 1024)*8
        
print (f"{valor3:.14f}")