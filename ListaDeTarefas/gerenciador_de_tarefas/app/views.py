from django.shortcuts import render

# renderizar template


def listar_tarefas(request):
    nome_tarefa = "Aula de inglês - 16h"
    return render(request, 'tarefas/listar_tarefas.html',
    {"nome_tarefa": nome_tarefa})

