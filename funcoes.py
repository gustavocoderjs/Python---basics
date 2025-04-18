



def exibir_mensagem():
    print ("Mensagem exibida com sucesso!")
    
exibir_mensagem()

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor(numero):
    antecessor = numero - 1 
    sucessor = numero + 1 
    return antecessor, sucessor 

print(calcular_total([10, 20, 35]))
print(retorna_antecessor(10))



