#Menu módulo cliente do projeto caixa eletrônico

import os
from time import sleep

# Funcionando 100%
def cadastrar():
    print('-' * 80)
    print('{:=^80}'.format('CADASTRO'))
    print('-' * 80)
    nome = input("Digite o Nome da Empresa: ")
    cnpj = input("Digite o CNPJ da Empresa: ")
    localizacao = input("Digite Localização da Empresa: ")
    inscricao = input("Digite a Inscrição Estadual da Empresa: ")
    #func = input("Escolher Funcionalidades: S ou N:")
    lista = [nome, cnpj, localizacao, inscricao]
    arquivo = open('{}.txt'.format(nome), 'a')
    arquivo.write('- Nome do Banco/Fintech: {};\n- CNPJ: {};\n- Localização: {};\n- Inscrição Estadual: {}.'
                  .format(lista[0], lista[1], lista[2], lista[3]))
    arquivo.close()
    print('Cadastro(s) Concluído(s)!')
    print('=' * 80)
    sleep(1)
    sn = input('Deseja cadastrar mais algum Banco ou Fintech? [S]/[N]: ').upper().strip()
    while sn != 'N':
        if sn == 'S':
            print('Próximo Cadastro...')
            sleep(1)
            cadastrar()
        else:
            sleep(1)
            print('\033[1;31mOpção inválida! Tente novamente!\033[m')
        sn = input('Você Quer continuar? [S]/[N]: ').upper().strip()
        if sn == 'N':
            sleep(1)
            print('Cadastro(s) Concluído(s)!')
            sleep(1)


def listar():
    from glob import glob  # modulo glob serve para listar os caminhos de arquivos
    print('-' * 80)
    print('{:=^80}'.format('LISTA'))
    print('-' * 80)
    print("Os Bancos e Fintech's disponiveis são:")
    lista = []
    lista = glob('*.txt')

    # Mostra os bancos/fintech's para o usuário
    for c in range(0, len(lista)):
        print(lista[c].replace('.txt', ''))

    # Consulta do usuário
    print('=' * 80)
    con = input("Você quer realizar alguma consulta? "
                "\nPositivo: Digite o nome do Banco/Fintech;"
                "\nNegativo: Digite 'N'."
                "\nSua Escolha: ").strip()
    while con != 'N':
        for c in range(0, len(lista)):
            if con in lista[c]:
                print('=' * 80)
                print('Aqui Estão os dados do seu Banco/Fintech: ')
                arquivo = open('{}.txt'.format(con), 'r')
                listar = arquivo.read()
                arquivo.close()
                sleep(2)
                print(listar)
                sleep(3)
                print('=' * 80)
                break
        print('=' * 80)
        con = input("Deseja realizar mais alguma consulta? "
                    "\nPositivo: Digite o nome do Banco/Fintech;"
                    "\nNegativo: Digite 'N'."
                    "\nSua Escolha: ")
        print('Consulta(s) Efetuada(s)')
        print('=' * 80)


# Falta tudo!
def remover():
    import glob
    print('-') * 80
    print('{:=^80}'.format('REMOÇÃO'))
    print('-' * 80)
    print("Escolha algum dos Bancos e Fintech's abaixo para excluir:")
    for file in glob.glob("*.txt"):
        print(os.path.splitext(file)[0])

# Funcionando 100%
def principal():
    opcao = 0
    while opcao != 4:
        print('-=' * 40)
        print('{:=^80}'.format('MÓDULO CLIENTE'))
        print('-=' * 40)
        sleep(2)
        print('=' * 80)
        print('Bem-vindo(a) ao Caixa Total! Escolha alguma das opções abaixo:')
        print('{:80}'.format('[1] Cadastrar Banco ou Fintech'))
        print('{:80}'.format('[2] Editar Cadastro'))
        print('{:80}'.format('[3] Listar Banco ou Fintech'))
        print('{:80}'.format('[4] Sair do Sistema de Banco'))
        print('=' * 80)
        sleep(3)
        opcao = int(input('{}'.format('Digite a opção desejada: ')))
        print('Você escolheu: [{}] '.format(opcao), end="")

# Funcionando 100%
        if opcao == 1:
            print('Cadastrar Banco ou Fintech')
            sleep(2)
            cadastrar()

        elif opcao == 2:
            print('Editar Cadastro')
            sleep(2)
            print('!Em manutenção!')
            sleep(2)

# Funcionando 100%
        elif opcao == 3:
            print('Listar Banco ou Fintech')
            sleep(2)
            listar()

# Funcionando 100%
        elif opcao == 4:
            print('Sair do Sistema de Banco')
            sleep(2)
            print('Saindo do programa...')
            sleep(1)

# Funcionando 100%
        else:
            sleep(1)
            print('\033[1;31mOpção Inválida! Tente novamente!\033[m')
            sleep(2)
    sleep(2)
    print('Fim do programa!')
principal()

