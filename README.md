# Drops of Life

## Key Points
- Each modules will be implemented using one or more **apps**
- Each app is responsible for doing only a **single job**
- Each app consists of a **model**, **view**
- **model.py** contains some classes, each class represents a **db table**
- **view.py** performs any backend jobs required and renders html pages in response to a **requested url**

## Project Structure
Monitor how the app **polls** is structured.
On starting a new app with ```python manage.py startapp```, the following files were automatically created
- admin.py
- app.py
- models.py
- tests.py
- views.py
```
└───DropsOfLife
    │   db.sqlite3
    │   manage.py
    │   README.md
    ├───DropsOfLife
    │   │   asgi.py
    │   │   settings.py
    │   │   urls.py
    │   │   wsgi.py
    │   │   __init__.py
    └───polls
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   urls.py
        │   views.py
        │   __init__.py
        ├───static
        │   └───polls
        │       └───css
        │               style.css
        │
        ├───templates
        │   └───polls
        │           detail.html
        │           index.html
        │           results.html
```

- All the static files (image, css, js) for an app (say myapp) should be under the directory ```myapp/static/myapp/<image, css, js>/myfile```.
- All the html files for myapp should be under the directory ```myapp/templates/myapp/myhtml.html```.
***This convention has to be maintained***

## How to proceed
- If you want to create/implement a new module use ```python manage.py startapp newapp```
- If you want add a certain static file or an html file under a certain existing app, make sure the file is in the correct folder for that app

## Creating a new app
To create a new app named **myapp** under the directory **MyDirectory**:
```bash
mkdir MyDirectory
cd MyDirectory
python ../manage.py startapp myapp
```

Correctly configure the ***name*** attribute of **myapp/apps.py**
```python
from django.apps import AppConfig


class myappConfig(AppConfig):
    name = 'MyDirectory.myapp'
``` 

Include this app in INSTALLED_APPS of **settings.py** 
```python
INSTALLED_APPS = [
    'MyDirectory.myapp.apps.myappConfig',
    'django.contrib.admin',
    ...
]
```

Create **urls.py** for this app
```
MyDirectory/myapp/urls.py
```

Include this under root urls
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myappurl/', include('MyDirectory.myapp.urls')),
]
```

## HTML File editing
There are 3 html files, which are of massive interest. Those 3 are:
> navbar.html \
> sidebar.html \
> skeleton.html

All 3 can be found in ```home/templates/skeleton/```. \
The motivation behind these 3 files is to reduce repeating codes, for every html files.
For example, every webpage should have the same sidebar. So it's inefficient and 
error prone to write the same code for sidebar in html files for every webpage.

### navbar.html
Contains the code for navbar

### sidebar.html
Contains the code for sidebar 

### skeleton.html
Contains the **skeleton code for every other html page to extend from**. \
This file is of **extreme importance** to us. So let's spend a minute trying to 
understand how this works.
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Request Blood</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'home/css/style.css' %}">

    {% block myStyle %}
    {% endblock %}

    <script src="https://kit.fontawesome.com/8fd9809be9.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>

    <div class="wrapper">

        {% include 'skeleton/sidebar.html' %}

        <div class="main_content">
            {% include 'skeleton/navbar.html' %}

            {% block myBody %}
            {% endblock %}
        </div>
    </div>

    {% block myScript %}
    {% endblock %}
</body>

</html>
```

One look over this code and we can see some differences between ```skeleton.html``` with
a regular html file. There are many lines that has the symbol ```{% %}```. Let's
analyze those specific lines one-by-one.

#### Referencing a css file from inside html using {% static .. %}
```html
{% load static %}
<link rel="stylesheet" href="{% static 'home/css/style.css' %}">
```
- The above two lines tell django that there is a file named ```style.css``` in the
directory > ```home/css/```. 
- Include that css file as a stylesheet.


#### Including code from another html file using {% include .. %}
```html
<div class="wrapper">

        {% include 'skeleton/sidebar.html' %}
        ...
</div>
```

- The syntax ```{% include <file_name> %}``` is used to tell django, that we want to 
**replace this line with all the contents of** ```file_name```. Say from the above
example, ```sidebar.html```:
```html
<p>Hello</p>
<p>World</p>
``` 

- Then, the first bit of codes would become
```html
<div class="wrapper">

        <p>Hello</p>
        <p>World</p>
        ...
</div>
```


#### Creating empty _pockets_ using {% block .. %}
I'm using the term _pocket_, which might not make any sense as of now, but hopefully
will be clear when we create other html pages __extending__ from  ```skeleton.html```. \
For now, let's analyze these lines:
```html
<div class="main_content">
    ...
    {% block myBody %}
    {% endblock %}
    ...
</div>
```
- ```{% include 'skeleton/navbar.html' %}``` replaces this line of code with 
contents from ```skeleton/navbar.html```
- ```{% block myBody %}{% endblock %}``` creates a __pocket__ in this file

#### Using these _pockets_ with {% extends .. %}
Now that we have created a ```skeleton.html``` with some empty _pockets_, we can
create other html files. Say, we want to create a home page ```homepage.html```:
```html
{% extends 'skeleton/skeleton.html' %}

{% block myBody %}
This is homepage
{% endblock %}
``` 
- We are telling django to create ```homepage.html``` with the same content as
 ```skeleton.html```
- But remember that ```skeleton.html``` has some pockets??
- We thus, now, have the **option** to fill in those pockets with some extra codes
- Here, we filled the pocket ```myBody``` with ```This is homepage```
- Final result:
```html
<div class="main_content">
    ...
    This is homepage
    ...
</div>
```

## Summary
- For all the webpages, we will simply _extend_ from ```skeleton.html```
- Fill the empty pockets of ```skeleton.html``` according to that particular webpage