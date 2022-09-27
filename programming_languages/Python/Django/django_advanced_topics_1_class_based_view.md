# Django - Advanced Topics 1 - Class Based View
* probably not that advanced at all for experienced python developers

## Class-Based View

#### Before
* **views.py**
```
def index(request):
		return HttpResponse('Function views are middle cool')
```
* **urls.py**
```
path('', views.index)
```

#### After
* **views.py**
```
class CBView(View):
	def get(self, request):
		return HttpResponse('Class based views are cool')
```
* **urls.py**
```
path('', views.CBView.as_view())
```


## Class-Based Template View

#### Unchanged
```
{% extends "base.html" %}

{% block body_block %}
	<h1>Testing template view! Index Page Home!</h1>
	<h2>Injected Content {{ inject_me }}</h2>
{% endblock %}
```

#### Before
* **views.py**
```
def index(request):
	context = {'inject_me': 'BASIC INJECTION!'}
		return render(request, 'index.html', context=context)
```

#### After
* **views.py**
```
from django.views.generic import TemplateView
.
.
.

class IndexView(TemplateView):
    template_name = 'index.html' #defines template

    def get_context_data(self, **kwargs): #defines context
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION!'
        return context
```


## ListView
Renders automatically a template page named **MODEL_list.html**   
Pass in a **list as context** containing all model instances

#### Templates
* **school_list.html** -> receives the list 'schools' s context;   
adds a link to the DetailView (see next section)

```
{% extends "basic_app/basic_app_base.html" %}

{% block body_block %}
	<h1>Welcome to a list of all the schools!</h1>
	<ol>
		{% for school in schools %}

			<h2>
				<a href="{{school.id}}">
					<li>
						{{ school.name }}
					</li>
				</a>
			</h2>

		{% endfor %}
	</ol>
{% endblock %}
```
#### App

* **urls.py**
```
urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
```

* **views.py**
```
from django.views.generic import ListView
.
.
.
# Creates context item school_list (MODELNAME_list)
# Pass in context and renders automacally the template school_list.html (standard filename)
class SchoolListView(ListView):
	# Redefines the object context name; standard would be school_list
    context_object_name = 'schools'  
    model = models.School


```
## DetailView
**Requires a PK** to be passed in   
Renders a page with the PK path that **details attributes of a model instance**    




#### Templates
* **school_detail.html** -> receives the instance schools[pk];   
renames it as school_detail for use

```
{% extends 'basic_app/basic_app_base.html' %}
{% block body_block %}
<div class="jumbotron">
	<h1>Welcome to the School Detail Page</h1>
	<br>
	<h3>School details:</h2>
	<p>Name: {{ school_detail.name }}</p>
	<p>Principal: {{ school_detail.principal }}</p>
	<p>Location: {{ school_detail.location }}</p>

	<h3>Students:</h3>
	<br>
	<ol>
		{% for student in school_detail.students.all %} 
		<!-- #access all instances of the foreign key students  linked to this specific school-->
			<li><strong>{{ student.name }}</strong> who is <strong>{{ student.age }}</strong></li>
	{% endfor %}
	</ol>
</div>
{% endblock %}
```

#### App

* **urls.py** -> passes in the PK to the SchoolDetailView class

```
url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail')
```
**or**
```
path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail') 
```

* **views.py**
```
from django.views.generic import DetailView
.
.
.
class SchoolDetailView(DetailView):
    # Shows an instance of the school list;
    # receives automatically the instances corresponding primary key as context from urls.py
    context_object_name = 'school_detail'  # standard context_object_name would be just school
    model = models.School
    template_name = 'basic_app/school_detail.html'
```