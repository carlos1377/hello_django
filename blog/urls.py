from django.urls import path

from blog.views import blog_view, example_view, post_view

app_name = 'blog'

# blog/
urlpatterns = [
    path('', blog_view, name='home'),
    path('<int:_id>/', post_view, name='post'),
    path('example/', example_view, name='example',)
]
