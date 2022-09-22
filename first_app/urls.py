from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/<int:num>', views.hello),
    path('', views.index)
]
