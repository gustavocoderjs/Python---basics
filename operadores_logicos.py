
saldo = 1000
saque = 250
limite = 200 
conta_especial = True

# Na condição AND: para ser True, tudo precisa ser True
# Na condição OR: 
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)

expressao = (saldo >= saque  and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao)

conta_normal_com_saldo = saldo >= saque and saque <= limite
conta_especial_com_saldo = conta_especial and saldo >= saque

expressao_dois = conta_especial_com_saldo or conta_especial_com_saldo
print (expressao_dois)

saldoVendendor = 500
saldoComprador = 200

operacaoSaque = saldoVendendor and saldoComprador >= 500 
print(operacaoSaque)
