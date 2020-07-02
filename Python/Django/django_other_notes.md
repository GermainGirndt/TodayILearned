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