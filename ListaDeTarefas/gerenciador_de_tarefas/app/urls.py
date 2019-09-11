from django.urls import path
from .views.tarefa_views import *
from .views.usuario_views import *
from .views import *
# gerencia as rotas da aplicacao
urlpatterns = [
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('editar_tarefa/<int:id>', editar_tarefa, name='editar_tarefa'),
    path('remover_tarefa/<int:id>', remover_tarefa, name='remover_tarefa'),
    # entre <> passamos o tipo do parametro e o parametro, deve ser o mesmo nome no metodo editar_tarefa na view
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
]
