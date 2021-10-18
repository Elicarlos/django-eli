from django.urls import path
from core.views import index, produtos, contato

urlpatterns = [ 
    path("", index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produtos, name='produto'),
]