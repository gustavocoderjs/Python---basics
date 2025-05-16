

conjunto = { "python", "java", "python" } 

print(conjunto)

# Conjuntos em python não suportam indexação e nem fatiamento, caso queira acessar
# os seus valores é necessário converter o conjunto para uma lista 

conjuntoDois = list(conjunto)
print(conjuntoDois[0])

# A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for 

carros = {'gol', 'celta', 'hb20', 'fiesta'}

for carro in carros: 
    print(carro)
    
    
for indice, carro in enumerate(carros): 
    print(f'{indice}: {carro}')
    
conjuntoA = {1, 2}
conjuntoB = {9, 0}

print(conjuntoA.union(conjuntoB))

print(conjuntoA.difference(conjuntoB))

print(conjuntoA.symmetric_difference(conjuntoB))

print(conjuntoA.issubset(conjuntoB))

# .clear(): esvazia o conjunto 
# .copy(): copia o conjunto 
# .discard(): remove o valor informado do conjunto 
# .pop(): remove o primeiro valor da frente 
# .remove(): remove o valor informado 
# len: tamanho do conjunto 
# in: verifica se o elemento é um objeto e está dentro de um conjunto

numeros = { 44, 55, 77 ,99 }

print(99 in numeros) # True 



