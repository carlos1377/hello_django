from django.urls import path

from blog.views import blog_view, example_view

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='home'),
    path('example/', example_view, name='example',)
]
