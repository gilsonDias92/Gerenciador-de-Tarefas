from ..models import Tarefa

def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(tituloo=tarefa.tituloo,
                          descricao=tarefa.descricao,
                          data_expiracao=tarefa.data_expiracao,
                          prioridade=tarefa.prioridade)


# retorna todas as tarefas cadastradas no banco de dados
# SELECT * FROM app_tarefa
def listar_tarefas():
    return Tarefa.objects.all()

