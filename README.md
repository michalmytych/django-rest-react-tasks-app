# Django Rest Framework & React To-Do App

_Python3+, Pip3 required._

__Setup:__

```bash
# clone repository then:

# install react and other required npm packages
cd django_rest_react_task_app/frontend && npm install

# create python3 virtualenv
cd ../backend && python3 -m venv venv && source venv/bin/activate

# install required packages with pip3
pip3 install -r requirments.txt

# setup django app:
python3 manage.py makemigrations && python3 manage.py migrate

# optionally fill database with sample data:
python3 manage.py loaddata < data.json

# If you decide to use sample data:
# Username: ernest1899
# Password: password123456
```

__Running apps:__
```bash
# In 1st terminal instance being in "django_rest_react_task_app/frontend":
npm start

# In 2nd terminal instance being in "django_rest_react_task_app/backend":
python3 manage.py runserver

# *** React app running on localhost port 3000, Django app on 8000 ***
```

### Preview:

![preview_todo](https://user-images.githubusercontent.com/59512535/97160641-f2186280-177c-11eb-9087-d9b1dc0a073a.gif)