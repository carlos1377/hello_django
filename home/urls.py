from django.urls import path

from home.views import home_view

# http://dominio.com.br/

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home',),
]
