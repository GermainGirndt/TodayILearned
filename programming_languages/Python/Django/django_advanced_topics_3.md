# Django - Advanced Topics 3 - Others
probably not that advanced at all for experienced python developers

## Login Required 

#### views.py

* **Before**
```
from django.contrib.auth.decorators import login_required

@login_required
def post_view(request):
    ...
```

* **After** -> Adds Mixin for loggin required

```
from django.contrib.auth.mixins import LoginRequiredMixin

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
```

## Query Set
A QuerySet represents a **collection of objects** from your database.  
It **translates query** and can have zero, one or many filters (instance.objects).


#### Post.objects.filter(published_date__lte=CONDITION)

**SQL Translation**
```
SELECT * FROM Post where published_date <= DATE
```
**Python Code Example**

```
class PostListView(ListView):
    model = Post

	#'SELECT * FROM Post where published_date <= timezone.now...;
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

```


## Login/Logout


#### Main

* **urls.py**
```
from django.contrib.auth import views
...
urlpatterns = [
	path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout', kwargs={'next_page': '/'})
]
```

#### Templates/blog/registration
* **login.html**

```
{% extends 'blog/base.html'%}

{% block content %}
<div class="jumbotron">
	<h2>Please Login:</h2>
	<br>
	<h3>(Must be a SuperUser, please check with the site admin)</h3>

	{% if form.errors %}
	<p>Your username and pssword didn't match! Please try again.</p>
	{% endif %}

	<form action="{% url 'login' %}" method="POST">
		{% csrf_token %}
		{% form.as_p %}
		<input type="submit" class="btn btn-primary" name="" value="Login">
		<!-- For the context 'next' (next_page)-->
		<input type="hidden" name="next" value={{next}}>
 
	</form>
</div>
{% endblock %}
```


## Access object's atribbutes using class views


#### App

* **views.py**

```
class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Post

    def get_success_url(self):
        obj = self.get_object()
        if obj.published_date:
            return reverse_lazy('post_list')
        else:
            return reverse_lazy('post_draft_list')
```


## Widgets
Utilize widgets to pass in css classes or placeholders

* **forms.py**
```
class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # for modifing the forms css classes itself
        widgets = {
            'title': forms.TextInput(attrs={'class': 'post-title', 'placeholder': 'Title PH'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea post-content',
                                          'placeholder': 'This is the text placeholder'})
        }
```