# Django Basics - 2

---
## 0. Installing packages (bootstrap)

#### Terminal

```
pip install django-bootstrap4
```

#### Main
* **settings.py**
```
INSTALLED_APPS = [
	'bootstrap4'
]
```

## 1. Success message after user register

#### Main

* **views.py** -> import messages
```
from django.shortcuts import render, redirect
from djangocontrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
	if request.method == 'POST':
	form = UserCeationForm(request.POST)
	if form = form.isvalid():
		username = form.cleaned_data.get('username')
		messages.success(request, f'Account created for {username}')
		messagess.success(request, f'Account created for {username}')
		return redirect('blog-home')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form':form})
```


## 2. Cryspy - forms - Form layout 

#### Main
* **settings.py** -> Set bootstrap4
```
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

#### Templates
* **formtemplate.py** -> Add tag
```
{% load crispy_forms_tags %}
.
.
.
<!-- Remember to add form legends: -->
{{ form|crispy }}
```

* **