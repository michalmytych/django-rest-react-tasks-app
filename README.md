# Django Rest Framework & React To-Do App

_Python3+, Pip3, Node.js, npm required._

__Setup:__
```bash
# After cloning repo to your local machine, just:

cd django-rest-react-tasks-app

# and

bash setup.sh   # you may need to : chmod +x setup.sh before executing it 

# If you decide to use sample data:
# Username: ernest1899
# Password: password123456
```


## Running apps:

__Running React frontend__
In 1st terminal instance being in "django-rest-react-tasks-app/frontend":
```bash
npm start
```

If you choose to automatically run Django API after setup via setup script, you don't have to do the next step.

__Running Django API__
In 2nd terminal instance being in "django-rest-react-tasks-app/backend":
```bash
python3 manage.py runserver
```

### Preview:

![preview_todo](https://user-images.githubusercontent.com/59512535/97160641-f2186280-177c-11eb-9087-d9b1dc0a073a.gif)
