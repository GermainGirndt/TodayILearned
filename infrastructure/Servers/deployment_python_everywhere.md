# Upload a server - Python Everywhere


# Local: 
### Preparation
* **Add server to allowed hosts (settings.py)**
```
ALLOWED_HOSTS = ['username.pythonanywhere.com']
```
* **Upload repository to GitHub**


# On PE's Terminal:

### Create venv
```
mkvirtualenv --python=python3.7 myproj
pip install -u django=3.0.6
```

### Switch between venv
```
workon myproj
```

### Check install
```
which django-admin.py
```

### Host Terminal

* **Clone repository**
* **Run migrations/makemigrations**
* **Create super user**
* **Run migrations/makemigrations ?**

### Create new web app

* **Choose Manual Settings**
* **Add created virtual env**
```
/home/user/.virtualenvs/myproj
```
* **Source code (project)**
```
/home/user/github_repo_name/project_folder
```

* **Configure WSGI file**
```
import os
import sys

path = '/home/user/github_repo_name/project_folder'
if path not in sys.path:
    sys.path.append(path)
os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_folder.settings")

import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Add static files

**1.**
```
name: /static/admin

path: /home/user/.virtualenvs/myproj/lib/python3.7/site-packages/django/contrib/admin/static/admin
```
**2.**
```
name: /static/

path: /home/user/github_repo_name/project_folder/
```

### Finishing

* **Set debug to False (settings.py)**

* **Reload the web app**