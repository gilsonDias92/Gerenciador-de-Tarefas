from django.shortcuts import render

# renderizar template


def listar_tarefas(request):
    return render(request, 'tarefas/listar_tarefas.html')