from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def handler404(request, exception):
    return render(request, 'error-404.html')
 
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Usuario.objects.filter(user__email=email).exists():
            username = Usuario.objects.get(user__email=email).user.username
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user=user)
                return redirect('dashboard')

    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def cadastrarUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        apelido = request.POST.get('apelido')
        conf_senha = request.POST.get('conf_senha')

        if conf_senha == password:
            if not Usuario.objects.filter(user__email=email).exists():
                user = User.objects.create_user(username, email, password)
                user.save()
                Usuario(user=user, u_apelido=apelido).save()
        else:
            print('Senhas diferem!!')

    return render(request, 'auth-register.html')

@login_required(login_url='index')
def editarUsuario(request):
    usuario_perfil = Usuario.objects.get(user = request.user)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_senha = request.POST.get('conf_senha')
        imagem = request.FILES.get('user_imagem')

        if conf_senha == password:
            if Usuario.objects.filter(user__email=email).exists():

                usuario_perfil.user.username = username
                usuario_perfil.user.email = email
                usuario_perfil.user.set_password(password)
                usuario_perfil.user.save()

                usuario_perfil.user_imagem = imagem
                usuario_perfil.save()
                
        else:
            print('Senhas diferem!!')

    context = {
        'user': usuario_perfil
    }

    return render(request, 'editar-usuario.html', context)

