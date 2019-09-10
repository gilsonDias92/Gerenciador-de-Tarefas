from django.shortcuts import render
from .forms import TarefaForm
# renderizar template


def listar_tarefas(request):
    nome_tarefa = "Aula de inglês - 16h"
    return render(request, 'tarefas/listar_tarefas.html',
    {"nome_tarefa": nome_tarefa})


def cadastrar_tarefa(request):
    form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})

