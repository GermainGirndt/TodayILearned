# Django - Other Notes

## kwargs
* **models.py** - they're normally used to pass in key props that are going to be used in the next page's url

* **views.py** - use the get_context_data method to get data from the DB and inject it into the page's context. 
* Here, I'm using super().get_context_data to get to the primary key that's already in the page (url/:model/:pk) and use it to call for the object in the db I wanna use.


```
class DetailPoA(generic.TemplateView):
    template_name = 'poa/poa_detail.html'  # defines template

    def get_context_data(self, **kwargs):  # defines context
        context = super().get_context_data(**kwargs)
        poa_data = models.PoA.objects.get(pk=context["pk"])
        context['poa'] = poa_data
        return context
```


## Adding labels to generic Create View

```

# Create your views here.
class CreatePoA(generic.edit.CreateView):
    model = models.PoA
    fields = "__all__"

    redirect_field_name = 'blog/post_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.request.pk)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def add_placeholder(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CreatePoA, self).get_form(form_class)
        form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'John Snow'})
        return form
```

## Verbose field form (overwrittes placeholders and label)

* **verbose_name=('Chapter number')**
```
from django.db import models

class PoA(models.Model):
    nome = models.CharField(max_length=100, verbose_name=('Chapter number'))
...
```