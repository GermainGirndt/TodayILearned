# Django - Advanced Topics
* probably not that advanced at all for experienced python developers

## Class-Based Views

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

#### Before
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
