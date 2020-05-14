# Django Basics

---
## 1. Getting Started

```
django-admin startproject PROJECTNAME
cd PROJECTNAME
django-admin startapp APPNAME (also python manage.py startapp APPNAME)
```

---
## 2.Template views

### Main
* **settings.py** -> Insert the new app
* **urls.py** -> Import app's url; include app url World's path 

#### App
* **urls.py** -> Create file
* **urls.py**-> import app's views; include the view.function to be created
```
from django.urls import path
from first_app import views


urlpatterns = [
    path('', views.index, name='index')
]
```
* **views.py** -> create function returning a rendered page (using the template to be created)

```
from django.shortcuts import render

def index(request):
    my_dict = {'insert_context': "HELLO I'M FROM FIRSTAPP!"}
    return render(request, "first_app/index.html", context=my_dict)
```


#### Templates
* **Project Root** -> Create 'templates' folder
* **Templates Folder** -> Create APPNAME folder; 
* **APPNAME Folder** -> Create a index.html template file.

```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Hello World</title>
	</head>
	<body>
	<h1>Testing page</h1>
	<p>{{ insert_context }}</p>
	</body>
</html>
```

#### Main (Again)
* **settings.py** -> Insert the new template


---

## 3. Static files


#### App/Templates

* **html** -> Add the static image code.

```
{% load static %}
.
.
.

<img src="{% static "my_app/example.jpg" %}" alt="My image">
```

#### Main

* **settings.py** -> Insert the static directory

```
STATIC_DIR = os.path.join(BASE_DIR, "static")
.
.
.

STATICFILES_DIRS = [
    STATIC_DIR,
]
```


---

## 4. Models



#### App

* **models.py** -> Create new models

```
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)
```

* **views.py** -> Import created models to the views; Add model view;

```
from . import models.User

def users(request):
	user_list = User.objects.order_by('first_name')
	user_dict = {'users': user_list}
	return render(request, )
```

#### Root
```
python manage.py createsuperuser

```
