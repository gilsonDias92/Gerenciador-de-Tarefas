from ..models import Tarefa

def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(tituloo=tarefa.tituloo,
                          descricao=tarefa.descricao,
                          data_expiracao=tarefa.data_expiracao,
                          prioridade=tarefa.prioridade)
