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

```