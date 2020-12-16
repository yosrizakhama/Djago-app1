from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('book/', views.book, name = "books"),
    path('costumer/', views.connect, name = "costumers"),
    path('costumer/<int:id>', views.costumer, name = "costumer"),
    path('create/', views.create, name = "create"),
    path('create/<int:pk>', views.create_inline, name = "createinline"),
    path('update/<int:id>', views.update, name = "update"),
    path('delete/<int:id>', views.delete, name = "delete"),
]
