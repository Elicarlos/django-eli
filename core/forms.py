from django import forms
from django.forms import fields
from django.forms.widgets import Textarea
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome")
    email = forms.EmailField(label='Email')
    assunto = forms.CharField(label="Assunto")
    mensagem = forms.CharField(label="mensagem", widget=Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n Email: {email}\n Assunto: {assunto}\n Mensagem: {mensagem}' 
        
        email = EmailMessage(
            subject='Email enviado pelo Projeto Django 2',
            body= conteudo,
            to=['contato@dominio.com.br',],
            from_email ='contato@dominio.com',
            headers= {'Reply_To': email}
        )

        email.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
