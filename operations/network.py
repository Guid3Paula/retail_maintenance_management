




# Define a Rede de Supermercados
class RedeSupermercados:

    """
    Classe que gerencia as operações de manutenção da rede de supermercados.
    Demonstra Composição, pois "tem" lojas e ordens de manutenção.
    """

    # Construtor da classe RedeSupermercados
    def __init__(self, nome: str):

        # Nome da rede de supermercados
        self.nome = nome

        # Dicionário de lojas (chave: ID da loja, valor: objeto Loja)
        self._lojas = {}

        # Dicionário de Ordens de Manutenção (chave: ID da Ordem, Valor: Objeto OrdemManutencao)
        self._ordens_manutencao = {}

    # Método para adicionar uma nova loja à rede
    def adicionar_loja(self, nome: str, id_loja: str) -> Loja:

        """Criar e adiciona uma nova loja à rede de supermercados."""

        # Verifica se já existe loja com o mesmo ID
        if id_loja in self._lojas:
            print("Erro: Loja com este ID já cadastrada.")
            return self._lojas[id_loja]

        # Cria objeto Loja e adiciona ao dicionário
        nova_loja = Loja(nome, id_loja)
        self._lojas[id_loja] = nova_loja
        print(f"Loja {nome} adicionada com sucesso!")
        return nova_loja

    # Método para criar uma ordem de manutenção para uma loja
    def criar_ordem_manutencao(self, loja: Loja, tipo: str) -> OrdemManutencao:

        """Cria uma nova ordem de manutenção para uma loja existente."""

        # ID da nova ordem será baseado no total de ordens + 1
        id_ordem = OrdemManutencao.get_total_ordens() + 1

        # Cria ordem de manutenção se o tipo informado for "preventiva"
        if tipo.lower() == 'preventiva':
            nova_ordem = OrdemManutencaoPreventiva(id_ordem, loja)

        # Cria ordem de manutenção se o tipo informado for "corretiva"
        elif tipo.lower() == 'corretiva':
            nova_ordem = OrdemManutencaoCorretiva(id_ordem, loja)

        # Cria ordem de manutenção se o tipo informado for "emergencial"
        elif tipo.lower() == 'emergencial':
            nova_ordem = OrdemManutencaoEmergencial(id_ordem, loja)

        # Caso o tipo não seja válido
        else:
            print("Tipo de ordem inválido. Escolha 'preventiva', 'corretiva' ou 'emergencial'.")
            return None

        # Adiciona a nova ordem ao dicionário de ordens de manutenção
        self._ordens_manutencao[id_ordem] = nova_ordem

        # Associa a ordem de manutenção à loja
        loja.adicionar_ordem_manutencao(nova_ordem)
        print(f"Ordem de manutenção {tipo} nº {id_ordem} criada para a loja {loja.nome}.")
        return nova_ordem

    # Método para buscar uma ordem de manutenção pelo ID
    def buscar_ordem_manutencao(self, id_ordem: int) -> OrdemManutencao:
        
        """Busca uma ordem de manutenção pelo ID."""
        
        # Tenta buscar a ordem de manutenção no dicionário
        ordem = self._ordens_manutencao.get(id_ordem)

        # Se a ordem não for encontrada, exibe uma mensagem de erro
        if not ordem:
            print(f"Erro: Ordem de manutenção com ID {id_ordem} não encontrada.")
            return None
        return ordem