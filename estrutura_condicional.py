
saldo = 2000 
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado! ")
else:
    print("Saldo insuficiente! ")

maior_idade = 18 

idade = int(input("Informe sua idade: "))

if idade >= maior_idade: 
    print("Usuário maior de idade, habilitação ok!")
else:
    print("Usuário menor de idade, habilitação recusada")

numero = int(input("Digite um número: "))
mensagem = "Par" if numero % 2 == 0 else "Ímpar" 
print(mensagem) #Saída: Ímpar 