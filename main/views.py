from django.shortcuts import render

def show_main(request):
    context = {
        'project_name': 'Formerce',
        'name' : 'Muhammad Wendy Fyfo Anggara',
        'kelas': 'PBP E',
        'product_name': 'AIO Screwdriver',
        'price': 75000,
        'description': 'An all-in-one screwdriver for all your screwing needs. \n64 kind of screw bits included with the products',
    }

    return render(request, "main.html", context)