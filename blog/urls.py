from django.urls import path

from blog.views import blog_view, example_view

# http://dominio.com.br/


urlpatterns = [
    path('', blog_view),
    path('example/', example_view,)
]
