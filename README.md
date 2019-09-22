

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


TO turn active folder into git repository, run
```git init```
```git add -A```
```git commit -am "initial commit"```



To export a list of dependencies to a requirements file, run
```pip freeze > requirements.txt```

And to install all dependencies from requirements file, run
```pip install -r requirements.txt```
