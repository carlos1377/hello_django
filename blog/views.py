from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def blog_view(request):
    print('blog')
    return render(
        request,
        'blog/index.html'
    )


def example_view(request):
    print('example')
    return render(
        request,
        'blog/example.html'
    )
