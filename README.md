# FORMERCE

------ 

[Visit Website](https://muhammad-wendy-formerce.pbp.cs.ui.ac.id/)

## Pertanyaan dan Jawaban

A. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

    1. menjalankan program `django-admin startproject formerce .\` untuk membuat project django baru

    2. menjalankan program `python manage.py startapp main` untuk membuat aplikasi baru bernama main pada proyek.

    3. Menambahkan `path('', include('main.urls')),` pada formerce/urls/py untuk me-route proyek sehingga dapat menjalankan aplikasi main

    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

    4. Pada models.py, membuat class Product dengan atribut name, price, dan description yang masing-masing bertipe model.charField, models.IntegerField, models.TextField.

    ```
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
    ``` 

    5. Membuat sebuah fungsi pada views.py yang mengembalikan sebuah template HTML untuk menampilkan nama aplikasi serta nama dan kelas saya.

    ```
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
    ```
    
    6. Membuat routing pada urls.py pada aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
    
    ```
    from django.urls import path
    from main.views import show_main

    urlpatterns = [
    path('', show_main, name='show_main'),
    ]
    ```

    7.melakukakan **deployment** ke PWS dengan membuat project baru pada website pws dan push project ke PWS.
 
B. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

```mermaid
flowchart TD
    E[HTTP Requests] -->|Send Requests| A[urls.py]
    A --> |Forward request to appropriate view| B[views.py]
    B <--> |read/write data| C[models.py]
    D[Template .html file] --> B
    B -->|Return a Response| F[HTTP Response (HTML)]
```