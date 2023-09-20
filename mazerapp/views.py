from django.shortcuts import render, redirect
from usuarios.models import Usuario
from .models import Produtos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


@login_required(login_url='index')
def dashboard(request):
    produtos = Produtos.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(produtos, 3)
    page_num = paginator.get_page(page)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    usuario_perfil = Usuario.objects.get(user=request.user)

    context = {
        'produtos':result,
        'user': usuario_perfil,
    }
    
    return render(request, 'dashboard.html', context)

@login_required(login_url='index')
def editarProduto(request):
    return render(request, 'editar-produto.html')

@login_required(login_url='index')
def meusProdutos(request):
    produtos = Produtos.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(produtos, 3)
    page_num = paginator.get_page(page)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    usuario_perfil = Usuario.objects.get(user=request.user)

    context = {
        'produtos':result,
        'user': usuario_perfil,
    }
    
    return render(request, 'meus-produtos.html', context)

@login_required(login_url='index')
def registrarProdutos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_produto')
        email = request.POST.get('email')
        preco = request.POST.get('preco_produto')
        imagem = request.FILES.get('imagem_produto')
        descricao = request.POST.get('exampleFormControlTextarea1')
        categoria = request.POST.get('basicSelect')
        
        produto = Produtos(
            nome = nome,
            email = email,
            preco = preco,
            imagem = imagem,
            descricao = descricao,
            categoria = categoria
        )

        produto.save()

    return render(request, 'registrar-produtos.html')

@login_required(login_url='index')
def editarProduto(request, id):
    produto = Produtos.objects.get(id_produto = id)

    if request.method == 'POST':
        nome = request.POST.get('nome_produto')
        email = request.POST.get('email')
        preco = request.POST.get('preco_produto')
        imagem = request.FILES.get('imagem_produto')
        descricao = request.POST.get('exampleFormControlTextarea1')
        categoria = request.POST.get('basicSelect')

        produto.nome = nome
        produto.email = email
        produto.preco = preco
        produto.imagem = imagem
        produto.descricao = descricao
        produto.categoria = categoria
        produto.save()
    
    context = {
        'produto': produto,
    }

    return render(request, 'editar-produto.html', context)

@login_required(login_url='index')
def deletarProduto(request, id):
    produto = Produtos.objects.get(id_produto = id)
    produto.delete()

    return redirect('dashboard')
