from django.db import models
from django.db.models.base import Model
from stdimage.models import StdImageField, JPEGField

# signals
    # Existe um processamento para fazer algo antes ou depois de salvar
from django.db.models import signals

# um criar uma  slug
from django.template.defaultfilters import  slugify

 # e legal criar para todos os projeots por que alguns campos acabam se repetindo
class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True



class Produto(Base):
    nome = models.CharField('Nome', max_length= 100)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=True)

    def __str__(self):
        return self.nome


# temos que criar o singls no mesmo nível da classe

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)