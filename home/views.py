from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home_view(request):
    print('home')

    context = {
        'text': 'Estamos na Home'
    }

    return render(
        request,
        'home/index.html',
        context,
    )
