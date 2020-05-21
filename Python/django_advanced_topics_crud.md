# Django - Advanced Topics - CRUD
* probably not that advanced at all for experienced python developers

## CRUD - Imports - views.py
```
from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from basic_app import models
```

## Create

#### App

* **views.py** -> Create view for model instance creation. When created, calls the model's get_absolute_url method.

```
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    # tuple for not editing
    model = models.School
```
* **models.py** -> Import reverse; Add get_absolute_url method for redirecting to school detail view after school creation using the automatically generated PK)
```
from django.urls import reverse
.
.
.

class School(models.Model):
.
.
.
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk': self.pk})

```
* **urls.py**
```
path('create/', views.SchoolCreateView.as_view(), name='create')

```

#### Templates
* **basic_app/school_form.html** -> standard path
```
{% extends "basic_app/basic_app_base.html"%}

{% block body_block %}

<h1>
	{% if not form.instance.pk %}
	Create School
	{% else %}
	Update School
	{% endif %}
</h1>

<form method="post">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit" class="btn btn-primary" value="Submit"> 
</form>
{% endblock %}
```

## Update

#### App

* **views.py** -> Create UpdateViewClass;

```
class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')  # note: we don't want the location to be updated
    model = models.School
    #the class calls the school_form.html page (same as the creation view) but just exihibits the above fields


```

* **urls.py** -> add new urlpattern
```
path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
```

#### Templates
* **basic_app/school_detail.html** -> Adds a button that redirects to the basic_update url and pass in the primary key from the school beeing showed; 

```
<div class="container">
	<p>
		<a class="btn btn-warning" href="{% url 'basic_app:update' pk=school_detail.pk%}">
			Update
		</a>
	</p>
</div>

```

## Delete

#### App

* **views.py**
```
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
    #url to redirect if deleted
```

* **urls.py**
```
path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
```

#### Templates
* **basic_app/school_confirm_delete.html**
```
{% extends 'basic_app/basic_app_base.html'%}

{% block body_block %}
<h1>Delete {{school.name}}?</h1>
<form method="POST">
	{% csrf_token %}
	<input type="submit" class='btn btn-danger' value="Delete">
	<a href="{% url 'basic_app:detail' pk=school.pk%}">
		Cancel
	</a>
</form>
{% endblock %}
```

