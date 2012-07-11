Django applications
===================

todo
----
- ToDo list web application (simple)


Installation/Usage
------------------

In order to get the django environment running, you need to do the following:

- install Python 2.7 (not 3.x)
	- add python to your PATH, if it isn't already
- install pip
	- from Python_Dir/bin (Python_Dir\Scripts on Windows) run:
	    - easy_install pip
- cd to the project dir (wherever you clone:d the git repo)
- run pip:
	- pip install -r requirements/dev.txt
- run the django development web server
	- python manage.py runserver
- point your browser to http://localhost:8000/app_name (e.g. http://localhost:8000/todo ) 