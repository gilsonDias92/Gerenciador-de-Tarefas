from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import TarefaForm
from ..entidades.tarefa import Tarefa
from ..services import tarefa_service
# renderizar template


@login_required()
def listar_tarefas(request):
    tarefas = tarefa_service.listar_tarefas(request.user)
    # capturando todas as tarefas
    return render(request, 'tarefas/listar_tarefas.html', {"tarefas": tarefas})


@login_required()
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
                                 prioridade=prioridade,
                                 usuario=request.user)
           tarefa_service.cadastrar_tarefa(tarefa_nova)
           return redirect('listar_tarefas')
    else:
        form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})


@login_required()
def editar_tarefa(request, id):
    # buscar qual tarefa quero editar no bd
    tarefa_bd = tarefa_service.listar_tarefa_id(id)

    if tarefa_bd.usuario != request.user:
        return HttpResponse("Não permitido")

    # criamos o form com base nas informacoes que vieram do banco de dados
    form_tarefa = TarefaForm(request.POST or None, instance=tarefa_bd)
    # quando alterarmos as infos e clicar em 'salvar' verificamos se as mesmas sao validas
    if form_tarefa.is_valid():
        # captura de todas as informacoes do form
        tituloo = form_tarefa.cleaned_data["tituloo"]
        descricao = form_tarefa.cleaned_data["descricao"]
        data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
        prioridade = form_tarefa.cleaned_data["prioridade"]
        # criamos um novo objeto do tipo Tarefa com as novas infos
        tarefa_nova = Tarefa(tituloo=tituloo,
                             descricao=descricao,
                             data_expiracao=data_expiracao,
                             prioridade=prioridade,
                             usuario=request.user)
        # Enviamos tanto a tarefa antiga(bd) quanto a tarefa nova pro metod editar_tarefa
        tarefa_service.editar_tarefa(tarefa_bd, tarefa_nova)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})


@login_required()
def remover_tarefa(request, id):
    # retorna o id da tarefa a ser removida
    tarefa_bd = tarefa_service.listar_tarefa_id(id)
    if tarefa_bd.usuario != request.user:
        return HttpResponse("Não permitido")
    if request.method == "POST":
        tarefa_service.remover_tarefa(tarefa_bd)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/confirma_exclusao.html', {'tarefa': tarefa_bd})

