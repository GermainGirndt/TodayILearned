# Django Modules

## Debug Toolbar

#### Terminal
```
pip install django-debug-toolbar
```

#### Main

* **settings.py** -> insert to installed_apps, middleware and set internal_ips
```


INSTALLED_APPS = [
	.
	.
	.

    'debug_toolbar',
    .
    .
    .
]


MIDDLEWARE = [
	.
	.
	.
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


.
.
.

INTERNAL_IPS = ['127.0.0.1']

```

* **urls.py**
```
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

```

---

## Bootstrap for Forms

#### Terminal
```
pip install django-bootstrap4.
```

#### Main

* **settings.py** -> include as installed app

```
'bootstrap4'
```

#### Templates
* **post_form.html** -> load bootstrap and apply it to form
```
{% extends "posts/post_base.html" %}
{% load bootstrap4 %}


{% block post_content %}
	<h4>Create a new post</h4>

	<form id='postForm' action="{% url 'posts:new' %}" method="POST">
		{% csrf_token %}
		{% bootstrap_form form %}
		<input type="submit" value="POST" class="btn btn-warning btn-large" name="">

	</form>
{% endblock post_content %}
```

---

## MISAKA - Using Markdown

#### Terminal
```
pip install misaka
```

#### Use cases examples

* **models.py** -> by saving of a model, converting markdown to html
```
import misaka
.
.
.

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    # Save method; treats the data and save

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
```

# Braces - for SelectRelatedView
```
pip install django-braces
```

* **views.py**

```
from braces.views import SelectRelatedMixin


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    # from the mixin:
    select_related = ('user', 'group')

```