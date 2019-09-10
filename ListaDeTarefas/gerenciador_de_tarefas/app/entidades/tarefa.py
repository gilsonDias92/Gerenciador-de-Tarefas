class Tarefa():
    def __init__(self, tituloo, descricao, data_expiracao, prioridade):
        self.__tituloo = tituloo
        self.__descricao = descricao
        self.__data_expiracao = data_expiracao
        self.__prioridade = prioridade

    @property
    def tituloo(self):
        return self.__tituloo

    @tituloo.setter
    def tituloo(self, tituloo):
        self.__tituloo = tituloo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def data_expiracao(self):
        return self.__data_expiracao

    @data_expiracao.setter
    def data_expiracao(self, data_expiracao):
        self.__data_expiracao = data_expiracao

    @property
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade):
        self.__prioridade = prioridade

