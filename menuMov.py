import os
import time
from transacoes import Transacoes
import functions as fun
from datetime import date

transf = Transacoes(1)


def saldo():
    transf.query()

    print("\nPara imprimir digite -1-")
    print("Para finalizar a consulta digite -2-")
    numero = input("Digite o número: ")
    print()

    while(numero != "1" and numero != "2"):
        print("Digite os números apresentados..")
        escolha = input("Digite o número: ")
        print()

    if(escolha == "1"):
        print("Imprimindo...\n")
        time.sleep(2)


def trans():
    transf.transference()

    ks = input("\nConfirmar a transação (Digite -1- para SIM ou -2- para NÃO)\n")
    while(ks != "1" and ks != "2"):
        ks = input("\nConfirmar transação (Digite -1- para SIM ou -2- para NÃO)\n")

    if(ks == "1"):
        print("Transferência Completa")
        time.sleep(2)
    else:
        print("Retornando para o menu...")
        time.sleep(2)


def extrato():
    print("\n Histórico das operações\n")
    transf.statement()

    input("\nPara voltar ao menu pressione enter")


def principalMOV():
    while True:
        time.sleep(2)
        os.system("cls")
        print("-----------------------------------------")
        print(" === MÓDULO MOVIMENTAÇÃO === ")
        print("\-\ Banco Digital /-/")
        print("1 - Consulte seu extrato")
        print("2 - Realize uma transferência")
        print("3 - Consulte seu saldo")
        print("4 - Sair do Banco")
        escolhe = int(input("Digite o opção desejada:"))
        print("-----------------------------------------")

        if escolhe == 1:
            extrato()
        elif escolhe == 2:
            trans()
        elif escolhe == 3:
            saldo()
        elif escolhe == 4:
            print("Fechando o programa...")
            break
        else:
            print("Opcão invalida, por favor tente novamente.") 