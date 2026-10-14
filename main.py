# Importa a classe RedeSupermercados responsável por gerenciar lojas e ordens de manutenção
from operations.network import RedeSupermercados

# Importa exceções personalizadas usadas no fluxo de operações
from utils.exceptions import (OrcamentoInsuficienteError, OrdemManutencaoInexistenteError)

# Função que exibe o menu principal da aplicação
def menu_principal():

    print("\n--- Sistema de Gestão de Manutenção - Rede de Supermercados ---\n")
    print("1. Adicionar Loja")
    print("2. Criar Ordem de Manutenção")
    print("3. Acessar Ordem de Manutenção")
    print("4. Sair\n")

    # Retorna a opção digitada pelo usuário
    return input("Escolha uma opção: ")


# Função que exibe o menu de operações de uma ordem de manutenção específica
def menu_ordem(rede):

    try:

        # Solicita ao usuário o ID da ordem de manutenção
        id_ordem = int(input("Digite o ID da ordem de manutenção: "))

        # Busca a ordem na rede; pode gerar exceção se não existir
        ordem = rede.buscar_ordem_manutencao(id_ordem)

        # Loop de operações dentro da ordem
        while True:

            print(
                f"\n--- Operações para Ordem de Manutenção "
                f"Nº {ordem._id_ordem} ---"
            )

            print(
                f"Loja: {ordem._loja.nome} | "
                f"Orçamento disponível: R${ordem.orcamento:.2f}"
            )

            print("1. Adicionar Orçamento")
            print("2. Registrar Custo")
            print("3. Ver Histórico")
            print("4. Voltar ao Menu Principal")

            # Lê a opção do usuário
            opcao = input("Escolha uma opção: ")

            if opcao == '1':

                # Adiciona orçamento à ordem
                valor = float(
                    input("Digite o valor do orçamento a ser adicionado: ")
                )

                ordem.adicionar_orcamento(valor)

            elif opcao == '2':

                # Tenta registrar um custo de manutenção
                try:

                    valor = float(
                        input("Digite o valor do custo da manutenção: ")
                    )

                    # Polimorfismo:
                    # o comportamento depende do tipo da ordem
                    ordem.registrar_custo(valor)

                except OrcamentoInsuficienteError as e:

                    print(f"Erro na operação: {e}")

            elif opcao == '3':

                # Exibe o histórico da ordem
                ordem.historico()

            elif opcao == '4':

                # Sai do menu da ordem e retorna ao menu principal
                break

            else:

                print("Opção inválida. Tente novamente.")

    # Exceção caso a ordem de manutenção não exista
    except OrdemManutencaoInexistenteError as e:

        print(f"Erro: {e}")

    # Exceção para entradas inválidas
    except ValueError:

        print("Erro: Entrada inválida. Por favor, digite um número.")


# Função principal que controla o fluxo do sistema
def main():

    # Cria o objeto RedeSupermercados
    rede = RedeSupermercados("RedeMax Supermercados")

    # Loop principal do sistema
    while True:

        opcao = menu_principal()

        if opcao == '1':

            # Adiciona uma nova loja
            nome = input("Digite o nome da loja: ")
            id_loja = input("Digite o ID da loja: ")

            rede.adicionar_loja(nome, id_loja)

        elif opcao == '2':

            # Cria uma nova ordem vinculada a uma loja existente
            id_loja = input(
                "Digite o ID da loja para vincular a ordem de manutenção: "
            )

            loja = rede._lojas.get(id_loja)

            if loja:

                tipo = input(
                    "Digite o tipo da manutenção "
                    "(preventiva/corretiva/emergencial): "
                )

                rede.criar_ordem_manutencao(loja, tipo)

            else:

                print(
                    "Loja não encontrada. "
                    "Cadastre a loja primeiro."
                )

        elif opcao == '3':

            # Abre o menu de operações de uma ordem de manutenção
            menu_ordem(rede)

        elif opcao == '4':

            # Encerra o programa
            print(
                "\nObrigado por utilizar o Sistema de Gestão "
                "de Manutenção. Até logo!\n"
            )

            break

        else:

            print(
                "\nOpção inválida. "
                "Por favor, tente novamente.\n"
            )


# Ponto de entrada da aplicação
if __name__ == "__main__":
    main()