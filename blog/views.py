from django.shortcuts import render
from blog.data import posts
# from django.http import HttpResponse

# Create your views here.


def blog_view(request):
    print('blog')

    context = {
        'posts': posts,
    }
    return render(
        request,
        'blog/index.html',
        context
    )


def example_view(request):
    print('example')
    context = {
        'text': 'Estamos no example',
        'title': 'Exemplo - ',
    }
    return render(
        request,
        'blog/example.html',
        context,
    )


def post_view(request, _id):
    print('post', _id)

    context = {
        'posts': posts,
    }
    return render(
        request,
        'blog/index.html',
        context
    )
