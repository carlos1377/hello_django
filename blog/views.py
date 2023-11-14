from typing import Any
from django.shortcuts import render
from blog.data import posts
from django.http import HttpRequest, Http404
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


def post_view(request: HttpRequest, _id: int):
    found_post: dict[str, Any] | None = None
    for post in posts:
        if post['id'] == _id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não exite')

    context = {
        'post': found_post,
        'title': found_post['title'] + '-',
    }
    return render(
        request,
        'blog/post.html',
        context
    )
