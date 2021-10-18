from django import forms
from django.core.mail import message
from django.shortcuts import redirect, render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from . models import Produto

# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }   
    return render(request, 'index.html', context)

def contato(request): 
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            # Usando para testar
            # print(f'Nome {nome}')
            # print(f'Nome {email}')
            # print(f'Nome {assunto}')
            # print(f'Nome {mensagem}')
            form.send_email()
            messages.success(request, 'Email Enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar email')
    contexto = {
        'form':  form
    }   
    
   
    return render(request, 'contato.html', contexto)
    

def produtos(request):
    # usado para teste de sessao
    # print(f'Usuario: {request.user}')
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':

            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                # prod = form.save(commit=False)
                # print(f'Nome: {prod.nome}')
                # print(f'Preco: {prod.preco}')
                # print(f'Estoque: {prod.estoque}')

                form.save()
                messages.success(request, 'Produto salvo com sucess')
            
            else:
                messages.success(request, 'Erro ao salvar o produto')
        else:
            form = ProdutoModelForm()
        
        context = {
            'form': form
        }
        return render(request, 'produtos.html', context)
    else:
        return redirect('index')
