from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Muhammad Wendy Fyfo Anggara',
        'kelas': 'PBP E',
    }

    return render(request, "main.html", context)