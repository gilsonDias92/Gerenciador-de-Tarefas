from django.shortcuts import render, redirect
from .forms import TarefaForm
from .entidades.tarefa import Tarefa
from .services import tarefa_service
# renderizar template


def listar_tarefas(request):
    nome_tarefa = "Aula de inglês - 16h"
    return render(request, 'tarefas/listar_tarefas.html',
    {"nome_tarefa": nome_tarefa})


def cadastrar_tarefa(request):
    if request.method == "POST":
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
           tituloo = form_tarefa.cleaned_data["tituloo"]
           descricao = form_tarefa.cleaned_data["descricao"]
           data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
           prioridade = form_tarefa.cleaned_data["prioridade"]
           tarefa_nova = Tarefa(tituloo=tituloo,
                                 descricao=descricao,
                                 data_expiracao=data_expiracao,
                                 prioridade=prioridade)
           tarefa_service.cadastrar_tarefa(tarefa_nova)
           return redirect('listar_tarefas')
    else:
        form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})

