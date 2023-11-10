from django.urls import path

from home.views import home_view

# http://dominio.com.br/


urlpatterns = [
    path('', home_view),
]
