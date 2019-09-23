# DeepLab

DeepLab is an application which streamlines acquisition and analysis of data from laboratory experiments by enabling direct connectivity with instuments and data from the browser. This README documents the use and construction of the application.


# Building the project 

## Initialize the project

To activate virtual environment named _env_, navigate to project folder (```cd deeplab```) and run  
```source env/bin/activate```  

To deactivate, run  
```deactivate```  

To install Django, inside the environment run  
```pip install django```  

To test installation, run  
```python```  
```import django```  
```django.get_version()```  

To create django project, run  
```django-admin startproject mysitename```  
where ```mysitename``` is the name of the project.

To run the project on the on the testing server, navigate to the inner project filder which contains _manage.py_ and run  
```python manage.py runserver```  

## Create an app

To create an app in the project named _polls_, naavigate to the outter project folder containing _manage.py_ and run  
```python manage.py startapp polls```  

The app view can be edited inside _views.py_ in the _polls_ folder. Then the view must be called by mapping it to a URL. To do this, create _urls.py_ in the _polls_ folder. Now the root URLconf needs to point at the _polls.urls_ module. That can be done in the root _urls.py_. 


# Database management

## Creation of data tables and models

To create tables in the database before it is used, run  
```python manage.py migrate```  
The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your myproject/settings.py file and the database migrations shipped with the app.  

To update changes in the database tables, run  
```python manage.py makemigrations polls```  
where _polls_ is the name of the app.

Then again to create the tables run  
```python manage.py migrate```  

Generally, changes to the database model can be made in three steps:  
(1) Change your models in _models.py_.  
(2) Run ```python manage.py makemigrations``` to create migrations for those changes.  
(3) Run ```python manage.py migrate``` to apply those changes to the database.  

## Examining tables using the Django API

To open the python shell inside the project, run  
```python manage.py shell```  

To examine some database structures using the classes _Choice_ and _Question_:  
```from polls.models import Choice, Question  # import the models```  
Create a new question:  
```from django.utils import timezone```  
```q = Question(question_text="What's new?", pub_date=timezone.now())```  
```q.save```  
```q.id```  
```Question.objects.all()```  
```Question.objects.filter(id=1)```  
```Question.objects.filter(question_text__startswith='What')```  
```q.choice_set.create(choice_text='Not much', votes=0)```  
```q.choice_set.create(choice_text='The sky', votes=0)```  
```c = q.choice_set.create(choice_text='Just hacking again', votes=0)```  
```c.question()```  
```q.choice_set.all()```  
```q.choice_set.count()```  
```c = q.choice_set.filter(choice_text__startswith='Just hacking')```  
```c.delete()```  


# Creating an administrator page

Create an admin account by  
```python manage.py createsuperuser```  
Start the admin site by ```python manage.py runserver``` and go to _/admin/ on the local domain.  


# Using Git
## Setup Git repository

To turn active folder into git repository, run  
```git init```  
```git add -A```  
```git commit -am "initial commit"```  

To send to a Github repository, run  
```git remote add origin https://github.com/ericmuckley/DeepLab.git```  
```git push -u origin master```  

## Push future updates to Github

For future pushes to Github, run  
```git add *```
```git commit -am "commit message"```  
```git push origin master```  


# Deploy the app


To run the project on the on the testing server, navigate to the inner project filder which contains _manage.py_ and run  
```python manage.py runserver```  

To view administrator page, go to  the /admin page at the host address.  

Before deploying, change ```DEBUG = True``` to ```DEBUG = False``` in _settings.py_.  

To export a list of dependencies to a requirements file, run  
```pip freeze > requirements.txt```  

And to install all dependencies from requirements file, run  
```pip install -r requirements.txt```  
