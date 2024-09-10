from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Juragan Nelayan',
        'name': 'Raihan Akbar',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

