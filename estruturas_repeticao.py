
i = 1 

while i < 10: 
    print(i)
    i +=1

print("Fim da execução")
print(i)

criancas = ["Manu", "Vini", "Selina"]

for item in criancas:
    print(item)

canal = "Refatorando"

for letra in canal:
    print(letra)
    
for index in range(20):
    print(index)
    
for index in range (len(criancas)):
    print(index)
    

criancas = ["Duda", "Gabriel", "Marcela"]
for index in range (len(criancas)):
    print(criancas[index], index)
    
for index in range(3):
    if index == 0:
        print("primeira linha")
    else:
        print(f"outras linhas {index}")
        
   

matriz_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for linha in matriz_numeros:
    print("---")
    for coluna in linha:
        print(coluna)
        

    