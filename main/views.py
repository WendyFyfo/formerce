from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'AIO Screwdriver',
        'price': '75000',
        'description': 'Your all-in-one tool to fix all your device.'
    }

    return render(request, "main.html", context)