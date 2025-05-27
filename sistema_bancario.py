def mostrar_menu():
    """Exibe o menu de opções do sistema bancário"""
    print("\n" + "=" * 20)
    print(" MENU PRINCIPAL ".center(20))
    print("=" * 20)
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Saldo")
    print("4. Extrato")
    print("5. Sair")
    print("=" * 20)

def depositar(saldo, extrato):
    """Realiza um depósito na conta e registra no extrato"""
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: +R$ {valor:.2f}")
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\nErro: O valor do depósito deve ser positivo.")
    
    except ValueError:
        print("\nErro: Valor inválido. Digite um número positivo.")
    
    return saldo, extrato

def sacar(saldo, extrato, saques_realizados):
    """Realiza um saque da conta seguindo as regras estabelecidas"""
    LIMITE_POR_SAQUE = 500
    MAX_SAQUES_DIARIOS = 3
    
    try:
        valor = float(input("Informe o valor do saque: R$ "))
        
        # Verifica as condições para o saque
        if valor <= 0:
            print("\nErro: O valor do saque deve ser positivo.")
        elif valor > LIMITE_POR_SAQUE:
            print(f"\nErro: Limite máximo por saque é R$ {LIMITE_POR_SAQUE:.2f}")
        elif saques_realizados >= MAX_SAQUES_DIARIOS:
            print("\nErro: Limite diário de 3 saques atingido.")
        elif valor > saldo:
            print("\nErro: Saldo insuficiente para realizar o saque.")
        else:
            saldo -= valor
            saques_realizados += 1
            extrato.append(f"Saque:    -R$ {valor:.2f}")
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Saques realizados hoje: {saques_realizados}/{MAX_SAQUES_DIARIOS}")
    
    except ValueError:
        print("\nErro: Valor inválido. Digite um número positivo.")
    
    return saldo, extrato, saques_realizados

def ver_saldo(saldo):
    """Exibe o saldo atual formatado"""
    print("\n" + "=" * 20)
    print(f" SALDO ATUAL ".center(20))
    print("=" * 20)
    print(f"R$ {saldo:.2f}".center(20))
    print("=" * 20)

def mostrar_extrato(extrato, saldo):
    """Exibe o histórico completo de transações e o saldo atual"""
    print("\n" + "=" * 40)
    print(" EXTRATO BANCÁRIO ".center(40))
    print("=" * 40)
    
    if not extrato:
        print("Nenhuma movimentação realizada.".center(40))
    else:
        for movimento in extrato:
            print(movimento)
    
    print("=" * 40)
    print(f"SALDO ATUAL: R$ {saldo:.2f}".center(40))
    print("=" * 40)

def sistema_bancario():
    """Função principal que gerencia o sistema bancário"""
    saldo = 0.0
    extrato = []
    saques_realizados = 0
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, saques_realizados = sacar(saldo, extrato, saques_realizados)
        elif opcao == "3":
            ver_saldo(saldo)
        elif opcao == "4":
            mostrar_extrato(extrato, saldo)
        elif opcao == "5":
            print("\nObrigado por usar nosso sistema bancário. Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 5.")

# Iniciar o sistema bancário
if __name__ == "__main__":
    sistema_bancario()