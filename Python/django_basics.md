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

* **urls.py** -> Add view to be created

```
path('users/', views.users, name='users')
```


* **views.py** -> Import created models to the views; Add model view;

```
from . import models.User

def users(request):
	user_list = User.objects.order_by('first_name')
	user_dict = {'users': user_list}
	return render(request, 'first_app/users.html, context='user_dict')
```

#### Main

* **admin.py** -> Import Model and Register it;

```
from first_app.models import User

admin.site.register(User)
```

#### Terminal


* **Terminal** -> Make migrations to create the model in the DB;

```
python manage.py migrate
python manage.py makemigrations
```

* **Terminal** -> Create a super user
```
python manage.py createsuperuser
```

#### Template


* **users.html** -> Print the models (obs: endfor! endif!)


```
{% if users %}
<ol>
	{% for person in users %}
	<li class="row">User info</li>
	<ul>
		<li col s1>First Name: {{ person.first_name }}</li>
		<li col s1>Last Name: {{ person.last_name }}</li>
		<li col s1>Email: {{ person.email }}</li>
		<br>
	</ul>
	{% endfor %}
</ol>
{% endif %}
```

---

## 5. Forms

#### App

* **forms.py** -> Create new form (like models)

```
from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)  # standard widget for it
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")


#	def clean_botcatcher(self):
#		botcatcher = self.cleaned_data['botcatcher']
#		if len(botcatcher) > 0:
#		raise forms.ValidationError("GOTCHA BOT!")
#		return botcatcher```

```

* **views.py** -> Create form view

```
from . import forms   
.   
.   
.   
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")  # on the console
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"EMAIL: {form.cleaned_data['email']}")
            print(f"TEXT: {form.cleaned_data['text']}")
            form = forms.FormName()
    context = {"form": form}
    return render(request, "basicapp/form_page.html", context)
```

* **urls.py** -> Add new url pattern poiting to the created view and to the template to be created
```
    path('formpage/', views.form_name_view, name='form_name'),
```


#### Template

* **form_page.html** -> Create a new form page template

```
<!DOCTYPE html>
<html>
<head>
	<title>Forms</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
	<h1>Fill out the form!</h1>
	<div class="container">
		<form method="POST">
		{{ form.as_p }}
		{% csrf_token %}
		<input type="submit" class="btn btn-primary" name="Submit">
		</form>
	</div>
</body>
</html>
```

---

## 6. ModelForms
With a preexisting model you can directly create a model form to it, saving lots of time.


#### App

* **forms.py** -> Create a class that inherits the models

```
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    # form fields
    # add extra form validation here

    class Meta:
        model = User
        fields = "__all__"
        # Alternatively:
        # fields = FIELD TO INCLUDE
        # exclude = FIELDS TO EXCLUDE

```

* **urls.py** -> Create a url and redirect it to the view to be created

* **view.py** -> Create a form view. Remember to save the data to the database after the validation:

```
form.save(commit==True)
```

#### Templates
* **model_form.html** -> Create a form page


---

## 7. Template Tagging

#### App

* **urls.py** -> Insert the app name

```
app_name = 'APPNAME'

```

#### Templates

* **relative_url_templates.py** -> Reference the app name

**Before (referencing template itself):**
```
    <a href="app_name/webpage.html"> The app page</a>
```
**After (referencing url.py file):**
```
    <a href="{% url 'app_name:url_pattern_name' %}"> The app page</a>
```

## 8. Template Inheritance (Template Extending)

#### Templates

* **base.html** -> Create base file to be inherited. Mark the varibles with blocks.

* **index.html** -> Extend to the base html. Insert what's new in the blocks.

```
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
 
```


## 9. Using filters

#### Templates
* **index.html** -> use |

```
{{ story.headline|upper }}

{{ clients_number|add:"99" }}
```

## 10. Custom filters

#### App
* **templatetags** -> Create folder

#### App/templatetags
* **__init__.py** -> Create file
* **my_extras.py** -> Create file, create function and register it using the register decorator:
```
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):

    #Cuts out all values of 'arg' from the string
    return value.replace(arg,'')
```

