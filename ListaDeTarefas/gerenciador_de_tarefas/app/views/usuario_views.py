from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_tarefas')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})


def logar_usuario(request):
    # verifica se o metodo é post, (user clicou em 'entrar')
    if request.method == "POST":
        # coletando infos do form
        username = request.POST["username"]
        password = request.POST["password"]
        # verificando se as infos existem no bd (se este user já está cadastrado)
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            # se ele existe, é feito o login e redireciona até a home (entrou no sist)
            login(request, usuario)
            return redirect('listar_tarefas')
        else:
            # se nao, mostramos mensagem de erro e se mantem na tela de login
            messages.error(request, "As credenciais do usuário estã incorretas.")
            return redirect('logar_usuario')
    else:
        # se nao for post criamos uma instancia vazia
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})


