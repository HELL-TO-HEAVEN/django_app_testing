# DeepLab

DeepLab is an application which streamlines acquisition and analysis of data from laboratory experiments.


# Building the project 

## Initialize the project

To activate virtual environment, navigate to project folder and run  
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

Before deploying, change ```DEBUG = True``` to ```DEBUG = False``` in _settings.py_.  

To export a list of dependencies to a requirements file, run  
```pip freeze > requirements.txt```  

And to install all dependencies from requirements file, run  
```pip install -r requirements.txt```  
