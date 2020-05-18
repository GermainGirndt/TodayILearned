# Django Authentication

---
## 1. Getting Started


#### Terminal
```
pip install django[argon2]
pip install bcrypt
```


---
## 2. Hashers


#### Main

* **settings.py** -> add password hashers
```
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]
```
* **settings.py** -> increase min. password length at AUTH_PASSWORD_VALIDATORS
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length':9}
    },



#### Root

* **media** -> create a media foder for user's media and register it in the settings.py file

```
MEDIA_DIR = os.path.join(BASE_DIR, "media")
.   
.   
.   

#MEDIA
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
```
