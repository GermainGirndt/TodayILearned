# Django Basics - 2

---
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


