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


def listar_tarefa_id(id):
    return Tarefa.objects.get(id=id)


# esse metodo realiza as alteracoes, da tarefa antiga para a tarefa nova, agora vamos criar uma rota
def editar_tarefa(tarefa_bd, tarefa_nova):
    tarefa_bd.tituloo = tarefa_nova.tituloo
    tarefa_bd.descricao = tarefa_nova.descricao
    tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
    tarefa_bd.prioridade = tarefa_nova.prioridade
    tarefa_bd.save(force_update=True)


def remover_tarefa(tarefa_bd):
    tarefa_bd.delete()