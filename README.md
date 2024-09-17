# FORMERCE

## URLs 
- Visit [Formerce](https://muhammad-wendy-formerce.pbp.cs.ui.ac.id/)
- Tugas
    - [Tugas 3](#pertanyaan-dan-jawaban-tugas-3)
    - [Tugas 2](#pertanyaan-dan-jawaban-tugas-2)


## Pertanyaan dan Jawaban Tugas 3
A. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
> Data delivery butuh diimplementasikan karena kita perlu mengirimkan data dari satu stack ke stack lainnya.

B. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
> Menurut saya JSON lebih baik dibandingkan dengan XML. JSON lebih populer dibandingkan XML karena *syntax* nya yang lebih mudah dibaca, skema dokumentasi yang lebih simpel dan fleksibel, ukuran berkas yang lebih kecil, dan lebih aman.

C.  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
> Fungsi dari Method is_valid() adalah untuk mengecek apakah data yang diinput valid dengan *data field* yang ada dan mengembalikan boolean berdasarkan hasil validasi. *Method* ini dibutuhkan untuk memastikan bahwa data yang diinput sesuai dengan yang diminta dan aman sebelum diproses lebih lanjut.

D.  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
> csrf_token dibutuhkan untuk menlindungi serangan *Cross-Site Request Forgery*, yaitu serangan yang membuat browser pengguna melakukan aksi-aksi yang tidak diinginkan seperti mentransfer uang atau mengubah email yang terdaftar. csrf_token melindungi dari serangan ini dengan cara membuat sebuah token secara acak dan unik setiap pengguna memulai sesi di suatu website, lalu menggunakan token tersebut untuk memverifikasi setiap request yang diproses.

E. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat berkas baru bernama `base.html` pada direktori `templates` yang digunakan sebagai template dasar dan kerangka umum halaman web lainnya pada proyek dengan konten seperti berikut:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
Lalu saya menambahkan `'templates'` pada variabel TEMPLATES dalam berkas `settings.py`

2. Mengubah kode pada berkas `main.html` untuk menggunakan `base.html sebagai *template* utama.

3. Membuat berkas baru `forms.py` pada direktori main untuk membuat struktur form yang dapat menerima data *Product Entry* baru. 
```python
from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description"]
```
4. Membuat fungsi baru pada `views.py` yang menerima parameter `request` untuk menghasilkan form yang dapat menambahkan data Product Entry secara otomatis ketika data di-submit dari form.
```python
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

5.Mengubah fungsi show_main pada berkas yang sama untuk dapat mengambil seluruh objek `ProductEntry` pada database.
```python
def show_main(request):
    product_entries = ProductEntry.objects.all()

    context = {
        'project_name': 'Formerce',
        'name' : 'Muhammad Wendy Fyfo Anggara',
        'class': 'PBP E', 
        'product_entries': product_entries,
    }

    return render(request, "main.html", context)
```

6. Menambahkan path URL untuk membuat ProductEntry ke dalam variabel urlpatterns pada urls.py di main untuk mengakses fungsi pada `views.py`
```python
urlpatterns = [
   ...
   path('create-product-entry', create_product_entry,name='create_product_entry')
]
```

7. Membuat berkas HTML baru dengan nama create_product_entry.html pada direktori `main/templates`
```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

8. Menambahkan kode pada `main.html` untuk menampilkan product serta tombol yang me-*redirect* ke halaman form. 
```html
<!DOCTYPE html>

{% extends 'base.html' %}
{% block content %}
<h1>{{ project_name }}</h1>
<p>{{ name }} ----- {{ class }}</p>

<h3>Products:</h3>

{% if not product_entries %}
<p>Belum ada product yang terdaftar.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
  </tr>

  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product</button>
</a>
{% endblock content %}
```

9. Menambahkan empat fungsi baru pada `views.py` untuk mengembalikan data dalam bentuk XML atau JSON, serta menampilkan semua atau berdasarkan id
```python
def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request,id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

```

10. Menambahkan path url ke dalam urlpatterns pada `main/urls.py` untuk mengakses fungsi-fungsi di atas.
```python
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>', show_json_by_id, name='show_json_by_id'),
]
```

### Lampiran --- Hasil akses keempat URL pada Postman 
- '/xml'
![XML](assets/postman_results/request_xml.png)

- '/xml/[id]'
![XML_by_id](assets/postman_results/request_xml_by_id.png) 

- '/json'
![JSON](assets/postman_results/request_json.png) 

- '/json/[id]'
![JSON_by_id](assets/postman_results/request_json_by_id.png) 

## Pertanyaan dan Jawaban Tugas 2

A. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1. menjalankan program `django-admin startproject formerce .\` untuk membuat project django baru

2. menjalankan program `python manage.py startapp main` untuk membuat aplikasi baru bernama main pada proyek.

3. Menambahkan `path('', include('main.urls')),` pada formerce/urls/py untuk me-route proyek sehingga dapat menjalankan aplikasi main

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

4. Pada models.py, membuat class Product dengan atribut name, price, dan description yang masing-masing bertipe model.charField, models.IntegerField, models.TextField.

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
``` 

5. Membuat sebuah fungsi pada views.py yang mengembalikan sebuah template HTML untuk menampilkan nama aplikasi serta nama dan kelas saya.

***views.py***

```python
from django.shortcuts import render

def show_main(request):
    context = {
        'project_name': 'Formerce',
        'name' : 'Muhammad Wendy Fyfo Anggara',
        'kelas': 'PBP E',
    }

    return render(request, "main.html", context)
```

***main.html***

```html
<!DOCTYPE html>

<h1>{{ project_name }}</h1>
<p>{{ name }} ------- {{ kelas }}</p>
```

6. Membuat routing pada urls.py pada aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py

```python
from django.urls import path
from main.views import show_main

urlpatterns = [
path('', show_main, name='show_main'),
]
```

7.melakukakan *deployment* ke PWS dengan membuat project baru pada website PWS dan push project ke PWS.
 
B. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

```mermaid
flowchart TD
    E[HTTP Requests] -->|Send Requests| A[urls.py]
    A --> |Forward request to appropriate view| B[views.py]
    B <--> |read/write data| C[models.py]
    B -->|Return a Response| F[HTTP Response html]
    D[Template .html file] --> B
```
1. urls.py menerima HTTP request
2. urls.py parse request dan meneruskannya ke views.py yang sesuai
3. views.py membaca/memperbarui models.py sesuai request
4. views.py mengembalikan respon dengan file html yang sesuai dengan request dan hasil  *read/write* models.py ke user

C. Jelaskan fungsi git dalam pengembangan perangkat lunak!

> Fungsi git dalam pengembangan perangkat lunak adalah menjadi **sistem kontrol versi** yang membantu melacak perubahan pada kode sumber proyek. Git memberikan kemampuan untuk memantau semua revisi yang pernah dilakukan selama proses pengembangan perangkat lunak.

D. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

>Django adalah framework yang dibuat di atas bahasa pemrograman python, sehingga penggunaan bahasa pemrograman yang mudah menjadi salah satu alasannya. Selain itu, Django hadir dengan banyak fitur siap pakai yang memudahkan pemula untuk membangun perangkat lunak dengan mudah dan cepat.

E. Mengapa model pada Django disebut sebagai ORM?

>Kepanjangan dari ORM adalah **Object-Relational Mapper**. ORM adalah fitur/teknik yang memungkinkan kita untuk berinteraksi langsung dengan database menggunakan class python tanpa perlu menuliskan SQL queries. Model pada Django disebut sebagai ORM karena model adalah object python karena teknik ORM memetakan relasi antara **database** dengan sebuah model, sehingga setiap class model merepresentasikan sebuah tabel database yang memiliki atribut yang berhubungan dengan sebuah kollom pada tabel tersebut.