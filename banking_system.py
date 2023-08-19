DEPOSIT, WITHDRAW, EXTRACT, EXIT = "d", "s", "e", "q"
MAX_WITHDRAW = 500.00
CONTINUE_MESSAGE = "\nPressione Enter para continuar"

balance = 0
deposits = []
withdrawals = []

title_menu = " RL Bank ".center(30, "#")

menu = f"""
{title_menu}

  Informe a operação desejada: 

  {EXTRACT} - Extrato da conta
  {WITHDRAW} - Saque
  {DEPOSIT} - Depósito
  {EXIT} - Sair

"""

operation = ""

while operation.lower() != EXIT:
    print(menu)
    operation = input("Informe a operação desejada: ").lower()

    if operation == DEPOSIT:
        amount = float(input("Informe o valor do depósito: "))
        print()
        if amount <= 0:
            print("Valor não permitido!")
        else:
            balance += amount
            deposits.append(amount)
            print(f"Depósito realizado com sucesso!\nSaldo atual: R$ {balance:.2f}\n")
        input(CONTINUE_MESSAGE)
    elif operation == WITHDRAW:
        amount = float(input("Informe o valor do saque: "))
        print()
        if amount > MAX_WITHDRAW:
            print(f"O valor máximo para saque é R$ {MAX_WITHDRAW}")
        elif amount > balance:
            print(f"Saldo insuficiente!\nSaldo atual: R$ {balance}")
        elif amount == 0:
            print("Informe um valor maior que 0!")
        elif withdrawals.__len__() == 3:
            print("Limite diário de saques atingido!")
        else:
            withdrawals.append(amount)
            balance -= amount
            print(f"Saque realizado com sucesso!\nSaldo atual: R$ {balance:.2f}\n")
        input(CONTINUE_MESSAGE)
    elif operation == EXTRACT:
        print()
        print(" Extrato da conta ".center(30, "*"))
        print()
        if (withdrawals.__len__() == 0 and deposits.__len__() == 0):
            print("Não foram realizadas movimentações.".center(30))
        else:
            print("  Depósitos")
            for deposit in deposits:
                print(f"    R$ {deposit:.2f}")
            
            print("  Saques")
            for withdraw in withdrawals:
                print(f"    R$ {withdraw:.2f}")

            print(f"\n\n  Saldo Atual: R$ {balance:.2f}")
        input(CONTINUE_MESSAGE)
    elif operation != EXIT:
        print("\nOpção inválida!")
        input(CONTINUE_MESSAGE)
    else:
        print("\nFinalizando o sistema...")
