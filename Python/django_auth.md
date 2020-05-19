# Django Authentication

---
## 1. Getting Started


#### Terminal
```
pip install django[argon2]
pip install bcrypt
```


---
## 2. Hashers


#### Main

* **settings.py** -> add password hashers
```
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]
```
* **settings.py** -> increase min. password length at AUTH_PASSWORD_VALIDATORS
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length':9}
    },



#### Root

* **media** -> create a media foder for user's media and register it in the settings.py file

```
MEDIA_DIR = os.path.join(BASE_DIR, "media")
.   
.   
.   
#MEDIA
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
```



---
## 2. Creating a new User Model

* **Install Pillow lib for using images**

```
pip install pillow
```

#### App

* **models.py** -> import default User; Extend new User to it; Create a new User model; Create a new folder in media directory for the user's media;

```
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

    # extending class (inheritating may cause error)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    # profile_pics in media folder

    def __str__(self):
        return self.user.username


```


* **forms.py** -> create the model forms

```
from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

```

* **admin.py** -> register the new model/form

```
from basic_app.models import UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
```

#### Terminal

* **Makemigrations/Migrate**

## 3. Setting the templates

#### Templates

* **base.html**

```
<!DOCTYPE html>
<html>
<head>
	<title>Base</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
	<div class="container">
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
			<ul class="navbar-nav">
				<li><a class="navbar-brand" href="{% url 'index' %}">DJANGO</a></li>
				<li><a class="nav-link" href="{% url 'admin:index' %}">Admin</a></li>	
				<li><a class="nav-link" href="{% url 'basic_app:register' %}">Register</a></li>			
			</ul>
		</nav>
	</div>	

	<div class="container">
		 {% block body_block %}
		 {% endblock %}
	</div>
</body>
</html>
```

* **index.html**
```
{% extends "basic_app/base.html" %}

{% block body_block %}
<div class="jumbotron">
	<h1>Django Level Five</h1>
</div>
{% endblock %}
```

* **registration.html**

```
{% extends "basic_app/base.html" %}
{% load static %}

{% block body_block %}
<div class="jumbotron">
	{% if registered %}
		<h1>Thank you for registering!</h1>
	{% else %}
		<h1>Register Here!</h1><br>
		<h3>Fill out the form:</h3>

	<form enctype="multipart/form-data" method="post">
		{% csrf_token %}
		{{ user_form.as_p }}
		{{ profile_form.as_p }}
		<input type="submit" name="" value="Register">
	</form>
	{% endif%}

</div>
{% endblock %}
```

## 4. Setting up the views

## App

* **views.py**

```
from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()  # sets and saves to the database
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)  # false to not colliding with user
            profile.user = user  # sets up the 1 to 1 relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:  # if invalid, print errors
            print(user_form.errors, profile_form.errors)
    else:  # http get request
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',
                  {
                      'user_form': user_form,
                      'profile_form': profile_form,
                      'registered': registered
                  }
                  )


```

## Main and App
* ** urls.py** -> add app_name and correctly redirect to the views


## 5. Setting up the login views

#### Main
* **settings.py** -> add login_url
```
LOGIN_URL = '/basic_app/user_login'
```

#### Templates

* **login.html** -> Create the login page (user login view to be implemented)
```
{% extends "basic_app/base.html" %}
{% block body_block %}

<div class="jumbotron">
	<h1>Please Login</h1><br>
	<form action="{% url 'basic_app:user_login' %}" method="post">
		{% csrf_token %}
		<label for="username">Username: </label>
		<input type="text" name="username" placeholder="Enter Username">
		<label for="password">Password: </label>
		<input type="password" name="password">
		<input type="submit" name="" value="Login">
	</form>	
</div>
{% endblock %}
```

#### App

* **views.py** -> Create login function

```
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required  # turns login required for viewing a page



def user_login(request):
    print("hehe	")
    if request.method == "POST":
        username = request.POST.get('username')  # gets username from html-form
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)  # django built-in function

        if user:
            if user.is_active:
                login(request, user)  # built-in function
                return HttpResponseRedirect(reverse('index'))  # direct back to the homepage

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print(f" Username: {username} tried to login and failed")
            return HttpResponse("Invalid login/password")
    else:
        return render(request, 'basic_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


```

#### Main and App

* **Main/urls.py** -> Add new pattern
```
path('logout/', views.user_logout, name='logout')
```
* **App/urls.py** -> Add new pattern
```
path('login/', views.user_login, name='login')
```


#### Templates
* **base.html** -> Include login/logout
```
				{% if user.is_authenticated %}

				<li><a class="nav-link" href="{% url 'logout' %}">Logout</a></li>

				{% else %}

				<li><a class="nav-link" href="{% url 'basic_app:user_login' %}">Login</a></li>

				{% endif %}



```