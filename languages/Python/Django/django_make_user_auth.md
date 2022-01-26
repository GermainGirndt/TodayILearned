# Django - Make user auth


#### Models

```
from django.db import models
from django.contrib import auth
# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{self.username}"
```


#### Views

```
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from accounts import forms


# Create your views here.
class SignUp(CreateView):
    # Not instantiate the class!! Class()
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"

```


#### Forms
```
from accounts import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding label
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"
        
```



#### Template

```
{% extends "base.html" %}
{% load bootrstrap4 %}

{% block content %}
<div class ="container">
	<h1>Sign Up</h1>
	<form method="POST">
		{% csrf_token %}
		{% bootstrap_form form %}
		<input type="submit" class='btn btn-primary' name="Sign Up">
	</form>	
{% endblock content %}
```




```

```




```

```