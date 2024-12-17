from django.urls import path 
from . import views

urlpatterns = [
    path('produtos', views.listar_produtos),
    path('listar_produtos', views.ProdutosViews.as_view()),
    path('produto/<int:pk>', views.ProdutoDetailView.as_view()),
]
