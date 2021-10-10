# Test App
Following are the steps to be taken for project setup.

### Creating Virtual environment:

**Linux**
Ubuntu
  
    virtualenv -p python3 my_venv
    source my_venv/bin/activate


### Install Requirements:

    pip install -r requirements.txt

### Run migrate command to create tables with respective field in database :
	python manage.py migrate

   
### Run Commands to load the dummy data:
    python manage.py save_medals
    python manage.py save_levels
    python manage.py save_users

**save_medals** : This management command will store medals in database with minimum score required to achieve that medal.
**save_levels** : This management command will store levels in database with the maximum score of that level.
**save_users** : This management command will store users in database, will assign medals and levels according to there score.

### Admin Access:
To access the admin interface you need to create a superuser.

	python manage.py createsuperuser
	

### Starting Django server:
	python manage.py runserver

