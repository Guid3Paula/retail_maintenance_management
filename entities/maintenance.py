# Importa a classe base abstrata e o decorador para métodos abstratos
from abc import ABC, abstractmethod

# Importa a classe datetime para registrar data e hora das movimentações
from datetime import datetime

# Importa exceção personalizada para orçamento insuficiente
from utils.exceptions import OrcamentoInsuficienteError


# Define a classe abstrata OrdemManutencao,
# que serve como base para os diferentes tipos de manutenção
class OrdemManutencao(ABC):

    """
    Classe base abstrata para ordens de manutenção.
    Demonstra Herança e Encapsulamento.
    """

    # Atributo de classe que calcula quantas ordens foram criadas
    _total_ordens = 0

    # Construtor da classe
    def __init__(self, id_ordem: int, loja):

        # ID da ordem de manutenção (atributo protegido)
        self._id_ordem = id_ordem

        # Orçamento disponível para a ordem, inicializado em 0.0
        self._orcamento = 0.0

        # Referência à loja vinculada à ordem de manutenção
        self._loja = loja

        # Lista para armazenar o histórico de movimentações da ordem
        self._historico = []

        # Incrementa o total de ordens criadas
        OrdemManutencao._total_ordens += 1

    # Propriedade para acessar o orçamento de forma controlada
    @property
    def orcamento(self):

        """Getter para o orçamento disponível."""

        return self._orcamento

    # Método de classe para consultar o número total de ordens
    @classmethod
    def get_total_ordens(cls):

        """Método de classe para obter o número total de ordens criadas."""

        return cls._total_ordens

    # Método para adicionar orçamento à ordem de manutenção
    def adicionar_orcamento(self, valor: float):

        """Adiciona orçamento à ordem de manutenção."""

        if valor > 0:

            # Incrementa o orçamento disponível
            self._orcamento += valor

            # Registra a movimentação no histórico
            self._historico.append(
                (
                    datetime.now(),
                    f"Orçamento adicionado: R${valor:.2f}"
                )
            )

            print(
                f"Orçamento de R${valor:.2f} "
                f"adicionado com sucesso."
            )

        else:

            print("Valor de orçamento inválido.")

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def registrar_custo(self, valor: float):

        """
        Método abstrato para registrar um custo de manutenção.
        Deve ser implementado pelas subclasses.
        """

        pass

    # Método para exibir o histórico da ordem de manutenção
    def historico(self):

        """Exibe o histórico da ordem de manutenção."""

        print(
            f"\n--- Ordem de Manutenção Nº {self._id_ordem} ---"
        )

        print(f"Loja: {self._loja.nome}")

        print(
            f"Orçamento disponível: "
            f"R${self._orcamento:.2f}"
        )

        print("Histórico de movimentações:")

        # Caso não haja movimentações registradas
        if not self._historico:
            print("Nenhuma movimentação registrada.")

        # Percorre o histórico e exibe cada movimentação
        for data, movimentacao in self._historico:

            print(
                f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: "
                f"{movimentacao}"
            )

        print("--------------------------------------\n")


# Define a subclasse OrdemManutencaoPreventiva
class OrdemManutencaoPreventiva(OrdemManutencao):

    """
    Subclasse que representa uma manutenção preventiva.

    Os custos devem respeitar o orçamento disponível.
    Demonstra Polimorfismo ao sobrescrever registrar_custo.
    """

    # Construtor da manutenção preventiva
    def __init__(self, id_ordem: int, loja):

        # Chama o construtor da classe base
        super().__init__(id_ordem, loja)

    # Implementação do método registrar_custo
    def registrar_custo(self, valor: float):

        """
        Registra custos somente quando existe
        orçamento suficiente.
        """

        if valor <= 0:

            print("Valor de custo inválido.")
            return

        # Verifica se existe orçamento suficiente
        if valor > self._orcamento:

            raise OrcamentoInsuficienteError(
                self._orcamento,
                valor
            )

        # Deduz o custo do orçamento disponível
        self._orcamento -= valor

        # Registra a movimentação no histórico
        self._historico.append(
            (
                datetime.now(),
                f"Custo preventivo: R${valor:.2f}"
            )
        )

        print(
            f"Custo preventivo de R${valor:.2f} "
            f"registrado com sucesso."
        )


# Define a subclasse OrdemManutencaoCorretiva
class OrdemManutencaoCorretiva(OrdemManutencao):

    """
    Subclasse que representa uma manutenção corretiva.

    Permite utilizar o orçamento disponível mais
    um limite de contingência.
    """

    # Construtor com limite padrão de contingência
    def __init__(
        self,
        id_ordem: int,
        loja,
        limite_contingencia: float = 1000.0
    ):

        # Chama o construtor da classe base
        super().__init__(id_ordem, loja)

        # Define o limite adicional para contingências
        self.limite_contingencia = limite_contingencia

    # Implementação do método registrar_custo
    def registrar_custo(self, valor: float):

        """
        Permite registrar custos utilizando o orçamento
        mais o limite de contingência.
        """

        if valor <= 0:

            print("Valor de custo inválido.")
            return

        # Calcula o orçamento total disponível
        orcamento_disponivel = (
            self._orcamento + self.limite_contingencia
        )

        # Verifica se o custo ultrapassa o limite disponível
        if valor > orcamento_disponivel:

            raise OrcamentoInsuficienteError(
                orcamento_disponivel,
                valor,
                "Orçamento e limite de contingência insuficientes."
            )

        # Deduz o custo do orçamento
        self._orcamento -= valor

        # Registra a movimentação no histórico
        self._historico.append(
            (
                datetime.now(),
                f"Custo corretivo: R${valor:.2f}"
            )
        )

        print(
            f"Custo corretivo de R${valor:.2f} "
            f"registrado com sucesso."
        )


# Define a subclasse OrdemManutencaoEmergencial
class OrdemManutencaoEmergencial(OrdemManutencao):

    """
    Subclasse que representa uma manutenção emergencial.

    Possui um limite emergencial adicional,
    permitindo atender ocorrências críticas.
    """

    # Construtor com limite emergencial padrão
    def __init__(
        self,
        id_ordem: int,
        loja,
        limite_emergencial: float = 5000.0
    ):

        # Chama o construtor da classe base
        super().__init__(id_ordem, loja)

        # Define o limite adicional para emergências
        self.limite_emergencial = limite_emergencial

    # Implementação do método registrar_custo
    def registrar_custo(self, valor: float):

        """
        Permite registrar custos utilizando o orçamento
        mais o limite emergencial.
        """

        if valor <= 0:

            print("Valor de custo inválido.")
            return

        # Calcula o orçamento total disponível
        orcamento_disponivel = (
            self._orcamento + self.limite_emergencial
        )

        # Verifica se o custo ultrapassa o limite disponível
        if valor > orcamento_disponivel:

            raise OrcamentoInsuficienteError(
                orcamento_disponivel,
                valor,
                "Orçamento e limite emergencial insuficientes."
            )

        # Deduz o custo do orçamento
        self._orcamento -= valor

        # Registra a movimentação no histórico
        self._historico.append(
            (
                datetime.now(),
                f"Custo emergencial: R${valor:.2f}"
            )
        )

        print(
            f"Custo emergencial de R${valor:.2f} "
            f"registrado com sucesso."
        )