from django.contrib import admin
from django.urls import path
from .views import *

# gerencia as rotas da aplicacao
urlpatterns = [
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('editar_tarefa/<int:id>', editar_tarefa, name='editar_tarefa'),
    # entre <> passamos o tipo do parametro e o parametro, deve ser o mesmo nome no metodo editar_tarefa na view
]
