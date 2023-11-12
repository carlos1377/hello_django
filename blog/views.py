from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def blog_view(request):
    print('blog')

    context = {
        'text': 'Estamos no blog',
        'title': 'Blog - ',
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
