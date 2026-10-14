# Define a classe da loja
class Loja:

    """
    Classe que representa uma loja da rede de supermercados.
    """

    # Construtor da classe Loja
    def __init__(self, nome: str, id_loja: str):

        # Atributo para armazenar o nome da loja
        self.nome = nome

        # Atributo para armazenar o ID da loja
        self.id_loja = id_loja

        # Lista vazia para armazenar as ordens de manutenção associadas à loja
        self.ordens_manutencao = []

    # Método para adicionar uma ordem de manutenção à lista de ordens da loja
    def adicionar_ordem_manutencao(self, ordem):

        # Insere o objeto ordem de manutenção na lista de ordens
        self.ordens_manutencao.append(ordem)

    # Método especial que define a representação em string do objeto
    def __str__(self):

        # Retorna uma string formatada com nome e ID da loja
        return f"Loja: {self.nome} (ID: {self.id_loja})"