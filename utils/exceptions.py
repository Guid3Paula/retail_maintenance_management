# Define a exceção para orçamento insuficiente
class OrcamentoInsuficienteError(Exception):

    """
    Exceção levantada quando o custo de uma manutenção
    excede o orçamento disponível.
    """

    # Construtor da exceção
    def __init__(
        self,
        orcamento_atual,
        valor_custo,
        mensagem="Orçamento insuficiente para registrar o custo."
    ):

        # Orçamento disponível no momento do erro
        self.orcamento_atual = orcamento_atual

        # Valor do custo que tentou ser registrado
        self.valor_custo = valor_custo

        # Mensagem detalhada de erro
        self.mensagem = (
            f"{mensagem} "
            f"Orçamento disponível: R${orcamento_atual:.2f}, "
            f"Custo solicitado: R${valor_custo:.2f}"
        )

        # Chama o construtor da classe Exception com a mensagem
        super().__init__(self.mensagem)


# Define a exceção para ordens de manutenção inexistentes
class OrdemManutencaoInexistenteError(Exception):

    """
    Exceção levantada ao tentar acessar uma ordem
    de manutenção que não existe.
    """

    # Construtor da exceção
    def __init__(
        self,
        id_ordem,
        mensagem="A ordem de manutenção especificada não foi encontrada."
    ):

        # ID da ordem que não foi encontrada
        self.id_ordem = id_ordem

        # Mensagem detalhada de erro
        self.mensagem = (
            f"{mensagem} "
            f"ID da ordem: {id_ordem}"
        )

        # Chama o construtor da classe Exception com a mensagem
        super().__init__(self.mensagem)